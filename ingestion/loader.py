from pathlib import Path

from langchain_community.document_loaders import PyMuPDFLoader


def load_documents(directory: str):

    documents = []

    for file_path in Path(directory).glob("*.pdf"):

        loader = PyMuPDFLoader(str(file_path))

        docs = loader.load()

        documents.extend(docs)

    return documents