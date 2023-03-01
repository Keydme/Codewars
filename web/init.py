import os
import time
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/Share/uploads'
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','epub'}

app = Flask(
    __name__,
    template_folder='.',
    static_folder='.',
    static_url_path='',
)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
'''
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

'''

messages = []

temp=''
with open('./dynamic/talk.log') as file:
    temp = file.read()

with open('./dynamic/talk.log', 'w') as file:
    file.write(temp+'\n')
    file.write('-------vvv'+str(time.asctime(time.localtime(time.time()))).replace(' ','-')+'vvv-------')

del temp

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and file.filename:
            filename = file.filename  #secure_filename(file.filename)#解除安全文件名限制
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index', name=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@app.route('/talk', methods=['GET', 'POST'])
def talk():
    global messages
    if request.method == 'POST':
        
        temp=''
        with open('./dynamic/talk.log') as file:
            temp = file.read()
            
        with open('./dynamic/talk.log','w') as file:
            file.write(temp+'\n')
            file.write(request.headers.get('User-Agent')+'\n')
            file.write(request.form['text'])
        print(request.headers.get('User-Agent'))
        messages.append(request.form['text'])
    return render_template('/templates/talk.html', messages=messages)


@app.route('/download')
def look():
    entries = os.listdir('./uploads')
    return render_template('/templates/download.html', entries=entries)


@app.route('/uploads/<filename>')
def files(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == '__main__':
    app.run('0.0.0.0')
