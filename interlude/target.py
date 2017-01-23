import socket
import sys
import time
from datetime import datetime

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)
batt_level = 10

def decrement_batt(key=False):
    global batt_level
    if batt_level < 0:
        return -1
    if key:
        batt_level = batt_level - 1
        if batt_level < 0:
            return -1
        else:
            return batt_level

def increment_batt():
    global batt_level
    time.sleep(5)
    batt_level = 10

while True:
    # Wait for a connection
    print 'waiting for a connection'
    connection, client_address = sock.accept()
    d_date = datetime.now()
    reg_format_date = d_date.strftime("%Y-%m-%d %I:%M:%S %p")
    connection_established_text="connection established at %s" % reg_format_date
    print connection_established_text
    connection.sendall(connection_established_text)
    try:
        print  'connection from', client_address
        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print  'received "%s"' % data
            if data:
                batt = decrement_batt(data)
                print batt
                if batt < 0:
                    connection.sendall('battrey low recharging waiting for full charge')
                    increment_batt()
                else:
                    connection.sendall(data)
            else:
                print  'no more data from', client_address
                break
            
    finally:
        # Clean up the connection
        connection.close()


