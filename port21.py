import socket
 
s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
 
s.connect(("fe80::3596:f5ad:a5b8:d282%16", 3307))
 
print("Connected to local IPv6 Apache server")
