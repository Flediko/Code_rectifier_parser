import streamlit as st
import analyzer
import time

# Page Configuration
st.set_page_config(
    page_title="Code Audit & Refactor Tool",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .stTextArea textarea {
        font-family: 'Courier New', monospace;
        background-color: #1e1e1e;
        color: #ffffff;
    }
    .bug-box {
        padding: 10px;
        background-color: #ffe6e6;
        color: #1a1a1a;
        border-left: 5px solid #ff4b4b;
        margin-bottom: 10px;
        border-radius: 5px;
    }
    .dead-code-box {
        padding: 10px;
        background-color: #e6f3ff;
        color: #1a1a1a;
        border-left: 5px solid #0083b8;
        margin-bottom: 10px;
        border-radius: 5px;
    }
    .success-box {
        padding: 10px;
        background-color: #e6fffa;
        color: #1a1a1a;
        border-left: 5px solid #00cc99;
        margin-bottom: 10px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuration")
    language = st.selectbox("Target Language", ["C", "C++", "Python"])
    
    if language == "C":
        st.info("Mode: C Analysis (Standard)")
    elif language == "C++":
        st.info("Mode: C++ Analysis (Enhanced)")
    elif language == "Python":
        st.info("Mode: Python Analysis (PEP 8)")

    st.markdown("---")
    st.markdown("### 🔍 Compiler Phases")
    st.markdown("1. **Lexical Analysis**: Tokenization")
    st.markdown("2. **Syntax Analysis**: Parsing/Structure")
    st.markdown("3. **Semantic Analysis**: Symbol Table/Scope")
    st.markdown("4. **Optimization**: Refactoring/Linting")
    
    st.markdown("---")
    st.markdown("### 📖 How to use")
    st.info(
        f"1. Enter {language} code.\n"
        "2. Click **Start Compilation** to run all phases.\n"
        "3. distinct tabs will show tokens, symbol table, and errors."
    )

# --- MAIN CONTENT ---
st.title("🛠️ Static Code Analyzer")
st.markdown(f"**Compiler Design Project**: Lexical, Syntax, & Semantic Analysis for {language}")

# Default Code Snippets
default_code_c = """#include <stdio.h>

void main() {
    int x;
    int y = 5;
    
    printf("Result: %d"); 
    
    return;
    
    x = 10; // This will never run
    printf("Unreachable");
}
"""

default_code_cpp = """#include <iostream>

int main() {
    int* ptr = new int(10); // Raw pointer
    
    std::cout << "Value: " << *ptr << std::endl;
    
    return 0;
}
"""

default_code_py = """import os, sys # Multiple imports

def ProcessData(data): # Bad naming (CamelCase)
    global x # Global usage
    x = 10
    
    # This is a very long line that exceeds the standard seventy-nine character limit recommended by PEP 8 guidelines for Python code style
    
    try:
        if data == True: 
            val = eval(data) 
    except: 
        print("Error") 

    return 5 / 0 
"""

# Select default code based on language
if language == "C":
    code_value = default_code_c
elif language == "C++":
    code_value = default_code_cpp
else:
    code_value = default_code_py

code_input = st.text_area("Source Editor", value=code_value, height=350)

col1, col2, col3, col4 = st.columns(4)

with col1:
    compile_btn = st.button("▶️ Start Compilation", width="stretch")
with col2:
    refactor_btn = st.button("✨ Auto-Refactor", width="stretch")
with col3:
    remove_comments_btn = st.button("🗑️ Remove Comments", width="stretch")
    
# LOGIC
if compile_btn:
    with st.spinner("Running Compiler Phases..."):
        time.sleep(1) # Simulation
        
        # Phase 1: Lexical
        tokens = analyzer.lexical_analysis(code_input, language)
        
        # Phase 2 & 3: Syntax/Semantic (Issues + Symbol Table)
        if language == "C":
            issues = analyzer.analyze_code(code_input)
            symbol_table = analyzer.semantic_analysis_symbol_table(code_input, language)
        elif language == "C++":
            issues = analyzer.analyze_code_cpp(code_input)
            symbol_table = analyzer.semantic_analysis_symbol_table(code_input, language)
        else: # Python
            issues = analyzer.analyze_code_python(code_input)
            symbol_table = analyzer.semantic_analysis_symbol_table(code_input, language)
        
        # TABS for phases
        tab1, tab2, tab3, tab4 = st.tabs(["📝 Lexical Analysis", "🏗️ Syntax/Semantic", "📊 Symbol Table", "❌ Errors/Warnings"])
        
        with tab1:
            st.subheader("Token Stream (Lexer)")
            st.dataframe(tokens, width="stretch")
            
        with tab2:
            st.subheader("Structure Validation")
            if not any(i['type'] == 'Syntax Error' for i in issues):
                st.success("✅ Syntax Valid (No Structural Errors)")
            else:
                st.error("❌ Syntax Errors Detected")
                
        with tab3:
            st.subheader("Symbol Table (Semantic)")
            st.dataframe(symbol_table, width="stretch")
            
        with tab4:
            st.subheader("Analysis Report")
            if issues:
                # Categorize for display
                synt_err = [i for i in issues if i['type'] == 'Syntax Error']
                sem_err = [i for i in issues if i['type'] == 'Semantic Error' or i['type'] == 'Dead Code' or i['type'] == 'Logic Error']
                run_risk = [i for i in issues if i['type'] == 'Runtime Risk' or i['type'] == 'Infinite Loop' or i['type'] == 'Math Error']
                lints = [i for i in issues if 'Lint' in i['type'] or 'Suggestion' in i['type'] or 'Style' in i['type']]
                
                if synt_err:
                    st.error(f"Syntax Errors ({len(synt_err)})")
                    for i in synt_err: st.write(f"- Line {i['line']}: {i['message']}")
                    
                if sem_err:
                    st.warning(f"Semantic/Logic Errors ({len(sem_err)})")
                    for i in sem_err: st.write(f"- Line {i['line']}: {i['message']}")
                    
                if run_risk:
                    st.warning(f"Runtime Risks ({len(run_risk)})")
                    for i in run_risk: st.write(f"- Line {i['line']}: {i['message']}")
                    
                if lints:
                    st.info(f"Lint Warnings / Optimization ({len(lints)})")
                    for i in lints: st.write(f"- Line {i['line']}: {i['message']}")
            else:
                st.success("No issues detected!")

if refactor_btn:
     st.subheader("Optimized Code (Refactoring)")
     if language == "C" or language == "C++":
         # Use the generic C refactor for both
         refactored = analyzer.refactor_code(code_input)
         st.code(refactored, language='c')
     else:
         refactored = analyzer.refactor_code_python(code_input)
         st.code(refactored, language='python')
     st.success("Code Refactored & Optimized!")
     
if remove_comments_btn:
    cleaned = analyzer.remove_comments(code_input)
    st.subheader("Code (Comments Removed)")
    st.code(cleaned, language='python' if language == 'Python' else 'c')
