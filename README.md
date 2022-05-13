# Text data extractor: PDF to Text
This PDF text data extraction app takes a PDF document as input and return either a txt file that contains all pages or a compressed folder of txt files representing the document pages.

```mermaid
flowchart LR

A[Input: PDF] --> |text conversion| B(Output: Text)
B --> |Option 1| D[One output .txt file]
B --> |Option 2| E[ZIP folder containing .txt file pages]

```

