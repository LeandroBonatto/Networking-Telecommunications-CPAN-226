import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8000
s.bind((host, port))
s.listen(1)
print("Server listening....")

conn, addr = s.accept()
print("Got connection from", addr)

filename = conn.recv(1024).decode()
print("Server received the file name:", filename)

try:
    with open(filename, 'rb') as file:
        file_data = file.read()
        conn.sendall(file_data)
    print("Sent")
except FileNotFoundError:
    error_message = "Error: File not found"
    conn.sendall(error_message.encode())

conn.close()
print("Connection closed")


'''
socket object 's = socket.socket' - bind 'host' and 'port';
listening connections 's.listen';
Connection accept 's.accept()', returning a socket object 'conn' and client 'addr';
Filename receiving and decode 'conn.recv(1024)'
open the requested file and read, if open successful send file to client using 'conn.sendall';
If fail to open error message will show;
close connection 'conn.close()'
'''