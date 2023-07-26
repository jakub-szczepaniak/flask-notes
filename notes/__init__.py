from flask import Flask


def create_app():
    app = Flask(__name__)

    from . import documents

    app.register_blueprint(documents.bp)
    from . import db

    db.init_app(app)

    return app
