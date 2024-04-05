from flask import Flask, render_template

app = Flask(__name__)





@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/gallery")
def gallery():
    return render_template('gallery.html')

navigation = [{"name" : "home", "path" : hello()},{"name" : 'gallery', "path" : gallery()}, { "name" : "info", "path" : "templates/info.html"}]

@app.context_processor
def inject_navigation():
    return dict(navigation = navigation)