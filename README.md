# Text data extractor: PDF to Text


This PDF text data extraction app takes a PDF document as input and return either a txt file that contains all pages or a compressed folder of txt files representing the document pages.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/nainiayoub/pdf-text-data-extractor/main/app.py)

```mermaid
flowchart LR

A[Input: PDF] --> |text conversion| B(Output: Text)
B --> |Option 1| D[One output .txt file]
B --> |Option 2| E[ZIP folder containing .txt file pages]

```

## Application Demo

https://user-images.githubusercontent.com/50157142/169509962-48d34c24-16a3-441f-af93-8702890fcf18.mp4

