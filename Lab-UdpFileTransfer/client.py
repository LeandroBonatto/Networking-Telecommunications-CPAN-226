import socket

payload_size = 1024

def UDPclient(port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', port)

    filename = 'myfile.txt'
    filename_pdu = b'F' + filename.encode()
    client_socket.sendto(filename_pdu, server_address)

    try:
        with open(filename, 'wb') as file:
            while True:
                pdu, server_address = client_socket.recvfrom(payload_size)
                pdu_type = pdu[0:1]

                if pdu_type == b'D':
                    data = pdu[1:]
                    file.write(data)
                elif pdu_type == b'L':
                    print('File transfer is done.')
                    break
                elif pdu_type == b'E':
                    error_message = pdu[1:].decode()
                    print('Error:', error_message)
                    break
    except PermissionError:
        print('Error. Please try another filename.')

    client_socket.close()

'''
import: socket module;
payload_size = max bytes transferred - pdu;
UPDclient = function client side;
client_socket = AF_INET is the address family and DGRAM is socket type for UDP communication;
server_address = server address and port number client connection;
filename = name of file client want download;
filename_pdu = create a filename using pdu by concatenate the filename;
socket.sendto = send the filename to especified server address;
pdu, server address = receive pdu from server. The recvfrom return  both pdu data;
pdu_type = identify its type by extracting the first byte (pdu[0:1]);
pdu Data = data portion of the PDU is extracted;
pdu Last = file transfer is completed;
pdu Error = error message;
socket close = after the file transfer is done;
'''


