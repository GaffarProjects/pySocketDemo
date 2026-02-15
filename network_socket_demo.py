"""
Network Socket Programming Demonstration
==========================================
Demonstrates socket programming with different protocols and ports

Author: [Your Name]
LinkedIn: [Your Profile]
Date: February 2026

This program demonstrates:
- HTTP Server (Port 8080)
- FTP Server (Port 2121)
- SMTP Server (Port 2525)
- Custom TCP/UDP Servers
- DNS Query (Port 53)
- Cloud-ready socket implementations
"""

import socket
import threading
import time
from datetime import datetime
import json

# ============================================================================
# CONFIGURATION - Standard and Custom Ports
# ============================================================================

PORTS = {
    'HTTP': 8080,      # Web traffic (standard: 80/443)
    'FTP': 2121,       # File Transfer (standard: 21)
    'SMTP': 2525,      # Email (standard: 25)
    'DNS': 5353,       # Domain Name System (standard: 53)
    'CUSTOM_TCP': 9000,
    'CUSTOM_UDP': 9001,
    'WEBSOCKET': 8765,
    'DATABASE': 5432,  # PostgreSQL-like (standard: 5432)
}

HOST = '127.0.0.1'  # Localhost - change to '0.0.0.0' for cloud deployment


# ============================================================================
# 1. HTTP SERVER - Web Traffic (Port 8080)
# ============================================================================

class SimpleHTTPServer:
    """Basic HTTP server demonstrating web protocol"""
    
    def __init__(self, host=HOST, port=PORTS['HTTP']):
        self.host = host
        self.port = port
        self.socket = None
        
    def start(self):
        """Start the HTTP server"""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        print(f"✓ HTTP Server listening on {self.host}:{self.port}")
        
        while True:
            try:
                client_socket, address = self.socket.accept()
                print(f"  → HTTP Connection from {address}")
                threading.Thread(target=self.handle_client, args=(client_socket,)).start()
            except Exception as e:
                print(f"  ✗ HTTP Error: {e}")
                break
    
    def handle_client(self, client_socket):
        """Handle HTTP request"""
        try:
            request = client_socket.recv(1024).decode('utf-8')
            print(f"  → Request: {request.split()[0:2] if request else 'Empty'}")
            
            # HTTP Response
            response = self.build_response()
            client_socket.send(response.encode('utf-8'))
        except Exception as e:
            print(f"  ✗ Error handling HTTP request: {e}")
        finally:
            client_socket.close()
    
    def build_response(self):
        """Build HTTP response"""
        html_content = """
        <!DOCTYPE html>
        <html>
        <head><title>Socket Programming Demo</title></head>
        <body>
            <h1>Socket Programming Demonstration</h1>
            <p>Server Time: {}</p>
            <p>Protocol: HTTP/1.1</p>
            <p>Port: {}</p>
        </body>
        </html>
        """.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), PORTS['HTTP'])
        
        response = f"HTTP/1.1 200 OK\r\n"
        response += f"Content-Type: text/html\r\n"
        response += f"Content-Length: {len(html_content)}\r\n"
        response += f"Connection: close\r\n\r\n"
        response += html_content
        
        return response


# ============================================================================
# 2. FTP SERVER - File Transfer Protocol (Port 2121)
# ============================================================================

class SimpleFTPServer:
    """Basic FTP server for file transfer demonstration"""
    
    def __init__(self, host=HOST, port=PORTS['FTP']):
        self.host = host
        self.port = port
        self.socket = None
        
    def start(self):
        """Start FTP server"""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        print(f"✓ FTP Server listening on {self.host}:{self.port}")
        
        while True:
            try:
                client_socket, address = self.socket.accept()
                print(f"  → FTP Connection from {address}")
                threading.Thread(target=self.handle_client, args=(client_socket,)).start()
            except Exception as e:
                print(f"  ✗ FTP Error: {e}")
                break
    
    def handle_client(self, client_socket):
        """Handle FTP commands"""
        try:
            # Send welcome message
            client_socket.send(b"220 Welcome to Simple FTP Server\r\n")
            
            while True:
                data = client_socket.recv(1024).decode('utf-8').strip()
                if not data:
                    break
                
                print(f"  → FTP Command: {data}")
                
                if data.upper().startswith('USER'):
                    client_socket.send(b"331 Username OK, need password\r\n")
                elif data.upper().startswith('PASS'):
                    client_socket.send(b"230 Login successful\r\n")
                elif data.upper() == 'PWD':
                    client_socket.send(b"257 \"/\" is current directory\r\n")
                elif data.upper() == 'QUIT':
                    client_socket.send(b"221 Goodbye\r\n")
                    break
                else:
                    client_socket.send(b"502 Command not implemented\r\n")
        except Exception as e:
            print(f"  ✗ Error handling FTP: {e}")
        finally:
            client_socket.close()


