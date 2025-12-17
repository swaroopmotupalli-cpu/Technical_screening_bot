async function runCode() {
    const language = document.getElementById("language").value;
    const code = document.getElementById("code").value.trim();
    const problem_id = document.getElementById("problem_id").value;
    const resultsDiv = document.getElementById("results");
    const heading = document.getElementById("resultHeading");

    resultsDiv.innerHTML = "";
    heading.classList.remove("hidden");
    heading.classList.add("highlight");

    if (!language) {
        resultsDiv.innerHTML = `<div class="error">⚠ Please select a language</div>`;
        return;
    }

    if (!code) {
        resultsDiv.innerHTML = `<div class="error">⚠ Please write your code</div>`;
        return;
    }

    // Language mismatch detection
    function languageMismatch(lang, codeText) {
        const hints = {
            c: /#include\s*<|int\s+main\s*\(/i,
            java: /class\s+\w+|public\s+static\s+void\s+main/i,
            python: /def\s+\w+|print\s*\(|input\s*\(/i
        };

        for (const [key, regex] of Object.entries(hints)) {
            if (lang !== key && regex.test(codeText)) return true;
        }
        return false;
    }

    if (languageMismatch(language, code)) {
        resultsDiv.innerHTML = `
            <div class="error">
                ⚠ Check your code language.<br>
                Selected language: <b>${language.toUpperCase()}</b>
            </div>
        `;
        return;
    }

    try {
        const response = await fetch("http://127.0.0.1:8000/run", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ language, code, problem_id })
        });

        const data = await response.json();

        if (data.error) {
            resultsDiv.innerHTML = `<div class="error">❌ ${data.error}</div>`;
            return;
        }

        // Show results
        data.results.forEach((res, i) => {
            const div = document.createElement("div");
            div.className = res.passed ? "pass" : "fail";
            div.innerHTML = `
                <strong>Test Case ${i + 1}</strong><br>
                Input: ${res.input}<br>
                Expected: ${res.expected}<br>
                Output: ${res.actual}
            `;
            resultsDiv.appendChild(div);
        });

    } catch (err) {
        resultsDiv.innerHTML = `<div class="error">❌ Unable to connect to server</div>`;
    }
}
