#server.py
import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 12345))
server.listen(1)
print("Server waiting for client...")
conn, addr = server.accept()
print("Client connected")
data = conn.recv(1024).decode()
digits = sum(ch.isdigit() for ch in data)
spaces = data.count(" ")
response = f"Number of digits: {digits}\nNumber of spaces: {spaces}"
conn.send(response.encode())
conn.close()
server.close()

#client.py
import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 12345))
message = input("Enter a string: ")
client.send(message.encode())
response = client.recv(1024).decode()
print("\nResult from server:")
print(response)
client.close()
