from datetime import (
    datetime, 
    timedelta, 
    timezone
)

def get_now_time(self, time: datetime = None, hours = 8) -> datetime:
    ori = datetime.now(timezone(timedelta(hours=hours))) if not time else time
    return datetime(ori.year, ori.month, ori.day, ori.hour, ori.minute, ori.second)