from flask import Flask, render_template

app = Flask(__name__)

navigation = [{"name" : "home", "path" : "templates/index.html"},{"name" : 'gallery', "path" : "templates/gallery.html"}, { "name" : "info", "path" : "templates/info.html"}]

@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/gallery")
def gallery():
    return render_template('gallery.html')