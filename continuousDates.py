import datetime
import pandas as pd

"""
This code is very useful to create a list of continuous dates.
"""

class ContinuousDates:

    def createContinousDates(self, year: int, month: int, day: int, number_of_dates: int):
        dates = pd.DataFrame()
        start_date = datetime.date(year, month, day)
        date_list = [start_date + datetime.timedelta(days=idx) for idx in range(number_of_dates)]
        dates['Date'] = date_list
        return dates, date_list
