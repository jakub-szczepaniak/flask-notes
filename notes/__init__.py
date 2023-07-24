from flask import Flask


def create_app():
    app = Flask(__name__)

    from . import documents

    app.register_blueprint(documents.bp)

    return app
