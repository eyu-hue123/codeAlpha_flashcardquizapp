async function sendMessage() {
  const input = document.getElementById("user-input").value;
  const res = await fetch("http://localhost:5000/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({message: input})
  });
  const data = await res.json();
  const chatBox = document.getElementById("chat-box");
  chatBox.innerHTML += `<div><b>You:</b> ${input}</div>`;
  chatBox.innerHTML += `<div><b>Bot:</b> ${data.response}</div>`;
}
