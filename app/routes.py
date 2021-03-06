from flask import request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import os, shutil
from app import app, classifier


def allowed_file(filename):
    '''
    Checks if a given file `filename` is of type image with 'png', 'jpg', or 'jpeg' extensions
    '''
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'jfif'}
    return '.' in filename and  \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        
        # check if no file was submitted to the HTML form
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            img_bytes = file.read()
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['STATIC_DIR'], filename))
            class_name = classifier.get_prediction(image_bytes=img_bytes)
            result = {
                'output': class_name,
                'filename': filename,
                'size': 224
            }
            return render_template('show.html', result=result)

    # clean out static folder when user clicks on "go back"
    static_folder = os.listdir(app.config['STATIC_DIR'])
    for item in static_folder:
        if not item.endswith('.h5'):  # don't delete model .h5 file
            os.remove(os.path.join(app.config['STATIC_DIR'], item))

    return render_template('index.html')
