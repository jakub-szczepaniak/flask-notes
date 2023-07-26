from notes.documents.service import Document


class DocumentRepository:
    def __init__(self, db=None):
        self.db = db

    def save(self, document):
        self.db.execute("INSERT INTO documents (title) VALUES (?)", (document.title,))
        document.id = 1
        return document

    def get_by(self, id):
        row = self.db.execute("SELECT * FROM documents WHERE id = ?", (id,)).fetchone()
        return Document(title=row["title"], id=row["id"])