# ============================================================================
# 3. SMTP SERVER - Email Protocol (Port 2525)
# ============================================================================

class SimpleSMTPServer:
    """Basic SMTP server for email demonstration"""
    
    def __init__(self, host=HOST, port=PORTS['SMTP']):
        self.host = host
        self.port = port
        self.socket = None
        
    def start(self):
        """Start SMTP server"""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        print(f"✓ SMTP Server listening on {self.host}:{self.port}")
        
        while True:
            try:
                client_socket, address = self.socket.accept()
                print(f"  → SMTP Connection from {address}")
                threading.Thread(target=self.handle_client, args=(client_socket,)).start()
            except Exception as e:
                print(f"  ✗ SMTP Error: {e}")
                break
    
    def handle_client(self, client_socket):
        """Handle SMTP commands"""
        try:
            client_socket.send(b"220 Simple SMTP Server Ready\r\n")
            
            while True:
                data = client_socket.recv(1024).decode('utf-8').strip()
                if not data:
                    break
                
                print(f"  → SMTP Command: {data}")
                
                if data.upper().startswith('EHLO') or data.upper().startswith('HELO'):
                    client_socket.send(b"250 Hello\r\n")
                elif data.upper().startswith('MAIL FROM'):
                    client_socket.send(b"250 OK\r\n")
                elif data.upper().startswith('RCPT TO'):
                    client_socket.send(b"250 OK\r\n")
                elif data.upper() == 'DATA':
                    client_socket.send(b"354 Start mail input\r\n")
                elif data == '.':
                    client_socket.send(b"250 Message accepted\r\n")
                elif data.upper() == 'QUIT':
                    client_socket.send(b"221 Bye\r\n")
                    break
                else:
                    client_socket.send(b"250 OK\r\n")
        except Exception as e:
            print(f"  ✗ Error handling SMTP: {e}")
        finally:
            client_socket.close()


# ============================================================================
# 4. CUSTOM TCP SERVER - Application-Specific Protocol
# ============================================================================

class CustomTCPServer:
    """Custom TCP server for application-specific communication"""
    
    def __init__(self, host=HOST, port=PORTS['CUSTOM_TCP']):
        self.host = host
        self.port = port
        self.socket = None
        
    def start(self):
        """Start custom TCP server"""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        self.socket.listen(5)
        print(f"✓ Custom TCP Server listening on {self.host}:{self.port}")
        
        while True:
            try:
                client_socket, address = self.socket.accept()
                print(f"  → TCP Connection from {address}")
                threading.Thread(target=self.handle_client, args=(client_socket,)).start()
            except Exception as e:
                print(f"  ✗ TCP Error: {e}")
                break
    
    def handle_client(self, client_socket):
        """Handle custom protocol"""
        try:
            while True:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break
                
                print(f"  → Received: {data}")
                
                # Echo with timestamp
                response = {
                    'timestamp': datetime.now().isoformat(),
                    'echo': data,
                    'server': 'CustomTCP'
                }
                client_socket.send(json.dumps(response).encode('utf-8'))
        except Exception as e:
            print(f"  ✗ Error handling TCP: {e}")
        finally:
            client_socket.close()


# ============================================================================
# 5. UDP SERVER - Connectionless Protocol
# ============================================================================

class CustomUDPServer:
    """UDP server for connectionless communication"""
    
    def __init__(self, host=HOST, port=PORTS['CUSTOM_UDP']):
        self.host = host
        self.port = port
        self.socket = None
        
    def start(self):
        """Start UDP server"""
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.host, self.port))
        print(f"✓ UDP Server listening on {self.host}:{self.port}")
        
        while True:
            try:
                data, address = self.socket.recvfrom(1024)
                print(f"  → UDP from {address}: {data.decode('utf-8')}")
                
                # Send response
                response = f"UDP Echo: {data.decode('utf-8')} at {datetime.now()}"
                self.socket.sendto(response.encode('utf-8'), address)
            except Exception as e:
                print(f"  ✗ UDP Error: {e}")
                break


