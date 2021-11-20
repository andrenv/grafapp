from flask import Flask, render_template, request, Response
from models.trips import DataModel
import pandas as pd
import os


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:example@0.0.0.0:3306/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SWAGGER_UI_JSONEDITOR'] = True
app.config['UPLOAD_FOLDER'] = r'/home/ubuntu/graf/files'

app.secret_key = '123'



@app.route('/upload')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods = ['GET', 'POST'])
def uploader_file():
    if request.method == 'POST':
        f = request.files['file']

        f.save(os.path.join(app.config['UPLOAD_FOLDER'], 'data.csv'))
        return render_template('progress.html', resp=200)


@app.route('/progress')
def progress():

    chunks = 5
    ts = sum(1 for row in open(os.path.join(app.config['UPLOAD_FOLDER'], 'data.csv'), 'r'))
    incremental = 100/int(ts/chunks)

    def generate():
        x = 0
        for c in pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'], 'data.csv'), chunksize=chunks):
            c['datetime'] = pd.to_datetime(c['datetime'], format='%Y-%m-%d %H:%M:%S')

            with app.app_context():
                [DataModel(**i).save_to_db() for i in c.to_dict('records')]
                db.session.commit()

            x = x+incremental
            yield "data:" + str(x) + "\n\n"

    return Response(generate(), mimetype='text/event-stream')


if __name__ == '__main__':
    from db import db

    db.init_app(app)

    app.run(port=8050, debug=True, host='0.0.0.0')
