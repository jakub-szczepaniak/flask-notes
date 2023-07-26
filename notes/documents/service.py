from dataclasses import dataclass


@dataclass
class Document:
    title: str
    id: int = None


class CreateDocument:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, title=None):
        document = Document(title=title, id=1)
        return self.repository.save(document)


class GetDocumentById:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, id):
        return self.repository.get_by(id)
