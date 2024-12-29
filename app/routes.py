from flask import Flask, render_template, request, redirect, url_for
import os
from spleeter.separator import Separator

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'app/static/uploads'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            separator = Separator('spleeter:2stems')
            separator.separate_to_file(filepath, app.config['UPLOAD_FOLDER'])
            return redirect(url_for('index'))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
