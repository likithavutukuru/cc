#server
import socket
import os
server = socket.socket()
server.bind(("127.0.0.1", 5000))
server.listen(5)
print("Server waiting for client...")
conn, addr = server.accept()
print("Client connected")
filename = conn.recv(1024).decode().strip()
if os.path.isfile(filename):
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    lines = len(content.splitlines())
    words = len(content.split())
    size = os.path.getsize(filename)
    response = (
        f"Lines: {lines}\n"
        f"Words: {words}\n"
        f"File size: {size} bytes"
    )
else:
    response = "File not found"
conn.send(response.encode())
conn.close()
server.close()


#client.py
import socket
client = socket.socket()
client.connect(("127.0.0.1", 5000))
filename = input("Enter filename: ")
client.send(filename.encode())
response = client.recv(1024).decode()
print("\nFile Details:")
print(response)
client.close()