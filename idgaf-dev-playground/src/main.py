import os, json, urllib, sqlite3

from bottle import route, get, post, request, response, run, template, static_file, TEMPLATE_PATH

class DBSettings():
    def __init__(self):
        self.dbPath = "../data/"
        self.devSessionsPath = "../data/dev-sessions"
        self.testTablesPath = "../data/test-tables"
        

dbSettings = DBSettings()


# Static Paths
@route('/static/<filename>')
def serve_static(filename):
    return static_file(filename, root='./views/static')

@route('/documentation/<filename>')
def serve_static_documentation(filename):
    return static_file(filename, root='../documentation')

@route('/styles/<filename>')
def serve_styles(filename):
    return static_file(filename, root='./views/styles')

# Landing Page
@route('/')
def home():
    return template('./views/home')

@route('/dev-sessions')
def devSessions():
    return template('./views/metadata-views/dev-sessions')

@route('/setup-dev-sessions-table/<devSessionFileName>')
def setupDevSessionsTable(devSessionFileName):
    
    con = sqlite3.connect(f"{dbSettings.dbPath}{devSessionFileName}.db")
    cursor = con.cursor()
    table = f"CREATE TABLE dev_sessions(id INTEGER PRIMARY KEY, username TEXT, start_time TEXT, end_time TEXT, session_notes TEXT, commits TEXT)"
    cursor.execute(table)
    con.commit()
    con.close()

    return f"</p> New Dev Session Table Created. SQLite filename: {devSessionFileName}</p>"

# Testing Routes

@route('/test-lab')
def testLab():
    return template('./views/metadata-views/test-lab')

@route('test-lab/git-history')
def testLabGitHistory():
    history = os.system("git log")
    print(history)
    return template('./views/metadata-views/test-lab', gitHistory=history)

# Project Management Routes
@route('/project-management')
def projectManagement():
    return template('./views/project-management/project-management-dashboard.tpl')


# UTILITY ROUTES
@route('/docs')
def docs():
    return template('./views/docs/docs.tpl')


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
