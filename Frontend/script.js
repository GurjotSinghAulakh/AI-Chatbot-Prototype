document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("chat-form").addEventListener("submit", function(event) {
        event.preventDefault();
        const userInput = document.getElementById("user-input").value;
        
        // Append user input to chat history
        const chatHistory = document.getElementById("chat-history");
        const userMessageDiv = document.createElement("div");
        userMessageDiv.className = "chat-message user-message";
        userMessageDiv.innerText = userInput;
        chatHistory.appendChild(userMessageDiv);

        // Fetch user input to the Flask server for processing
        fetch("http://127.0.0.1:5000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: userInput })
        })
        .then(response => response.json())
        .then(data => {
            // Append bot response to chat history
            const botMessageDiv = document.createElement("div");
            botMessageDiv.className = "chat-message bot-message";
            botMessageDiv.innerText = data.response;
            chatHistory.appendChild(botMessageDiv);

            // Scroll to the bottom of the chat history
            chatHistory.scrollTop = chatHistory.scrollHeight;

            // Clear the input field
            document.getElementById("user-input").value = "";
        })
        .catch(error => console.error("Error:", error));
    });
});
