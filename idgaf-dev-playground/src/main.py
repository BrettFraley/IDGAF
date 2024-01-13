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


# Load configuration, setup, and launch Server
run(host='localhost', port=8080, debug=True, reloader=True)
