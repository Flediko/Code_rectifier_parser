# Static Code Analyzer & Refactoring Tool

A powerful static code analysis and auto-refactoring tool supporting **C**, **C++**, and **Python**. This project offers two web-based implementations: a **Streamlit** dashboard for quick interactive analysis and a **Flask** web application for a lightweight, traditional web experience.

## 🚀 Features

### 🔍 Static Analysis
- **Lexical Analysis**: Break down code into token streams.
- **Syntax Analysis**: Validate structure and detect syntax errors.
- **Semantic Analysis**: Build symbol tables and check variable scopes/types.
- **Safety Checks**: Detect infinite loops (`while(1)`), division by zero, and unreachable code.
- **Security Audits**: Identify unsanitized inputs (`eval`, `gets`, `strcpy`).

### ✨ Auto-Refactoring
- **Code Formatting**: Fix indentation and spacing.
- **Cleanup**: Remove dead code and comments.
- **Standardization**: Enforce PEP 8 (Python) and standard compliance (C/C++).

## 📂 Project Structure

The project is divided into two main versions:
- **`stream_lit/`**: The Streamlit-based interactive dashboard.
- **`web_version/`**: The Flask-based web application.

## 📦 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. Install the required libraries for both versions:
   ```bash
   pip install streamlit flask
   ```

## 🎮 How to Run

### Option 1: Streamlit Version (Interactive Dashboard)
Navigate to the `stream_lit` directory and run:

```bash
cd stream_lit
streamlit run app.py
```
*Access at: `http://localhost:8501`*

### Option 2: Flask Version (Lightweight Web App)
Navigate to the `web_version` directory and run:

```bash
cd web_version
python app.py
```
*Access at: `http://127.0.0.1:5000`*

## 🛡️ Supported Analysis

| Category | Detects |
|----------|---------|
| **Security** | `eval()`, `gets()`, `strcpy()` usage |
| **Logic** | Infinite loops, Assignment in conditional (`if(x=5)`), Division by Zero |
| **Style** | Naming conventions, Line length, Missing docstrings |
| **Optimization** | Unused variables, Unused imports, Redundant comparisons |

---
*This tool is designed for educational purposes to demonstrate compiler design concepts.*
