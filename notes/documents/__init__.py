from flask import Blueprint, render_template, request, redirect, url_for


from . import service
from . import repository
from notes.db import get_db

bp = Blueprint("documents", __name__, url_prefix="/documents")


@bp.route("/")
def index():
    db = get_db()
    store = repository.DocumentRepository(db)
    create_document = service.CreateDocument(store)
    document = create_document.execute(title="Untitled")

    return render_template("documents/index.html", title=document.title)


@bp.route("/create", methods=["POST"])
def create():
    db = get_db()
    store = repository.DocumentRepository(db)
    create_document = service.CreateDocument(store)
    document = create_document.execute(title=request.form["title"])

    return redirect(url_for("documents.show", id=document.id))


@bp.route("/<int:id>", methods=["GET"])
def show(id):
    db = get_db()
    store = repository.DocumentRepository(db)
    get_by_id = service.GetDocumentById(store)
    document = get_by_id.execute(id)
    return render_template("documents/index", title=document.title)
