
# Question Generator

This Flask application generates objective and subjective questions based on user-provided input text.


## Introduction

The Question Generator is a web application built with Flask that automates the process of generating tests from text input. It supports two types of tests: objective tests, which consist of multiple-choice questions, and subjective tests, which involve descriptive questions.

## Features

- Generate objective tests with multiple-choice questions.
- Generate subjective tests with descriptive questions.
- Utilizes NLTK for natural language processing tasks.
- Simple web interface using Flask and WTForms for form handling.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/25-pranav-25/Question-generator.git
   cd Question-generator
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```
   The application will run on `http://localhost:5001` by default.

## Usage

1. Open your web browser and navigate to `http://localhost:5001`.
2. Enter the input text for which you want to generate a test.
3. Select the type of test (objective or subjective) and specify the number of questions.
4. Click on "Generate Test" to see the generated questions.

## How Questions are Generated

### Objective Test Generation

Objective tests are generated using the following steps:
- **Text Analysis:** The input text is analyzed to identify potentially trivial sentences.
- **Sentence Chunking:** NLTK is used to chunk sentences into noun phrases and identify key concepts.
- **Question Formulation:** Questions are formulated by replacing key phrases with blanks and providing answer options based on WordNet synsets.

### Subjective Test Generation

Subjective tests are generated as follows:
- **Pattern Matching:** Specific patterns in the input text are matched to generate questions.
- **Keyword Extraction:** Noun phrases are extracted using NLTK to form questions around key concepts.
- **Question Formulation:** Questions are framed using predefined patterns like "Explain in detail," "Define," etc., followed by extracted keywords.
