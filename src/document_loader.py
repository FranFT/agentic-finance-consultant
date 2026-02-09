from langchain_community.document_loaders import PyPDFLoader

class DocumentLoader():
    def __init__(self, file_path):
        self.file_path = file_path
        self.loader = PyPDFLoader(self.file_path)

        if str.endswith(self.file_path, ".pdf"):
            self.docs = self.loader.load()        
