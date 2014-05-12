**Python**

``import datetime as dt``

| ``# Add an entry for the current time``
| ``log_name = "temperature"``
| ``log_value = 21.5``
| ``AddTimeSeriesLog(inOutWS, Name=log_name, Time=dt.datetime.utcnow().isoformat(), Value=log_value)``
