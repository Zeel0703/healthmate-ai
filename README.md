# HealthMate AI Agent

An educational, AI-powered health information assistant built with Python and Streamlit. Users can describe symptoms in natural language and receive AI-generated general information about possible causes and basic home-care suggestions.

> **Disclaimer:** HealthMate AI is an educational project, not a diagnostic tool or a substitute for professional medical advice. AI-generated information may be inaccurate or incomplete. Always consult a qualified healthcare professional for medical concerns.

## Project Background

Developed as a capstone project during the **GTU Summer Internship 2025**, organized by CSRBOX in collaboration with IBM SkillsBuild (2 July 2025 – 16 July 2025).

The project explores the use of conversational AI to make general health information easier to access and supports **UN Sustainable Development Goal 3: Good Health and Well-being**.

## Features

- Natural-language symptom input.
- AI-generated general information about possible causes.
- Basic home-care suggestions.
- Responses in English, Hindi, and Gujarati.
- Streamlit interface with light and dark theme support.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Web interface |
| LangChain Core | Message handling and model interaction |
| langchain-google-genai | Google Gemini integration |
| Google Gemini API | AI response generation |
| python-dotenv | Environment variable management |
| pytest | Automated unit testing |

## Project Structure

```text
healthmate-ai/
├── .streamlit/
│   └── config.toml
├── assets/
│   └── logo.png
├── docs/
│   └── architecture.md
├── services/
│   ├── __init__.py
│   └── ai_service.py
├── tests/
│   └── test_response_parser.py
├── utils/
│   ├── __init__.py
│   └── response_parser.py
├── .env.example
├── .gitignore
├── app.py
├── requirements.txt
├── LICENSE
└── README.md
```

See [docs/architecture.md](docs/architecture.md) for the application flow and module responsibilities.

## Getting Started

### Prerequisites

- Python 3.10 or newer.
- pip.
- A Google Gemini API key.

### 1. Clone the Repository

```bash
git clone https://github.com/Zeel0703/healthmate-ai.git
cd healthmate-ai
```

### 2. Create and Activate a Virtual Environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the API Key

Create a `.env` file in the project root using `.env.example` as a reference.

Add your Google Gemini API key and model configuration:

```env
GOOGLE_API_KEY=your_google_api_key
GEMINI_MODEL=gemini-3.5-flash-lite
```

Never commit your `.env` file or expose your API key publicly.

### 5. Run the Application

```bash
streamlit run app.py
```

Streamlit will provide a local URL in the terminal where you can access the application.

## Running Tests

Install pytest if it is not already installed:

```bash
python -m pip install pytest
```

Run the automated tests:

```bash
python -m pytest -v
```

## Current Limitations

- Responses depend on the configured language model and may be inaccurate or incomplete.
- The application provides general health information and cannot diagnose medical conditions.
- The current application does not persist user sessions or symptom history in a database.
- The application requires an active internet connection and a valid Google Gemini API key.

## Future Improvements

- Add stronger response validation and clearer emergency guidance.
- Expand automated tests for API and error-handling scenarios.
- Improve accessibility and interface responsiveness.
- Evaluate trusted, curated health information sources.
- Consider privacy-conscious session management if persistence is introduced.

## License

This project is distributed under the MIT License. See [LICENSE](LICENSE) for details.