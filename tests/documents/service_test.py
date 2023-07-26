import pytest

from notes.documents.service import CreateDocument, GetDocumentById
from notes.documents.repository import DocumentRepository
from notes.db import get_db


def test_document_is_created_and_retrieved(app):
    with app.app_context():
        db = get_db()
        repository = DocumentRepository(db)
        create_document = CreateDocument(repository)
        document = create_document.execute(title="Untitled")

        assert document.title == "Untitled"
        assert document.id == 1
        get_document = GetDocumentById(repository)
        document = get_document.execute(document.id)
        assert document.title == "Untitled"
