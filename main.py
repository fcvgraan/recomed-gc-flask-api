import datetime
import pytz
import businesstimedelta
import holidays as pyholidays

def http_trigger(request):
    """ HTTP Cloud Function
    Arg: request (flask.Request)
    Res: arg(s) for flask.make_response
    """
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')

    diff = calculateBusinessTime()
    return 'diff is: {}'.format(diff)

def calculateBusinessTime():

    # Define a working day
    workday = businesstimedelta.WorkDayRule(
    start_time=datetime.time(8),
    end_time=datetime.time(17),
    working_days=[0, 1, 2, 3, 4])

    sa_holidays = pyholidays.ZA()
    holidays = businesstimedelta.HolidayRule(sa_holidays)
    businesshrs = businesstimedelta.Rules([workday, holidays])

    # Thursday 24 September 2020 was a public holiday in South Africa
    start = datetime.datetime(2020, 9, 23, 8, 0, 0)
    end = datetime.datetime(2020, 9, 25, 17, 0, 0)

    bhours = businesshrs.difference(start, end).hours

    return bhours
