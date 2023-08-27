// window.onload = function name(params) {
    
// }



function send_request() {
    // event.preventDefault()
    const textareaValue = document.getElementById("prompt").value;
    console.log(textareaValue);
    fetch("http://127.0.0.1:5000/api/data", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            key1: textareaValue
        }),
    })
    .then(response =>  response.json())
    .then(data => {
        let valueFromKey1 = data.received_data;
        show_respone(JSON.stringify(valueFromKey1));
        console.log(data.key1);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
    // show_respone();
}

function show_respone(message) {
    const convoSection = document.getElementById("convo");
    const newElement = document.createElement('p');

    // Replace newline characters with <br> elements
    message = message.replace(/\n/g, '<br>');
    
    // Use innerHTML instead of textContent to interpret the <br> tags
    newElement.innerHTML = message;
    
    convoSection.appendChild(newElement);
}
