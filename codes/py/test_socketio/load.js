const io = require('socket.io-client');
const args = process.argv
port = 8080
if (args.length > 2) {
    port = args[2]
}
console.log('port = ', port)
const socket = io('http://localhost:' + port + '/fanout', {
    // TODO: not working. too bad.
    localAddress: '192.168.77.28'
})
socket.on('connect', () => {
    console.log('connect')
})
socket.connect()
socket.on('message', (data) => {
    console.log('message =>', data)
})
socket.on('my event', (data) => {
    console.log('message =>', data)
})