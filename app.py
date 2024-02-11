import os

import psycopg2
from uuid import uuid4
from openpyxl import Workbook
from flask import Flask, request, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

from misc import *

app = Flask(__name__)

db = ''
UPLOAD_FOLDER = 'D:/'
ALLOWED_EXTENSIONS = {'xls', 'xlsx'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:postgres@5.145.160.142:5432'
app.config['SECRET_KEY'] = 'amogus'

wb = Workbook()
wb = wb.active

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/add_menu', methods=['GET', 'POST'])
def add_menu():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Не могу прочитать файл')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('Нет выбранного файла')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_origin = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_origin)
            add_food(file_origin)
    return '''
            <!doctype html>
            <title>Загрузить новый файл</title>
            <h1>Загрузить новый файл</h1>
            <form method=post enctype=multipart/form-data>
              <input type=file name=file>
              <input type=submit value=Upload>
            </form>
            </html>
            '''

def main():
    app.run(port=8080, host='0.0.0.0')


if __name__ == '__main__':
    main()