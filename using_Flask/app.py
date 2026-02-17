from flask import Flask, render_template, request, jsonify
import analyzer
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    code = data.get('code', '')
    language = data.get('language', 'Python')
    
    # Phase 1: Lexical
    tokens = analyzer.lexical_analysis(code, language)
    
    # Phase 2 & 3: Syntax/Semantic
    if language == "C":
        issues = analyzer.analyze_code(code)
        symbol_table = analyzer.semantic_analysis_symbol_table(code, language)
    elif language == "C++":
        issues = analyzer.analyze_code_cpp(code)
        symbol_table = analyzer.semantic_analysis_symbol_table(code, language)
    else: # Python
        issues = analyzer.analyze_code_python(code)
        symbol_table = analyzer.semantic_analysis_symbol_table(code, language)
        
    return jsonify({
        'tokens': tokens,
        'issues': issues,
        'symbol_table': symbol_table
    })

@app.route('/refactor', methods=['POST'])
def refactor():
    data = request.json
    code = data.get('code', '')
    language = data.get('language', 'Python')
    
    if language == "C" or language == "C++":
        refactored = analyzer.refactor_code(code)
    else:
        refactored = analyzer.refactor_code_python(code)
        
    return jsonify({'refactored_code': refactored})

@app.route('/remove_comments', methods=['POST'])
def remove_comments():
    data = request.json
    code = data.get('code', '')
    
    cleaned = analyzer.remove_comments(code)
    return jsonify({'cleaned_code': cleaned})

if __name__ == '__main__':
    app.run(debug=True)
