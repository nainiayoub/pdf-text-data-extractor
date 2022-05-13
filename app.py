import streamlit as st
from functions import convert_pdf_to_txt_pages, convert_pdf_to_txt_file, save_pages, displayPDF



st.markdown("""
    ## :outbox_tray: Text data extractor: PDF to Text

    [![Twitter](https://img.shields.io/twitter/url?label=Twitter&style=social&url=https%3A%2F%2Ftwitter.com%2Fnainia_ayoub)](https://www.twitter.com/nainia_ayoub)
    [![Linkedin](https://img.shields.io/twitter/url?label=Linkedin&logo=linkedin&style=social&url=https%3A%2F%2Fwww.linkedin.com%2Fin%2Fayoub-nainia%2F%3Flocale%3Den_US)](https://www.linkedin.com/in/ayoub-nainia/?locale=en_US)
    [![GitHub](https://img.shields.io/twitter/url?label=Github&logo=GitHub&style=social&url=https%3A%2F%2Fgithub.com%2Fnainiayoub)](https://github.com/nainiayoub)

    Before extracting information from a document, we have to extract text data first. 
    Hence, this PDF text data extractor was created.
""")

with st.sidebar:
    st.title("PDF to Text")
    textOutput = st.selectbox(
        "How do you want your output data?",
        ('One text file (.txt)', 'Text file per page (ZIP)'))

pdf_file = st.file_uploader("Load your PDF file", type="pdf")
if pdf_file:
    # display document
    with st.expander("Display document"):
        displayPDF(pdf_file)
    
    # pdf to text
    if textOutput == 'One text file (.txt)':
        text_data_f, nbPages = convert_pdf_to_txt_file(pdf_file)
        totalPages = str(nbPages)+" pages in total."
        st.info(totalPages)
        st.download_button("Download txt file", text_data_f)
    else:
        text_data, nbPages = convert_pdf_to_txt_pages(pdf_file)
        totalPages = str(nbPages)+" pages in total."
        st.info(totalPages)
        zipPath = save_pages(text_data)
        # download text data    
        with open(zipPath, "rb") as fp:
            btn = st.download_button(
                label="Download ZIP (txt)",
                data=fp,
                file_name="pdf_to_txt.zip",
                mime="application/zip"
            )
    
