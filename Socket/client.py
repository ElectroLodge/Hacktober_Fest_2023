import socket

server_port = 8080
server_address = ("127.0.0.1",server_port)

client_port = 8081
client_address = ("",client_port)

try:
    server_socket = socket.create_server(client_address)

    print("Connecting to the Server...\n")
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect(server_address)
    
    (connection,address) = server_socket.accept()

    print("Handshake completed...\n")
except Exception as ex:
    print("Exception in creating a socket\n")
    print(ex)


while(True):

    print("What do you want to convey to the Server : ",end="")
    client_response_in_text = input()
    client_response_in_bytes = client_response_in_text.encode("utf-8")
    connection.send(client_response_in_bytes)

    print("Listening for any communication...\n")
    server_response_in_bytes = client_socket.recv(1024)
    server_response_in_text = server_response_in_bytes.decode("utf-8")

    print("Server : "+server_response_in_text,end="\n")