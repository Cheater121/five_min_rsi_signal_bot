from datetime import datetime


def time_checker():
    now = datetime.now()
    if now.second == 0:
        return True
