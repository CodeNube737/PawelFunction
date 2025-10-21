# Copilot Exam Study Guide Workflow

This file documents the step-by-step workflow for reviewing lecture material and building a study guide with Copilot assistance. Use this workflow for efficient, collaborative exam preparation.

## Step-by-Step Workflow

1. **Verify Poppler Installation (at the beginning):** Confirm with the user that Poppler is installed before starting any PDF extraction. Provide installation instructions if needed.
2. **Extract Content:** Use Poppler tools (`pdftotext`, `pdftoppm`) to extract text and images from the lecture PDF, 10 pages at a time.
3. **Confirm Readiness:** Before each major step, ask the user to confirm they are ready to proceed.
4. **Review & Summarize:** For each set of pages, summarize key concepts and technical details, focusing on clarity and relevance.
5. **Comprehension Q&A:** I (AI) generate comprehension questions for each page or topic, and you (User) provide answers to reinforce understanding.
6. **Update Markdown:** Append summaries, Q&A, tables, diagrams, and user notes to `study_guide.md`, always preserving existing content.
7. **Clarify Technical Details:** Distinguish between similar technical concepts (e.g., cable categories, IEEE standards) and update tables/explanations as needed.
8. **Convert Markdown to Word Document (if requested):** Guide the user to convert the markdown study guide to a Word document using Pandoc.
9. **User Collaboration:** Incorporate your answers, manual edits, and screenshot content as requested, following specific formatting and focus instructions.
10. **Iterative Process:** Repeat extraction, review, and update steps for each new set of pages, ensuring the study guide remains comprehensive and well-organized.

---

**Reference this README for a reliable, stepwise approach to exam study guide creation with Copilot.**
