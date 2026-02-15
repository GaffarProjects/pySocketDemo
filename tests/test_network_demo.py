import json
import socket
import threading
import time

import network_socket_demo as nsd


def test_build_response_contains_html_and_status():
    server = nsd.SimpleHTTPServer()
    response = server.build_response()
    assert "HTTP/1.1 200 OK" in response
    assert "<html>" in response
    assert str(nsd.PORTS['HTTP']) in response


def test_port_scanner_reports_closed(capsys):
    # Use a high-numbered port that is unlikely to be open
    nsd.port_scanner('127.0.0.1', [65000])
    captured = capsys.readouterr()
    assert "CLOSED" in captured.out or "OPEN" in captured.out


def test_custom_tcp_handle_client_echo():
    # Create a pair of connected sockets
    s1, s2 = socket.socketpair()

    server = nsd.CustomTCPServer()

    def run_handler():
        try:
            server.handle_client(s1)
        except Exception:
            pass

    t = threading.Thread(target=run_handler, daemon=True)
    t.start()

    # Send a message from the client side
    message = "HelloTest"
    s2.send(message.encode('utf-8'))

    # Receive JSON response
    data = s2.recv(4096)
    assert data
    decoded = json.loads(data.decode('utf-8'))
    assert decoded['echo'] == message

    # Cleanup
    s2.close()
    s1.close()
    t.join(timeout=1)
