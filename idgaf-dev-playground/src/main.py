import os, json, urllib, sqlite3

from bottle import route, get, post, request, response, redirect, run, template, static_file, TEMPLATE_PATH

class DBSettings():
    def __init__(self):
        self.dbPath = "../databases/"
        self.devSessionsDB = "../databases/dev-sessions/dev-sessions.db"
        self.testTablesDB = "./databases/test-tables/"
        

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

# Dev Sessions Page
@route('/dev-sessions')
def devSessions():
    con = sqlite3.connect(dbSettings.devSessionsDB)
    cursor = con.cursor()

    getSessionsQuery = "SELECT * FROM sessions;"
    results = cursor.execute(getSessionsQuery)
    sessions = results.fetchall()

    return template('./views/metadata-views/dev-sessions', sessions=sessions)

# Create new dev session and upon 200 return to  /dev-sessions
@route('/new-dev-session', method=['POST'])
def newDevSession():

    developer = request.forms.get('developer')
    sessionName = request.forms.get('sessionName')
    sessionType = request.forms.get('sessionType')
    description = request.forms.get('description')

    db = dbSettings.devSessionsDB # TODO make dynamic for different dev sessions databases
    con = sqlite3.connect(db)
    cursor = con.cursor()

    query = f"INSERT INTO sessions (developer, session_name, session_type, session_description) VALUES ( '{developer}', '{sessionName}', '{sessionType}', '{description}' );"
    cursor.execute(query)
    con.commit()
    con.close()

    redirect('/dev-sessions')


# New Dev Sessions Table
@route('/new-dev-sessions-table', method = ['POST']) # TODO make a param
def setupDevSessionsTable():

    tableName = request.forms.get('tableName')

    db = dbSettings.devSessionsDB # TODO make dynamic for different dev sessions databases
    con = sqlite3.connect(db)

    # TODO query using user params!
    table = f"CREATE TABLE IF NOT EXISTS {tableName} (id INTEGER PRIMARY KEY, developer TEXT, session_name TEXT, session_type TEXT, description);"
    cursor = con.cursor()
    cursor.execute(table)
    con.commit()
    con.close()

# TODO route get-dev-sessions-tables

#     INSERT INTO table_name(column1,column2,...)
# VALUES(value_1,value_2,...),
#       (value_1,value_2,...),
#       (value_1,value_2,...)...

#



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
