import socket

server_port = 8080
server_address = ("",server_port)

client_port = 8081
client_address = ("127.0.0.1",client_port)

try:
    server_socket = socket.create_server(server_address)
    (connection,address) = server_socket.accept()

    print("Initiating a Handshake...")

    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client_socket.connect(client_address)
except:
    print("Exception in creating a socket")

while(True):

    print("\nListening for any communication...\n")
    client_response_in_bytes = client_socket.recv(1024)
    client_response_in_text = client_response_in_bytes.decode("utf-8")

    print("Client : "+client_response_in_text,end="\n")

    print("Generating Response...\n")
    print("Enter your Response : ",end="")
    server_response_in_text = input()
    server_response_in_bytes = server_response_in_text.encode("utf-8")
    connection.send(server_response_in_bytes)



