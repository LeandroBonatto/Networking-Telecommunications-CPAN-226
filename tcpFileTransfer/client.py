import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("Server host address: ")
port = 8000

s.connect((host, port))
print("Connected to server.")

filename = input("Enter the file name to request: ")
s.send(filename.encode())

file = open(filename, "wb")

while True:
    file_data = s.recv(1024)
    if not file_data:
        break
    file.write(file_data)

file.close()
print("Successfully get the file")

s.close()
print("Connection closed")

'''
socket object 's = socket.socket' - bind 'host' and 'port';
listening connections 's.listen';
Fill the filename to request to server;
Send filename using 's.send()';
Open a new file to write binary 'file = open(filename, "wb")';
Receive data from the server 'file_data = s.recv(1024)';
close the connection using 's.close()';
'''