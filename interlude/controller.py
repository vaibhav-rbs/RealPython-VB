import socket
import sys
import curses
import signal

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

stdscr = curses.initscr()
stdscr.keypad(1)

def signal_handler(signal, frame):
    print('You pressed Ctrl+C!')
    sys.exit(0)

try:
    key = ''
    while True:
        signal.signal(signal.SIGINT, signal_handler)
        print('Press Ctrl+C to exit')
        key = stdscr.getch()
        # Send data
        print 'sending "%s"' % chr(key)
        sock.sendall(str(key))
    curses.endwin()
    
finally:
    print >>sys.stderr, 'closing socket'
    sock.close()
