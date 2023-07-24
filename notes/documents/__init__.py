from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint("documents", __name__)


@bp.route("/")
def index():
    return render_template("documents/index.html")
