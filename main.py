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
    if request.method == 'GET':
        start_time = request.args.get('start_time')
        end_time = request.args.get('end_time')

        start_time_parsed = dateutil.parser.parse(start_time)
        end_time_parsed = dateutil.parser.parse(end_time)

        business_seconds = calculate_business_time(start_time_parsed, end_time_parsed)
        return str(business_seconds)
    
    else:
        return 'Request method is ' + str(request.method) + ', only GET is allowed'

def calculate_business_time(start, end):

    # Define a working day
    workday = businesstimedelta.WorkDayRule(
    start_time=datetime.time(8),
    end_time=datetime.time(17),
    working_days=[0, 1, 2, 3, 4])

    sa_holidays = pyholidays.ZA()
    holidays = businesstimedelta.HolidayRule(sa_holidays)
    businesshrs = businesstimedelta.Rules([workday, holidays])

    startDateTime = datetime.datetime(start.year, start.month, start.day, start.hour, start.minute, start.second)
    endDateTime = datetime.datetime(end.year, end.month, end.day, end.hour, end.minute, end.second)

    business_hours = businesshrs.difference(startDateTime, endDateTime).hours
    business_seconds = businesshrs.difference(startDateTime, endDateTime).seconds

    total_seconds = (business_hours*60*60) + (business_seconds)

    return total_seconds
