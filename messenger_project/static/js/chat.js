// Подключение к WebSocket-серверу
const roomName = "{{ room_name }}";
const chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/chat/' + roomName + '/'
);


// Обработчик открытия соединения
chatSocket.onopen = function(event) {
    console.log("WebSocket соединение установлено.");
};

// Обработчик получения сообщения
chatSocket.onmessage = function(event) {
    const messageData = JSON.parse(event.data);
    console.log("Получено сообщение:", messageData);

    // Отображение сообщения в контейнере сообщений
    const messageContainer = document.getElementById("messageContainer");
    const messageElement = document.createElement("div");
    messageElement.textContent = `${messageData.username || "Anonymous"}: ${messageData.message}`;
    messageContainer.appendChild(messageElement);
};

// Обработчик закрытия соединения
chatSocket.onclose = function(event) {
    console.log("WebSocket соединение закрыто.");
};

// Функция отправки сообщения
function sendMessage(text) {
    chatSocket.send(JSON.stringify({ message: text }));
    console.log("Сообщение отправлено:", text);
}

function sendMessageFromInput() {
    const input = document.getElementById("messageInput");
    const message = input.value;
    if (message.trim()) {
        sendMessage(message);
        input.value = '';  // Очистка поля ввода после отправки
    }
}
