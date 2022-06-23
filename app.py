from flask import Flask, request, render_template, send_from_directory

from main.main_view import main_blueprint
from loader.loader import loader_blueprint
from loggers import file_logger, page_logger
from functions import *


app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route("/post_uploaded.html", methods=["GET", "POST"])
def page_post_form():
    text = request.values['content']
    picture = request.files.get('picture')
    if not picture:
        file_logger.info('Picture file load error')
        return 'Ошибка загрузки'
    filename = picture.filename
    extension = filename.split('.')[-1]
    if extension.lower() not in ['jpeg', 'jpg', 'png']:
        file_logger.info('File extension error')
        return f"Файлы {extension} не поддерживаются."
    filepath = f"./uploads/{filename}"
    picture.save(filepath)
    add_post('.' + filepath, text)
    return render_template('post_uploaded.html', post_contents=text, picture=filepath)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


@app.route('/search/')
def post_by_tag():
    all_posts = get_json()
    qry = request.args.get('s')
    spec_posts = find_posts(all_posts, qry)
    page_logger.info(f'Search completed for {qry}')
    return render_template('post_list.html', qry=qry, posts=spec_posts)


app.run()
