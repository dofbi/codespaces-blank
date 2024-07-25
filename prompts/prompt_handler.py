from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

def before_rag(model, topic):
    before_rag_template = "What is {topic}"
    before_rag_prompt = ChatPromptTemplate.from_template(before_rag_template)
    before_rag_chain = before_rag_prompt | model | StrOutputParser()
    return before_rag_chain.invoke({"topic": topic})

def after_rag(retriever, model, question):
    after_rag_template = """Answer the question based only on the following context:
    {context}
    Question: {question}
    """
    after_rag_prompt = ChatPromptTemplate.from_template(after_rag_template)
    after_rag_chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | after_rag_prompt
        | model
        | StrOutputParser()
    )
    return after_rag_chain.invoke(question)
