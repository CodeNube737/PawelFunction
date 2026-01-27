# Copilot PDF-to-Markdown Documentation Workflow

This workflow outlines the steps taken to convert a PDF document into a fully accessible, image-referenced Markdown file using GitHub Copilot in VS Code.

---

## 1. Preparation
- Confirm the working environment is VS Code and the target folder is set.
- Ensure the PDF file is present in the workspace.
- Confirm Poppler is installed for PDF text and image extraction.

## 2. Extraction
- Use Poppler tools (`pdftotext` and `pdftoppm`) to extract:
  - Full text from the PDF into a `.txt` file.
  - Each page as a high-resolution PNG image.
- Store all outputs in a dedicated `pdf_outputs/<PDF_BASENAME>/` folder.

## 3. Verification
- Check that the `.txt` file contains the full text of the PDF.
- Ensure all page images are present and readable.

## 4. Markdown Conversion
- Create a summary Markdown file with:
  - Section headings and key points.
  - References to each extracted page image for visual context.
- On request, generate a full-text Markdown file:
  - Copy the entire extracted text, formatting it with Markdown headings, lists, and tables.
  - Insert image references for each page at the appropriate locations.

## 5. Completion
- Confirm the Markdown file(s) match the original PDF in content and structure.
- Provide navigation or further formatting as needed.

---

## Deliverables
- `pdf_outputs/<PDF_BASENAME>/` with all text and images.
- `<PDF_BASENAME>_extracted.md`: Summary with image references.
- `<PDF_BASENAME>_full.md`: Full manual in Markdown, with all details and images.
- `Copilot_docs_workflow.md`: This workflow documentation.

---

*This workflow ensures a repeatable, accessible, and visually rich conversion of PDF manuals for study, reference, or further processing.*
