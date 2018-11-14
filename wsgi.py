
def application(environ, start_response):
    start_response('200 OK', [('Content-Type','text/plain'),('Syndesis-Test', 'openshift-pong-py')])
    resp = []
    for k, v in environ.items():
        if k.startswith("HTTP_"):
            print(k, ":", v)
            resp.append("{}: {}\n".format(k[5:], v))
    resp.append(environ["QUERY_STRING"])
    return [bytes(v, 'ascii') for v in resp]
