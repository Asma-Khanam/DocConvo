
![White Minimalist Simple Aesthetic Name Twitter Header](https://github.com/Asma-Khanam/DocConvo/assets/128472305/d95a2fb5-4d5d-4057-8736-9301342e598a)

# DocConvo

This project consists of two Streamlit applications for document-related queries and for visualizing data in Excel files. The applications are designed to provide a seamless experience for users interested in interacting with their documents and visualizing  data.


# Features

## Document Chat
- Language Translation: Users can translate their queries to various languages before interacting with the document chat system.
- PDF Processing: Users can upload PDF documents, and the system extracts text for further analysis.
- Conversational AI: Utilizes a Conversational Retrieval Chain for handling user queries and generating responses based on document content.
- Word Cloud Visualization: Generates and displays a word cloud based on the processed document text.

## Excel Plotter
- Excel File Upload: Users can upload Excel files (.xlsx or .csv) for data analysis and visualization.
- Column Selection: Allows users to select specific columns for analysis.
- Grouping and Plotting: Group and visualize data based on selected columns, with support for bar plots.
- Download Options: Provides download links for the processed Excel file and generated plots.

## Getting Started

Install required dependencies:

```bash
  pip install -r requirements.txt
  pip install -r requirements2.txt

```

## Run the Streamlit applications:

For running application:
```bash
streamlit run 1_🏠_Home.py
```
## Dependencies

- [Streamlit](https://streamlit.io)

- [PyPDF2](https://pypi.org/project/PyPDF2/)

- [LangChain](https://www.langchain.com)

- [WordCloud]()

- [Matplotlib](https://matplotlib.org)

- [Googletrans]()

- [Pandas]()

- [Plotly Express](https://plotly.com/python/plotly-express/)


