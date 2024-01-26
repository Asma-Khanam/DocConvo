import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template
from langchain.llms import HuggingFaceHub
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from googletrans import Translator


st.set_option('deprecation.showPyplotGlobalUse', False)

# New function for language translation
def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

# New function for creating and displaying word cloud
def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig, ax = plt.subplots()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    st.pyplot()

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    # Filter out single letters
    filtered_chunks = [chunk for chunk in chunks if len(chunk) > 1]
    return filtered_chunks


def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore



def get_conversation_chain(vectorstore):
    llm = ChatOpenAI()
    # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})

    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain


def handle_userinput(user_question):
    # Search functionality
    search_query = st.text_input("Search in chat history:")

    if st.session_state.chat_history and search_query:
        st.session_state.chat_history = [
            message for message in st.session_state.chat_history if search_query.lower() in message.content.lower()]

    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)

    # After handling user input, display the filtered chat history
    if st.session_state.chat_history and search_query:
        st.subheader(f"Search Results for '{search_query}':")
        for i, message in enumerate(st.session_state.chat_history):
            st.write(message.content)



def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with DOCs",
                       page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chat with DOCs :books:")
    user_question = st.text_input("Ask a question about your documents:")
    # Language translation option
    translate_to = st.selectbox("Translate to:", ["English", "French", "Spanish", "Turkish","Arabic","Urdu"])
    
    
    if user_question:
        if translate_to.lower() != 'english':
            user_question_translated = translate_text(user_question, target_language=translate_to.lower())
            st.info(f"Translating question to {translate_to}: {user_question_translated}")
            handle_userinput(user_question_translated)
        else:
            handle_userinput(user_question)
    with st.sidebar:
        st.subheader("Your documents")
        pdf_docs = st.file_uploader(
            "Upload your DOCs here and click on 'Process'", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                # get pdf text
                raw_text = get_pdf_text(pdf_docs)

                # get the text chunks
                text_chunks = get_text_chunks(raw_text)

                # create vector store
                vectorstore = get_vectorstore(text_chunks)

                # create conversation chain
                st.session_state.conversation = get_conversation_chain(
                    vectorstore)

                # Generate and display word cloud
                st.subheader("Word Cloud:")
                generate_wordcloud(raw_text)

if __name__ == '__main__':
    main()
