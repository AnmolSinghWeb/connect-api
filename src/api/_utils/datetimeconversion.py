from datetime import datetime, timedelta
import pytz

DAY_IN_EPOCH_MILLIS = 86400000
def epoch_now_millis():
    return int((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds() * 1000)
def utcoffset():
    return int(datetime.now(pytz.timezone("America/New_York")).utcoffset().total_seconds() * 1000)

def yesterday_midnight_est_epoch():

    now_utc = datetime.now(pytz.utc)

    # Convert current time to EST
    now_est = now_utc.astimezone(pytz.timezone('US/Eastern'))

    # Calculate yesterday at midnight in EST
    yesterday_midnight_est = now_est.replace(hour=0, minute=0,
                                             second=0, microsecond=0) - timedelta(days=1)

    # Convert yesterday at midnight in EST to epoch time
    return (yesterday_midnight_est - datetime(1970, 1, 1,
                                                    tzinfo=pytz.utc)).total_seconds() * 1000
