@bp.route('/manifest.json')
def manifest():
    return send_from_directory('static', 'manifest.json')

@bp.route('/sw.js')
def service_worker():
    reponse = make_response(send_from_directory('static', 'sw.js'))
    response.headers['Cache-Control'] = 'no-cache'
    return response