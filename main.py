def http_trigger(request):
    """ HTTP Cloud Function
    Arg: request (flask.Request)
    Res: arg(s) for flask.make_response
    """
    start_time = request.args.get('start_time')
    end_time = request.args.get('end_time')
    return 'Start time is: {}, and end time is: {}'.format(start_time,end_time)