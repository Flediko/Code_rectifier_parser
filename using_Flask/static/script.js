document.addEventListener('DOMContentLoaded', () => {
    const codeEditor = document.getElementById('code-editor');
    const langSelect = document.getElementById('language-select');
    const langInfo = document.getElementById('lang-info');
    
    // Buttons
    const analyzeBtn = document.getElementById('analyze-btn');
    const refactorBtn = document.getElementById('refactor-btn');
    const cleanBtn = document.getElementById('clean-btn');
    
    // Outputs
    const tokensTable = document.getElementById('tokens-table').querySelector('tbody');
    const symbolTable = document.getElementById('symbol-table').querySelector('tbody');
    const issuesList = document.getElementById('issues-list');
    const syntaxStatus = document.getElementById('syntax-status');
    
    // Modal
    const modal = document.getElementById('code-modal');
    const modalContent = document.getElementById('refactored-output');
    const closeModal = document.querySelector('.close-modal');
    const copyBtn = document.getElementById('copy-btn');

    // Default Code Snippets
    const defaultCode = {
        'C': `#include <stdio.h>\n\nvoid main() {\n    int x;\n    int y = 5;\n    printf("Result: %d"); \n    return;\n    x = 10; // Dead code\n}`,
        'C++': `#include <iostream>\n\nint main() {\n    int* ptr = new int(10); // Raw pointer\n    std::cout << "Value: " << *ptr << std::endl;\n    return 0;\n}`,
        'Python': `import os, sys\n\ndef ProcessData(data):\n    global x\n    x = 10\n    if data == True: val = eval(data)\n    return 5 / 0`
    };

    // Initialize
    codeEditor.value = defaultCode['Python'];

    // Specific Events
    langSelect.addEventListener('change', () => {
        const lang = langSelect.value;
        codeEditor.value = defaultCode[lang];
        if (lang === 'C') langInfo.innerText = "Mode: C Analysis (Standard)";
        else if (lang === 'C++') langInfo.innerText = "Mode: C++ Analysis (Enhanced)";
        else langInfo.innerText = "Mode: Python Analysis (PEP 8)";
    });

    // Tab Switching
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.addEventListener('click', () => {
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
            btn.classList.add('active');
            document.getElementById(btn.dataset.tab).classList.add('active');
        });
    });

    // Analyze Action
    analyzeBtn.addEventListener('click', async () => {
        analyzeBtn.innerText = "⏳ Compiling...";
        try {
            const response = await fetch('/analyze', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    code: codeEditor.value,
                    language: langSelect.value
                })
            });
            const data = await response.json();
            renderResults(data);
        } catch (e) {
            console.error(e);
            alert("Analysis failed!");
        } finally {
            analyzeBtn.innerText = "▶️ Start Compilation";
        }
    });

    // Refactor Action
    refactorBtn.addEventListener('click', async () => {
        refactorBtn.innerText = "⏳ Processing...";
        try {
            const response = await fetch('/refactor', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    code: codeEditor.value,
                    language: langSelect.value
                })
            });
            const data = await response.json();
            showModal(data.refactored_code);
        } catch (e) {
            alert("Refactoring failed!");
        } finally {
            refactorBtn.innerText = "✨ Auto-Refactor";
        }
    });

    // Clean Comments Action
    cleanBtn.addEventListener('click', async () => {
        const response = await fetch('/remove_comments', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ code: codeEditor.value })
        });
        const data = await response.json();
        showModal(data.cleaned_code);
    });

    // Rendering Logic
    function renderResults(data) {
        // 1. Tokens
        tokensTable.innerHTML = '';
        data.tokens.forEach(t => {
            const row = `<tr><td>${t.type}</td><td>${t.value}</td><td>${t.line}</td></tr>`;
            tokensTable.innerHTML += row;
        });

        // 2. Syntax Status
        const syntaxErrors = data.issues.filter(i => i.type === 'Syntax Error');
        if (syntaxErrors.length === 0) {
            syntaxStatus.className = 'status-box success';
            syntaxStatus.innerText = '✅ Syntax Valid (No Structural Errors)';
        } else {
            syntaxStatus.className = 'status-box error';
            syntaxStatus.innerText = '❌ Syntax Errors Detected';
        }

        // 3. Symbol Table
        symbolTable.innerHTML = '';
        data.symbol_table.forEach(s => {
            const row = `<tr><td>${s.name}</td><td>${s.type}</td><td>${s.scope}</td><td>${s.line}</td></tr>`;
            symbolTable.innerHTML += row;
        });

        // 4. Issues
        issuesList.innerHTML = '';
        if (data.issues.length === 0) {
            issuesList.innerHTML = '<div class="issue-card info">No issues detected!</div>';
        } else {
            data.issues.forEach(i => {
                let typeClass = 'info';
                if (i.type.includes('Error') || i.type === 'Bug') typeClass = 'error';
                else if (i.type.includes('Warning') || i.type.includes('Risk')) typeClass = 'warning';
                
                const card = `<div class="issue-card ${typeClass}">
                    <strong>[Line ${i.line}] ${i.type}:</strong> ${i.message}
                </div>`;
                issuesList.innerHTML += card;
            });
        }
        
        // Switch to Lexical tab to show something happened
        document.querySelector('[data-tab="lexical"]').click();
    }

    // Modal Logic
    function showModal(code) {
        modalContent.value = code;
        modal.style.display = "block";
    }

    closeModal.onclick = () => modal.style.display = "none";
    window.onclick = (e) => {
        if (e.target == modal) modal.style.display = "none";
    }
    
    copyBtn.onclick = () => {
        modalContent.select();
        document.execCommand("copy");
        copyBtn.innerText = "Copied!";
        setTimeout(() => copyBtn.innerText = "Copy to Clipboard", 2000);
    }
});
