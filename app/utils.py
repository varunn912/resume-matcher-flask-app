from datetime import datetime
import pytz

def get_ist_time():
    """Returns the current time in Indian Standard Time (IST)."""
    return datetime.now(pytz.timezone('Asia/Kolkata'))