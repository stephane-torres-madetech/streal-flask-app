from flask import Flask, render_template, g

app = Flask(__name__)

""" @app.context_processor
def inject_navigation():
    return dict(navigation = g.navigation)


navigation = [{"name" : "home", "path" : 'hello'},
              {"name" : 'gallery', "path" : 'gallery'},
              { "name" : "info", "path" : "./templates/info.html"}] """


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/gallery/")
def gallery():
    return render_template('gallery.html')





