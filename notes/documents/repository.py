from notes.documents.service import Document


class DocumentRepository:
    def __init__(self, db=None):
        self.db = db

    def save(self, document):
        self.db.execute("INSERT INTO documents (title) VALUES (?)", (document.title,))
        document.id = 1
        print("Saved document")
        return document

    def get_by(self, id):
        print(f"{id} for the documents")
        row = self.db.execute("SELECT * FROM documents WHERE id = ?", (id,)).fetchone()
        print(f"{row} value")
        return Document(title=row["title"], id=row["id"])
