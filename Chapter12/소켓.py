import socket

my sock = socket.socket(socket.AF_INET, SOCKET.SOCK_STREAM)
mysock.connnet(('data.pr4e.org',80))
cmd = 'GET htpp://data.pr4e,org/romeo.txt. HTTP/1.0\r\n\r\n'encode()
mysock.send(cmd)

while True:
    data = musock.recv(512)
    if (len(data) < 1) :
        break
    print(data.docode(),end=")
mysock.close()
