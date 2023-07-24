from flask import Blueprint, render_template, request, redirect, url_for

bp = Blueprint("documents", __name__)

from . import service
from . import repository


@bp.route("/")
def index():
    store = repository.InMemoryDocumentRepository()
    create_document = service.CreateDocument(store)
    document = create_document.execute(title="Untitled")

    return render_template("documents/index.html", title=document.title)
