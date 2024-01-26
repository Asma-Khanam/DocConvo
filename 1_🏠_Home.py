import streamlit as st

# settings
page_title = "DocConvo"
page_icon = "📂"
layout = "centered"
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)

with st.sidebar:
    st.image("images/head.jpeg")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-color: #143d59;
background-size: 180%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# styling
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .shadow-text {
              text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
            }
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# body of page
st.title('📂 Welcome to DocConvo')

box_style = """
    background-color: #677C87;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
"""
st.markdown(
    f"""
    <br>
    <div style="{box_style}">
        <h4 style="shadow-text;">Ask, Discover, and Chat Seamlessly with Your Documents!</h4>
        <p>Create a Streamlit app enabling users to upload PDFs, ask questions in multiple languages, and receive responses from a conversational chain powered by GPT-based language models. Implement language translation, efficient PDF text extraction, and visual word cloud generation for enhanced document exploration. Optimize performance, ensure robust error handling, and deploy the app on a web server for broad accessibility.</p>
    </div>
    <br>
    """,
    unsafe_allow_html=True,
)


st.markdown(
        f"""
        <div style="{box_style}">
        <h4 style='color: #0066cc;'>How it Works!</h4>
        <ul>
            <li>Begin by choosing a specific task or analysis type from the options available in the sidebar.</li>
            <li>You can ask questions about the content of the PDFs, like having a chat with your documents</li>
            <li>The app generates a visual word cloud to give you a quick overview of the main terms in your documents.</li>
            <li>If needed, you can choose to translate your questions to different languages.</li>
            <li>If you upload a CSV file, you can ask questions about the data it contains.</li>
            <li>The app visualizes the CSV data with a bar chart, making it easier to understand the numerical values.</li>
            <li>Overall, the app transforms the way you interact with your documents, making it conversational and personalized.</li>
        </ul>
        </div>
        <br>
        """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <div style="{box_style}">
        <h4 style='color: #0066cc;'>Features</h4>
        <ul>
            <li>User-Friendly Interface</li>
            <li>Customized Results</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True
)

def create_footer():
    footer= """
            background-color:#677C87;
            padding: 20px;
            text-align: center;
            bottom: 0;
            width: 100%;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        """

    button="""
            background-color: #0066cc; 
            color: #fff;
            padding: 5px 5px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        """
    text="""
            font-size:11px
        """

    st.markdown(
        f"""
        <br>
        <br>
        <div style="{footer}">
        <a style="{button}" href="https://github.com/Ayesha-Siddiqua88" target="_blank">GitHub</a>
        <br>
        <br>
        <p style="{text}">2023 Copyright. All Rights Reserved.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

create_footer()