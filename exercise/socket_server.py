import socket
import time

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.bind(('127.0.0.1',9999))
s.listen(5)
print 'Waiting for connection...'

sock,addr = s.accept()
sock.send('Welcome! \n')

while True:
    data = sock.recv(1024)
    time.sleep(1)
    if data.strip() == 'exit':
        close = True
        break
    sock.send('Hello,%s!\n' % data.strip())
if close:
    sock.close()
    print 'connection from %s:%s closed.' % addr

