const agentSelect = document.getElementById("agent");
const suggestedSelect = document.getElementById("suggested");
const questionInput = document.getElementById("question");
const askBtn = document.getElementById("askBtn");
const responseDiv = document.getElementById("response");
const copyBtn = document.getElementById("copyBtn");
const downloadBtn = document.getElementById("downloadBtn");
const quickActions = document.querySelectorAll("#quickActions button");

const suggestionsMap = {
    marketing: ["Meta Ad for medical shop","Google Ads for new product","LinkedIn post for campaign"],
    sales: ["Prepare sales pitch","Customer follow-up email"],
    copywriting: ["Write catchy headline","Write persuasive email"],
    analytics: ["Generate campaign report","Predict CTR"]
};

agentSelect.addEventListener("change", ()=>{
    const agent = agentSelect.value;
    suggestedSelect.innerHTML='<option value="">-- Pick suggestion --</option>';
    (suggestionsMap[agent]||[]).forEach(s=>{
        const opt=document.createElement("option");
        opt.value=s; opt.textContent=s; suggestedSelect.appendChild(opt);
    });
});

suggestedSelect.addEventListener("change", ()=>{ questionInput.value=suggestedSelect.value; });

async function askAI(customQuestion){
    const agent = agentSelect.value;
    const question = customQuestion||questionInput.value;
    if(!question) return alert("Type a question!");
    responseDiv.textContent="Loading...";
    const res = await fetch("http://127.0.0.1:5000/api/ask", {
        method:"POST", headers:{"Content-Type":"application/json"},
        body:JSON.stringify({agent, question})
    });
    const data = await res.json();
    responseDiv.textContent = data.response || data.error;
}

askBtn.addEventListener("click",()=>askAI());

quickActions.forEach(btn=>btn.addEventListener("click", ()=>{
    let question=questionInput.value; if(!question) return alert("Type base question!");
    const act=btn.dataset.action;
    if(act==="generate") question+=" [Generate full ad copy]";
    else if(act==="optimize") question+=" [Optimize campaign]";
    else if(act==="analytics") question+=" [Show analytics]";
    askAI(question);
}));

copyBtn.addEventListener("click",()=>{navigator.clipboard.writeText(responseDiv.textContent); alert("Copied!");});
downloadBtn.addEventListener("click",()=>{
    const blob=new Blob([responseDiv.textContent],{type:"text/plain"});
    const link=document.createElement("a");
    link.href=URL.createObjectURL(blob); link.download="response.txt"; link.click();
});