import os
import json
import urllib

from bottle import route, get, post, request, response, run, template, static_file, TEMPLATE_PATH

# Static Paths
@route('/static/<filename>')
def serve_static(filename):
    return static_file(filename, root='./views/static')

@route('/styles/<filename>')
def serve_styles(filename):
    return static_file(filename, root='./views/styles')

# Landing Page
@route('/')
def home():
    return template('./views/home')

@route('/test')
def test():
    sys = os.name
    f = ""
    d = ""
    with open("../.gitignore") as fp:
        f = fp.read()

    # Note: OS functions from the context of a route, main, 
    # or public dir should be sandboxed and not aloud to do this.
    with open("../../../dev.txt") as dev:
        d = dev.read()

    return f"<h1>OS: {sys}</h1> <h2>.gitignore</h2> <p>{f}</p> <p>{d}</p>"

# Load configuration, setup, and launch Server
run(host='localhost', port=8080, debug=True, reloader=True)
