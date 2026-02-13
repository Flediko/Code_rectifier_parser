# Code Audit & Refactor Tool 🛠️

A powerful static code analysis and auto-refactoring tool built with Python and Streamlit. This application helps developers identify bugs, security risks, and style violations in **C**, **C++**, and **Python** code.

## 🚀 Features

### 🔍 Static Analysis
- **Lexical Analysis**: Generates token streams.
- **Syntax Analysis**: Validates code structure and detects syntax errors.
- **Semantic Analysis**: Builds symbol tables and checks for scope/logic errors.
- **Safety Checks**: detailed detection of:
    - Infinite loops (`while(1)`, `while True`)
    - Division by zero
    - Unreachable/Dead code
    - Unsanitized inputs (`eval`, `gets`, `strcpy`)

### ✨ Auto-Refactoring
- **Code Formatting**: Fixes indentation and spacing.
- **Cleanup**: Removes dead code and detailed comments.
- **Standardization**:
    - **Python**: Enforces PEP 8 (snake_case naming, removing unused imports, etc.).
    - **C/C++**: Expands single-line statements and fixes standard compliance (e.g., `void main` -> `int main`).

### 📊 Visualization
- Interactive Dashboard with split views.
- **Tabs**: View distinct phases (Tokens, Symbol Table, Errors).
- **Categorized Reporting**: Errors, Warnings, Runtime Risks, and Optimizations.

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

## 🎮 Usage

Run the web application using Streamlit:

```bash
streamlit run app.py
```

The application will open in your default browser at `http://localhost:8501`.

1. **Select Language**: Choose between C, C++, or Python from the sidebar.
2. **Input Code**: Type or paste your code into the editor.
3. **Analyze**: Click `▶️ Start Compilation` to see lexical, syntax, and semantic reports.
4. **Refactor**: Click `✨ Auto-Refactor` to instantly optimize and clean your code.

## 📂 Project Structure

- `app.py`: Main Streamlit application and UI logic.
- `analyzer.py`: Core logic for lexical analysis, parsing, error detection, and refactoring.
- `requirements.txt`: Project dependencies.

## 🛡️ Supported Issues Detected

| Category | Issue Types |
|----------|-------------|
| **Security** | `eval()`, `gets()`, `strcpy()` usage |
| **Logic** | Infinite loops, assignment in conditions (`if(x=5)`), Division by Zero |
| **Style** | Naming conventions (CamelCase vs snake_case), Line length, Missing docstrings |
| **Optimization** | Unused variables, Unused imports, Redundant comparisons (`== True`) |

---
**Note**: This tool is designed for educational purposes (PBL) to demonstrate compiler design concepts and is not a full replacement for production-grade compilers like GCC or Clang.
