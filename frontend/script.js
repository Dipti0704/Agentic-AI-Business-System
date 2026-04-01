const questionInput = document.getElementById("question");
const askBtn = document.getElementById("askBtn");
const responseDiv = document.getElementById("response");
const copyBtn = document.getElementById("copyBtn");
const downloadBtn = document.getElementById("downloadBtn");

// ===================== 🔥 REMOVED AGENT =====================
// const agentSelect = document.getElementById("agent");
// ============================================================

async function askAI() {
    const question = questionInput.value;

    if (!question) return alert("Type a question!");

    responseDiv.textContent = "Thinking... 🤖";

    const res = await fetch("http://127.0.0.1:5000/api/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            // ===================== 🔥 CHANGE =====================
            agent: null,
            // =====================================================
            question
        })
    });

    const data = await res.json();
    responseDiv.textContent = data.response || data.error;
}

askBtn.addEventListener("click", askAI);

copyBtn.addEventListener("click", () => {
    navigator.clipboard.writeText(responseDiv.textContent);
    alert("Copied!");
});

downloadBtn.addEventListener("click", () => {
    const blob = new Blob([responseDiv.textContent], { type: "text/plain" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = "response.txt";
    link.click();
});