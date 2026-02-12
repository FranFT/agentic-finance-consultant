import os
import pprint
from langchain_community.document_loaders import PyPDFLoader

class DocumentLoader():
    def __init__(self, file_path):
        self.file_path = file_path
        self.loader = PyPDFLoader(self.file_path)

        if os.path.exists(file_path):
            if str.endswith(self.file_path, ".pdf"):
                self.doc = self.loader.load()
            else:
                raise IOError("File extension not supported.")
        else:
            raise IOError("File doesn't exists.")

    def get_document_text(self):
        """
        Returns all pages from the document 
        """
        output = "\n".join([document.page_content for document in self.doc]) if len(self.doc) > 0 else ""
        return output
    
    def get_document_metadata(self):
        """
        Returns document metadata
        """
        output = self.doc[0].metadata if len(self.doc) > 0 else ""
        return output