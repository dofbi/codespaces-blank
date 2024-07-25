from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community import embeddings

def create_embeddings(docs_list, chunk_size, chunk_overlap, embedding_model):
    text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    doc_splits = text_splitter.split_documents(docs_list)
    return doc_splits
