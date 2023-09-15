import socket
print(socket.getfqdn())


print(socket.gethostname())


print(socket.gethostbyname(socket.gethostname()))
print(socket.gethostbyname(socket.getfqdn()))


