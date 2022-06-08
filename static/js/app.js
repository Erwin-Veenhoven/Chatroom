
const socket = io(socketURL);
let input = document.querySelector('input');

socket.on('message', text => {

    const el = document.createElement('li');
    el.innerHTML = text;
    document.querySelector('ul').appendChild(el);

});

input.addEventListener('keyup', (e) => {

    if (e.keyCode === 13) {
        sendMessage()
    }
});

document.querySelector('button').onclick = () => {

    sendMessage()
}

function sendMessage() {

    const text = input.value;
    if (text == '') return
    socket.emit('message', text);
    input.value = '';
}