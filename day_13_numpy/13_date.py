"""
Create a python function named **date_array** that accepts two dates as string format and returns a numpy array of dates between those 2 dates. The function only accept 2 strings, otherwise raise error. The date format should be like this only: `2022-12-6`. The end date should be included and for simplicity, choose dates from a same year.
"""
 

import numpy as np

def date_array(start_date, end_date):

    if not isinstance(start_date, str) or not isinstance(end_date, str):
        raise TypeError(
            "Both dates must be strings."
        )
    
    try:
        start = np.datetime64(start_date)
        end = np.datetime64(end_date)
    except ValueError:
        raise ValueError(
            "Date format must be YYYY-MM-DD."
        )
    
    start_year = str(start)[:4]
    end_year = str(end)[:4]
    if start_year != end_year:
        raise ValueError(
            "Both dates must be in the same year."
        )
    if start > end:
        raise ValueError(
            "Start date cannot be after the end date."
        )

    return np.arange(
        start,
        end + np.timedelta64(1, "D"),
        dtype="datetime64[D]"
    )


result = date_array(
    "2022-07-31",
    "2022-08-16"
)

print(result)

