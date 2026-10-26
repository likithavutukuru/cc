#server.py
import socket
server = socket.socket()
server.bind(("127.0.0.1", 5000))
server.listen(5)
print("Server waiting for client...")
conn, addr = server.accept()
print("Client connected",addr)
data = conn.recv(1024).decode()
marks = list(map(int, data.split()))
total = sum(marks)
percentage = total / len(marks)

if all(m >= 35 for m in marks):
    result = "Pass"
    if percentage >= 90:
        rank = "A"
    elif percentage >= 75:
        rank = "B"
    elif percentage >= 60:
        rank = "C"
    else:
        rank = "D"
else:
    result = "Fail"
    rank = "F"
response = (
    f"Total: {total}\n"
    f"Percentage: {percentage:.2f}%\n"
    f"Result: {result}\n"
    f"Rank: {rank}"
)
conn.send(response.encode())
print("Result sent to client")
conn.close()
server.close()

#client.py
import socket
client = socket.socket()
client.connect(("127.0.0.1", 5000))
m1 = int(input("Enter Subject 1 marks: "))
m2 = int(input("Enter Subject 2 marks: "))
m3 = int(input("Enter Subject 3 marks: "))
marks = f"{m1} {m2} {m3}"
client.send(marks.encode())
response = client.recv(1024).decode()
print("\nResult from Server:")
print(response)
client.close()