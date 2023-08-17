import socket

payload_size = 1024

def UDPserver(port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', port)
    server_socket.bind(server_address)

    print('Server started and listening for connections...')

    while True:
        data, client_address = server_socket.recvfrom(payload_size)
        pdu_type = data[0:1]
        if pdu_type == b'F':
            filename = data[1:].decode()
            print('Client requested file:', filename)

            try:
                with open(filename, 'rb') as file:
                    while True:
                        data = file.read(payload_size)
                        if not data:
                            break
                        pdu = b'D' + data
                        server_socket.sendto(pdu, client_address)

                last_pdu = b'L'
                server_socket.sendto(last_pdu, client_address)

                print('File transfer is done.')
            except FileNotFoundError:
                error_pdu = b'E'
                server_socket.sendto(error_pdu, client_address)
                print('File not found.')

    server_socket.close()

'''
import: socket module;
payload_size = max bytes transferred - pdu;
UDPserver(port) = function server;
server_socket = client_socket = AF_INET is the address family and DGRAM is socket type for UDP communication;
server_address = address and port number;
socket.bind = binds socket, address and port for incoming client request;
data, client_address = receive and return data to client;
pdu_type = identify its type by extracting the first byte (pdu[0:1]);
pdu_type F (filename) = client is request a file transfer;
rb = read binary;
pdu Data = data read from the file;
socket.sendto = send data to the client;
last_pdu = end of the file transfer;
pdu Error = file not found;
socket close = server finished;
'''
