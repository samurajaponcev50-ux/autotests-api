import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))
client_socket.send("Деревья расстут только вверх...".encode())

response = client_socket.recv(1024).decode()
print(f"Ответ от сервера: {response}")

client_socket.close()

