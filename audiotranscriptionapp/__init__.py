import os
from flask import Flask
from flask_bootstrap import Bootstrap


def create_app(test_config=None):
    # create and configure the application
    app = Flask(__name__, instance_path=os.path.join(os.path.abspath(os.curdir), 'instance'), instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    app.config.from_pyfile('config.py')
    app.app_context().push()

    # a simple page to welcome the use on the url /welcome
    @app.route('/welcome')
    def welcome():
        return 'Welcome to this Audio Transcription program!'

    from .upload import uploads
    app.register_blueprint(uploads)

    Bootstrap(app)

    return app
