from flask import Flask, render_template, g
import os

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
    images = os.listdir(os.path.join(app.static_folder, 'imgs/gallery_images'))
    return render_template('gallery.html', images=images)

@app.route('/info/')
def info():
    return render_template('info.html')

@app.route('/filtering/')
def filtering():
    list_to_filter = [ {"name": "Steph", "age": 33}, {"name": "Alex", "age": 32}, {"name": "Nick", "age": 19}, {"name": "Jess", "age": 16}]
    filtered_list = list(filter(lambda person: person["age"] > 30, list_to_filter))
    return render_template('filtering.html', list=list_to_filter, filtered_list=filtered_list)





