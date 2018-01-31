const io = require('socket.io-client');
auth_data = {}
const socket = io('http://localhost:8080/fanout', {
    transportOptions: {
        polling: {
            extraHeaders: auth_data
        }
    }
})
socket.on('connect', () => {
    console.log('connect')
    socket.send('raw message from client')
    socket.emit('my_event', 'event from client')
})
socket.connect()
socket.on('message', (data) => {
    console.log('message =>', data)
})
socket.on('my event', (data) => {
    console.log('message =>', data)
})
