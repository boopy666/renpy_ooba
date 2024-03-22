import socket

# Socket connection details
RENPY_HOST = '127.0.0.1'
RENPY_PORT = 8000

# Socket connection
sock = None

def setup():
    global sock
    sock = socket.create_connection((RENPY_HOST, RENPY_PORT))

def output_modifier(string, state, is_chat=False):
    global sock
    modified_string = string + "=END>"
    if sock:
        try:
            sock.sendall(modified_string.encode('utf-8'))
        except socket.error as e:
            print(f"Socket error: {e}")
    return string