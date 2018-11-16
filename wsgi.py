import json

def application(environ, start_response):
    start_response('200 OK', [('Content-Type','text/plain'),('Syndesis-Test', 'openshift-pong-py')])
    resp = {}
    for k, v in environ.items():
        if k.startswith("HTTP_"):
            print(k, ":", v)
            resp[k] = v
    resp["QUERY_STRING"] = environ["QUERY_STRING"]
    return [bytes(json.dumps(resp), 'ascii')]
