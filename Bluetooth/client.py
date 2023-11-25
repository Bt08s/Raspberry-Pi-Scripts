import bluetooth

server_address = input("Address: ")
port = 1

client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
client_socket.connect((server_address, port))

while True:
    message = input("Enter the data to send (type 'exit' to quit): ")
    if message == "exit":
        break
    client_socket.send(message)

client_socket.close()
