import datetime
import pytz
import businesstimedelta
import holidays as pyholidays
import dateutil.parser

def http_trigger(request):
    """ HTTP Cloud Function
    Arg: request (flask.Request)
    Res: arg(s) for flask.make_response
    """
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')

    startParsed = dateutil.parser.parse(start_time)
    endParsed = dateutil.parser.parse(end_time)

    diff = calculateBusinessTime(startParsed, endParsed)
    return str(diff)

def calculateBusinessTime(start, end):

    # Define a working day
    workday = businesstimedelta.WorkDayRule(
    start_time=datetime.time(8),
    end_time=datetime.time(17),
    working_days=[0, 1, 2, 3, 4])

    sa_holidays = pyholidays.ZA()
    holidays = businesstimedelta.HolidayRule(sa_holidays)
    businesshrs = businesstimedelta.Rules([workday, holidays])

    start = datetime.datetime(start.year, start.month, start.day, start.hour, start.minute, start.second)
    end = datetime.datetime(end.year, end.month, end.day, end.hour, end.minute, end.second)

    bhours = businesshrs.difference(start, end).hours
    bseconds = businesshrs.difference(start, end).seconds

    tsecs = (bhours*60*60) + (bseconds)

    return tsecs