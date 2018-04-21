from bottle import Bottle, static_file, run
from DBConnection import DBConnection

app = Bottle()
database = DBConnection()

@app.get("<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="")

@app.get('/')
def index():
    return static_file("index.html", root="")

if __name__ == '__main__':
    run(app, host="localhost", port=8080)

