# from sqlalchemy.dialects.postgresql import insert
# from sqlalchemy.sql import text, delete


# def upsert(model, data, constraint, excluded=None):
#     table = model.__table__
#     if excluded is None:
#         excluded = []
#     stmt = insert(table).values(data)
#     # Note: for now the excluded array is empty if there is a need to
#     # exclude some columns when preforming an upsert then the calling
#     # method should declare these columns as an array of strings that
#     # would not be updated
#     update_cols = [c.name for c in table.c
#                    if (c not in list(table.primary_key.columns) and c not in excluded)]
#     update_cols.remove('created_date')
#     return stmt.on_conflict_do_update(
#         constraint=constraint,
#         set_={k: getattr(stmt.excluded, k) for k in update_cols})


# # this upsert should only be used when scaling becomes an issue and we need to use raw sql to upsert
# # it was designed to fit a specific use case and is not generic
# def raw_upsert(model, data, constraint, excluded=None):
#     table = model.__table__
#     if excluded is None:
#         excluded = []
#     cols = ', '.join(data.keys())
#     row = ', '.join([f"'{value}'" for value in data.values()])
#     update_cols = [(c, v) for c, v in data.items()
#                    if (c not in list(table.primary_key.columns) and c not in excluded)]
#     return text(f"""
#         INSERT INTO {table} ({cols})
#         VALUES ({row})
#         ON CONFLICT ON CONSTRAINT {constraint}
#         DO UPDATE SET {','.join([f"{k}='{v}'" for k, v in update_cols])};
#         """)


# def delete_all(model, timestamp):
#     table = model.__table__
#     return delete(table).where(table.c['event_date'] <= timestamp)

# def clean_up_with_time_range(table, time_range):
#     return text(f"""
#       delete
#         from native_touch.{table} ic
# 	  where
#         ic.end_date < (SELECT EXTRACT(EPOCH FROM (NOW() - INTERVAL '{time_range}')) * 1000 AS two_years_in_millis)
#     """)
