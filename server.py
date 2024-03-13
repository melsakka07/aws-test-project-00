from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os

def hello_world(request):
    name = os.environ.get('NAME_01')
    if name == None or len(name) == 0:
        name = "world"
    message = "Hello, " + name + "!\n"
    return Response(message)

if __name__ == '__main__':
    port = int(os.environ.get("PORT"))
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    
    # Retrieve environment variables
    name01 = os.environ.get('NAME_01')
    name02 = os.environ.get('NAME_02')
    name03 = os.environ.get('MY_VAR_EXAMPLE_01')
    name04 = os.environ.get('MY_VAR_EXAMPLE_02')
    name05 = os.environ.get('MY_APP_PORT')

    # Print each environment variable on a new line
    print(name01)
    print(name02)
    print(name03)
    print(name04)
    print(name05)

    server = make_server('0.0.0.0', port, app)
    server.serve_forever()
