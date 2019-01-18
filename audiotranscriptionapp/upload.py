import simplejson as json
import os

from flask import (
    Blueprint, flash, redirect, render_template, request
)
from flask import current_app as app
from watson_developer_cloud import SpeechToTextV1
from werkzeug import secure_filename

uploads = Blueprint('uploads_bp', __name__)

transcription_text = []

ALLOWED_EXTENSIONS = set(['mp3'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# with app.app_context():
speech_to_text = SpeechToTextV1(
    iam_apikey=app.config['WATSON_API_KEY'],
    url=app.config['WATSON_API_URL']
)


@uploads.route('/', methods=('GET', 'POST'))
def upload_file():
    if request.method == 'POST':
        error = None
        if 'file' not in request.files:
            print('No file attached in request')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print('No file selected')
            return redirect(request.url)
        if not allowed_file(file.filename):
            error = 'Invalid format selected. Please ensure to select a .mp3 file'
            # return redirect(request.url)
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
            obtain_json_from_file(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
            # return 'file uploaded successfully'
            print(transcription_text)
            return render_template('upload/upload.html', text_result=transcription_text)

        flash(error)

    return render_template('upload/upload.html', text_result='')


def obtain_json_from_file(file_name):
    audio_file = open(file_name, 'rb')

    with open('transcript_result.json', 'w') as fp:
        text = speech_to_text.recognize(audio_file, content_type="audio/mp3", continuous=True, timestamps=False,
                                        max_alternatives=1, model='en-US_NarrowbandModel')
        json.dump(text.get_result(), fp, indent=2)

    load_and_read_json()


def load_and_read_json():
    global transcription_text
    transcript_text = []
    with open('transcript_result.json', 'r') as fp:
        # load_and_read_json(fp)
        print("Executing json load")
        json_dict = json.load(fp)

        print("this is some json  ")

        for transcript in range(len(json_dict['results'])):
            arr = json_dict['results'][transcript]
            transcript_arr = arr['alternatives']
            transcript_text.append(transcript_arr[0]['transcript'])

        transcription_text = transcript_text
    return transcription_text
