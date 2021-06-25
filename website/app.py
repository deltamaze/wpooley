from flask import Flask

app = Flask(__name__,
            static_url_path='',
            static_folder='static')


@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/index/')
def rootIndex():
    return app.send_static_file('index.html')
