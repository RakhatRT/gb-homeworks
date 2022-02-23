msg = ""
MINUTE_DURATION = 60
HOUR_DURATION = MINUTE_DURATION * 60
DAY_DURATION = HOUR_DURATION * 24
time_struct = {"days": 0, "hours": 0, "minutes": 0, "seconds": 0}

"""Request input"""
timestamp = int(input('Input duration in seconds: '))

""" Calculate duration parts"""
if timestamp >= DAY_DURATION:
    time_struct['days'] = int(timestamp / DAY_DURATION)
    timestamp = timestamp - (DAY_DURATION * time_struct['days'])

if timestamp >= HOUR_DURATION:
    time_struct['hours'] = int(timestamp / HOUR_DURATION)
    timestamp = timestamp - (HOUR_DURATION * time_struct['hours'])

if timestamp >= MINUTE_DURATION:
    time_struct['minutes'] = int(timestamp / MINUTE_DURATION)
    timestamp = timestamp - (MINUTE_DURATION * time_struct['minutes'])

time_struct['seconds'] = int(timestamp)

"""Build response message"""
if time_struct["days"] > 0:
    msg = f"{time_struct['days']} дн {time_struct['hours']} час {time_struct['minutes']} мин {time_struct['seconds']} сек"

elif time_struct["hours"] > 0:
    msg = f"{time_struct['hours']} час {time_struct['minutes']} мин {time_struct['seconds']} сек"

elif time_struct["minutes"] > 0:
    msg = f"{time_struct['minutes']} мин {time_struct['seconds']} сек"

elif time_struct["seconds"] > 0:
    msg = f"{time_struct['seconds']} сек"

"""Send response message"""
print(msg)
