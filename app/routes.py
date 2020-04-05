from flask import request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
import os, shutil
from app import app
# from . import classifier


def allowed_file(filename):
    '''
    Checks if a given file `filename` is of type image with 'png', 'jpg', or 'jpeg' extensions
    '''
    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'jfif'])
    return (('.' in filename) and (filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS))


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
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['OUTPUT_DIR'], filename))
            # output = classifier.load_and_predict(filename)
            path_to_image = url_for('static', filename=filename)
            print(path_to_image)
            result = {
                'output': '??',  # output,
                'path_to_image': path_to_image,
                'size': app.config['SIZE']
            }
            return render_template('show.html', result=result)
    
    # clean out static folder
    static_folder = os.listdir(app.config['OUTPUT_DIR'])
    for item in static_folder:
        os.remove(os.path.join(app.config['OUTPUT_DIR'], item))

    return render_template('index.html')
