const chatForm = document.getElementById("chat-form");
const chatbox = document.getElementById("chatbox");
const input = document.getElementById("input");

chatForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    const message = input.value.trim();
    if (!message) return;

    addMessageToChatbox(`You: ${message}`);
    input.value = "";
    input.focus();

    const response = await fetch("/api/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ prompt: message })
    });

    const responseText = await response.text();
    addMessageToChatbox(`ChatGPT: ${responseText}`);
});

function addMessageToChatbox(message) {
    const messageElement = document.createElement("div");
    messageElement.innerHTML = "<b>" + message.substring(0, message.indexOf(":")+2) + "</b>" + message.substring(message.indexOf(":")+2);
    messageElement.className = "message";
    chatbox.appendChild(messageElement);

    chatbox.scrollTop = chatbox.scrollHeight;
}

