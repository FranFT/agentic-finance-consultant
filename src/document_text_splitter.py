from langchain_text_splitters import RecursiveCharacterTextSplitter

class DocumentTextSplitter():
    def __init__(self, _chunk_size: int = 500):
        self.document_text_splitter = RecursiveCharacterTextSplitter(chunk_size=_chunk_size)