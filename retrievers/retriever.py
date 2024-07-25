from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

def create_retriever(doc_splits, embedding_model):
    vectorstore = Chroma.from_documents(
        documents=doc_splits,
        collection_name="rag-chroma",
        embedding=OllamaEmbeddings(model=embedding_model),
    )
    retriever = vectorstore.as_retriever()
    return retriever