from bottle import Bottle, static_file, run
from DBConnection import DBConnection

app = Bottle()
database = DBConnection()

@app.get('/')
def index():
    return static_file("index.html", root= "beanweb/public/")

if __name__ == '__main__':
    run(app, host="localhost", port=8080)

