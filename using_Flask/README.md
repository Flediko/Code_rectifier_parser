# Static Code Analyzer - Web Version

This is the Flask-based web implementation of the Static Code Analyzer, providing a lightweight and responsive interface for analyzing and refactoring code.

## 📋 Features

- **Multi-language Support**: Analyze C, C++, and Python code.
- **Lexical Analysis**: Break down code into tokens.
- **Syntax & Semantic Analysis**: Detect structural errors and logic issues.
- **Symbol Table**: Visualize variable scopes and types.
- **Code Refactoring**: Auto-optimize code structure.
- **Comment Cleaner**: Strip comments while preserving strings.

## 🚀 Getting Started

### Prerequisites

Ensure you have Python installed. You also need the `flask` library.

### Installation

1. Navigate to the `web_version` directory:
   ```bash
   cd web_version
   ```

2. Install the required dependencies:
   ```bash
   pip install flask
   ```
   *(Or simply `pip install -r requirements.txt` if you have created one)*

## 🏃‍♂️ Running the Application

To start the Flask server, run the following command from inside the `web_version` directory:

```bash
python app.py
```

After the server starts, open your web browser and navigate to:

```
http://127.0.0.1:5000
```

## 📂 Project Structure

- `app.py`: The main Flask application entry point.
- `analyzer.py`: Core logic for code analysis and refactoring.
- `templates/`: HTML templates for the frontend.
- `static/`: CSS and JavaScript files.

## 🛠️ Usage

1. **Select Language**: Choose C, C++, or Python from the dropdown.
2. **Enter Code**: Paste your source code into the editor.
3. **Analyze**: Click "Analyze Code" to see token streams, symbol tables, and error reports.
4. **Refactor/Clean**: Use the provided buttons to refactor code or remove comments. The output will appear below.
