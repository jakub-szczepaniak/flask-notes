class InMemoryDocumentRepository:
    def __init__(self):
        self.documents = {}

    def save(self, document):
        self.documents[document.id] = document
        return document

    def get(self, id):
        return self.documents[id]
