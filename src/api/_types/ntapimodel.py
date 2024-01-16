import re
from api._middleware.validation import validate_generic_data
from api._utils.datetimeconversion import epoch_now_millis

class NtApiModel:

    def __init__(self):
        self.storage_model = None

    def validate_data(self, data, validate_field_presence=True):
        errors = validate_generic_data(
            data,
            self.storage_model.get_columns(),
            ['id', 'is_deleted', 'created_date', 'modified_date'],
            validate_field_presence=validate_field_presence
        )
        return None if len(errors) == 0 else errors

    def get_sql_error_message(self, exception, errors):
        msg = str(exception)
        # The params contains all values used that failed
        errors_sql = []
        if 'duplicate' in msg:
            # It's the only way to get the message from
            regex = r"^DETAIL:  Key .*.\n$"
            matches = re.findall(regex, msg, re.MULTILINE)
            if len(matches) > 0:
                errors_sql.extend(matches)
        if 'invalid input syntax for type uuid' in msg:
            errors_sql.append('invalid UUID format')
        if errors is not None:
            errors_sql.extend(errors)
        return errors_sql if errors_sql else None

    def clean_offset_limit(self, limit, offset):
        clean_limit = max(int(limit), 1) if limit else 0
        clean_offset = max(int(offset), 0) if offset else 0

        return clean_limit, clean_offset

    def init_data_for_creation(self, data):
        epoch_now = epoch_now_millis()
        data['created_date'] = epoch_now
        data['modified_date'] = epoch_now
        data['is_deleted'] = False
