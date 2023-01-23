# PDF to Text
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/nainiayoub/pdf-text-data-extractor/main/app.py)
![visitor badge](https://visitor-badge.glitch.me/badge?page_id=nainiayoub.pdf-text-data-extractor)
![forks badge](https://img.shields.io/github/forks/nainiayoub/pdf-text-data-extractor)
![starts badge](https://img.shields.io/github/stars/nainiayoub/pdf-text-data-extractor?style=social)

PDF text data extraction app that takes a PDF document as input and returns either a txt file that contains all pages or a compressed folder of txt files representing the document pages. OCR can also be enabled for scanned docoments.


![pdf_text_image](https://user-images.githubusercontent.com/50157142/214037439-448fafb8-5363-46cb-849e-6132f9bc0fb2.PNG)




## How does it worK?

```mermaid
flowchart LR

A[PDF] --> |text conversion / OCR| B(Text)
B --> |Option 1| D[txt file]
B --> |Option 2| E[ZIP folder of txt files for pages]

```
1. Upload your PDF.
2. Enable OCR (for scanned documents).
3. Select the PDF language.
4. Download your output file (zip/txt).

## How to support the project
You can help support the project through feedback and/or [buy me coffee](https://www.buymeacoffee.com/nainiayoub).

