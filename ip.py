import socket
wep = input("Enter url site: ")
ip = socket.gethostbyname(wep)
print(ip)