def get_session_msgs(request):

    # get session data if available
    success_msg = request.session.get('success_msg')
    error_msg = request.session.get('error_msg')

    # delete every data from the session so its no more accessible
    if 'success_msg' in request.session:del request.session['success_msg']
    if 'error_msg' in request.session:del request.session['error_msg']

    return (success_msg,error_msg)