# ============================================================================
# 6. DNS QUERY CLIENT - Domain Name Resolution
# ============================================================================

def dns_query_demo(domain='google.com'):
    """Demonstrate DNS query"""
    try:
        print(f"\n📡 DNS Query for: {domain}")
        ip_address = socket.gethostbyname(domain)
        print(f"  → IP Address: {ip_address}")
        
        # Get full info
        host_info = socket.gethostbyname_ex(domain)
        print(f"  → Hostname: {host_info[0]}")
        print(f"  → Aliases: {host_info[1]}")
        print(f"  → IP List: {host_info[2]}")
    except socket.gaierror as e:
        print(f"  ✗ DNS Error: {e}")


# ============================================================================
# 7. PORT SCANNER - Network Reconnaissance
# ============================================================================

def port_scanner(host, ports):
    """Scan common ports"""
    print(f"\n🔍 Scanning {host} for open ports...")
    
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        
        if result == 0:
            print(f"  ✓ Port {port} is OPEN")
        else:
            print(f"  ✗ Port {port} is CLOSED")
        
        sock.close()


# ============================================================================
# 8. CLIENT EXAMPLES
# ============================================================================

def http_client_demo():
    """HTTP client example"""
    print("\n📤 HTTP Client Demo")
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORTS['HTTP']))
        
        request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
        client.send(request.encode('utf-8'))
        
        response = client.recv(4096).decode('utf-8')
        print(f"  → Response received ({len(response)} bytes)")
        
        client.close()
    except Exception as e:
        print(f"  ✗ Error: {e}")


def tcp_client_demo():
    """TCP client example"""
    print("\n📤 TCP Client Demo")
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST, PORTS['CUSTOM_TCP']))
        
        message = "Hello from TCP Client!"
        client.send(message.encode('utf-8'))
        
        response = client.recv(1024).decode('utf-8')
        print(f"  → Server response: {response}")
        
        client.close()
    except Exception as e:
        print(f"  ✗ Error: {e}")


def udp_client_demo():
    """UDP client example"""
    print("\n📤 UDP Client Demo")
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        message = "Hello from UDP Client!"
        client.sendto(message.encode('utf-8'), (HOST, PORTS['CUSTOM_UDP']))
        
        data, server = client.recvfrom(1024)
        print(f"  → Server response: {data.decode('utf-8')}")
        
        client.close()
    except Exception as e:
        print(f"  ✗ Error: {e}")


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """Main execution"""
    print("=" * 70)
    print("NETWORK SOCKET PROGRAMMING DEMONSTRATION")
    print("=" * 70)
    print(f"Host: {HOST}")
    print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)
    
    # Start all servers in separate threads
    servers = [
        ('HTTP', SimpleHTTPServer()),
        ('FTP', SimpleFTPServer()),
        ('SMTP', SimpleSMTPServer()),
        ('Custom TCP', CustomTCPServer()),
        ('UDP', CustomUDPServer()),
    ]
    
    threads = []
    for name, server in servers:
        thread = threading.Thread(target=server.start, daemon=True)
        thread.start()
        threads.append(thread)
        time.sleep(0.2)  # Stagger startup
    
    print("\n" + "=" * 70)
    print("ALL SERVERS STARTED - Running demonstrations...")
    print("=" * 70)
    
    # Give servers time to start
    time.sleep(1)
    
    # Run demonstrations
    dns_query_demo('google.com')
    time.sleep(0.5)
    
    port_scanner(HOST, [PORTS['HTTP'], PORTS['FTP'], PORTS['CUSTOM_TCP']])
    time.sleep(0.5)
    
    http_client_demo()
    time.sleep(0.5)
    
    tcp_client_demo()
    time.sleep(0.5)
    
    udp_client_demo()
    
    print("\n" + "=" * 70)
    print("DEMONSTRATION COMPLETE")
    print("Servers are still running. Press Ctrl+C to stop.")
    print("=" * 70)
    
    # Keep main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down servers...")
        print("Thank you for viewing this demonstration!")


if __name__ == "__main__":
    main()
