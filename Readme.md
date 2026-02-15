# Socket Programming with Multiple Protocols - Network Demonstration

## 🌐 Overview

This Python program demonstrates professional socket programming across multiple network protocols, showcasing real-world networking concepts used in cloud and enterprise environments.

## 📋 Protocols Implemented

| Protocol | Port | Purpose | Use Case |
|----------|------|---------|----------|
| **HTTP** | 8080 | Web traffic | Web servers, REST APIs, microservices |
| **FTP** | 2121 | File transfer | File sharing, backup systems |
| **SMTP** | 2525 | Email | Email servers, notification systems |
| **DNS** | 5353 | Name resolution | Domain lookups, service discovery |
| **Custom TCP** | 9000 | Reliable communication | Application protocols, data streaming |
| **Custom UDP** | 9001 | Fast communication | Gaming, live video, IoT sensors |
| **Database** | 5432 | Database connections | PostgreSQL, cloud databases |
| **WebSocket** | 8765 | Real-time bidirectional | Chat apps, live dashboards |

## 🚀 Features

### 1. **Multi-Protocol Support**
- HTTP server with proper response formatting
- FTP server with command handling
- SMTP server for email protocol
- Custom TCP/UDP servers for application-specific needs

### 2. **Client Demonstrations**
- HTTP client making web requests
- TCP client for reliable communication
- UDP client for connectionless messaging
- DNS query examples

### 3. **Network Tools**
- Port scanner for reconnaissance
- DNS resolver for domain lookups
- Connection monitoring

### 4. **Cloud-Ready Design**
- Threaded server architecture
- Configurable host/port settings
- Error handling and logging
- Production-ready patterns

## 💻 Installation & Usage

### Prerequisites
```bash
Python 3.7 or higher (no external dependencies required)
```

### Running the Program
```bash
python network_socket_demo.py
```

### Testing

Install `pytest` (recommended) and run the test suite included in `tests/`:

```bash
# Install pytest in your environment (use virtualenv or system Python)
python -m pip install --user pytest

# Run the tests
python -m pytest -q
```

The repository includes basic tests at `tests/test_network_demo.py` which cover HTTP response building, a simple port-scanner run, and a `CustomTCPServer` echo handler.

### Development & Branching

Use feature branches for changes and push to `origin` when ready. Example workflow:

```bash
# Create a feature branch
git checkout -b feature/your-change

# Make changes, run tests
python -m pytest -q

# Commit and push
git add .
git commit -m "Describe your change"
git push -u origin feature/your-change
```

Create a Pull Request on GitHub when the branch is ready for review.


### Testing Individual Servers

**Test HTTP Server:**
```bash
curl http://localhost:8080
# or open in browser: http://localhost:8080
```

**Test FTP Server:**
```bash
telnet localhost 2121
# Commands: USER username, PASS password, PWD, QUIT
```

**Test SMTP Server:**
```bash
telnet localhost 2525
# Commands: HELO localhost, MAIL FROM:<test@example.com>, QUIT
```

**Test Custom TCP:**
```bash
python -c "import socket; s=socket.socket(); s.connect(('localhost',9000)); s.send(b'Hello'); print(s.recv(1024)); s.close()"
```

**Test UDP:**
```bash
python -c "import socket; s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.sendto(b'Hello', ('localhost',9001)); print(s.recvfrom(1024)); s.close()"
```

## ☁️ Cloud Deployment Guide

### AWS EC2 Deployment

1. **Launch EC2 instance** (Ubuntu 22.04)
2. **Configure Security Group:**
   ```
   Inbound Rules:
   - HTTP: 8080 (TCP)
   - FTP: 2121 (TCP)
   - SMTP: 2525 (TCP)
   - Custom TCP: 9000
   - Custom UDP: 9001
   ```

3. **Deploy:**
   ```bash
   # SSH into instance
   ssh -i your-key.pem ubuntu@your-ec2-ip
   
   # Install Python (if needed)
   sudo apt update
   sudo apt install python3 python3-pip
   
   # Upload and run
   scp -i your-key.pem network_socket_demo.py ubuntu@your-ec2-ip:~
   python3 network_socket_demo.py
   ```

4. **Update HOST variable:**
   ```python
   HOST = '0.0.0.0'  # Listen on all interfaces
   ```

### Google Cloud Platform (GCP)

1. **Create Compute Engine instance**
2. **Configure Firewall Rules:**
   ```bash
   gcloud compute firewall-rules create socket-demo \
     --allow tcp:8080,tcp:2121,tcp:2525,tcp:9000,udp:9001
   ```

3. **Deploy using Cloud Shell or SSH**

### Azure

1. **Create Virtual Machine**
2. **Configure Network Security Group (NSG):**
   - Add inbound rules for ports: 8080, 2121, 2525, 9000, 9001

3. **Deploy via SSH**

### Docker Deployment

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY network_socket_demo.py .

# Expose all ports
EXPOSE 8080 2121 2525 9000 9001

CMD ["python", "network_socket_demo.py"]
```

**Build and run:**
```bash
docker build -t socket-demo .
docker run -p 8080:8080 -p 2121:2121 -p 2525:2525 -p 9000:9000 -p 9001:9001 socket-demo
```

### Kubernetes Deployment

```yaml
apiVersion: v1
kind: Service
metadata:
  name: socket-demo
spec:
  type: LoadBalancer
  ports:
  - port: 8080
    name: http
  - port: 2121
    name: ftp
  - port: 9000
    name: tcp
  selector:
    app: socket-demo
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: socket-demo
spec:
  replicas: 1
  selector:
    matchLabels:
      app: socket-demo
  template:
    metadata:
      labels:
        app: socket-demo
    spec:
      containers:
      - name: socket-demo
        image: your-registry/socket-demo:latest
        ports:
        - containerPort: 8080
        - containerPort: 2121
        - containerPort: 9000
```

## 🏗️ Architecture Concepts

### TCP vs UDP
- **TCP (Transmission Control Protocol)**: Connection-oriented, reliable, ordered delivery
  - Use for: HTTP, FTP, SMTP, databases, file transfers
  
- **UDP (User Datagram Protocol)**: Connectionless, fast, no guarantee
  - Use for: DNS, streaming, gaming, IoT, real-time applications

### Port Numbers

```
0-1023:     Well-known ports (system/privileged)
1024-49151: Registered ports (applications)
49152-65535: Dynamic/private ports
```

### Socket Types

```python
# Stream socket (TCP)
socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Datagram socket (UDP)
socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Raw socket (advanced)
socket.socket(socket.AF_INET, socket.SOCK_RAW)
```

## 🔒 Production Considerations

### Security
- Implement authentication/authorization
- Use SSL/TLS for encryption
- Validate all input data
- Implement rate limiting
- Use firewall rules

### Performance
- Connection pooling
- Load balancing
- Async I/O (asyncio)
- Caching strategies

### Monitoring
- Log all connections
- Track metrics (connections/sec, latency)
- Alert on failures
- Health checks

### Example with SSL:
```python
import ssl

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

secure_socket = context.wrap_socket(server_socket, server_side=True)
```

## 📊 Common Cloud Ports

| Service | Port | Protocol |
|---------|------|----------|
| PostgreSQL | 5432 | TCP |
| MySQL | 3306 | TCP |
| MongoDB | 27017 | TCP |
| Redis | 6379 | TCP |
| Elasticsearch | 9200 | TCP |
| Kafka | 9092 | TCP |
| RabbitMQ | 5672 | TCP |
| Kubernetes API | 6443 | TCP |
| Docker | 2375/2376 | TCP |
| gRPC | 50051 | TCP |

## 🎓 Learning Outcomes

After studying this code, you'll understand:

1. **Socket Programming Basics**
   - Creating client and server sockets
   - Binding, listening, accepting connections
   - Sending and receiving data

2. **Protocol Implementation**
   - How HTTP, FTP, SMTP work at the socket level
   - Request/response patterns
   - Protocol state machines

3. **Networking Concepts**
   - TCP vs UDP differences
   - Port numbers and their significance
   - Client-server architecture

4. **Concurrent Programming**
   - Threading for handling multiple clients
   - Thread-safe operations
   - Resource management

5. **Cloud Deployment**
   - Binding to network interfaces
   - Security group configuration
   - Container orchestration

## 🔗 Use Cases

### Microservices
- Service-to-service communication
- Health check endpoints
- Metric collection

### IoT Systems
- Sensor data collection (UDP)
- Device management (TCP)
- Real-time monitoring

### Data Pipelines
- Log aggregation
- Stream processing
- Event-driven architectures

### APIs & Web Services
- RESTful APIs
- WebSocket servers
- Real-time notifications

## 📚 Further Reading

- [RFC 791 - Internet Protocol](https://tools.ietf.org/html/rfc791)
- [RFC 793 - TCP](https://tools.ietf.org/html/rfc793)
- [RFC 768 - UDP](https://tools.ietf.org/html/rfc768)
- [Python Socket Documentation](https://docs.python.org/3/library/socket.html)
- [AWS VPC Networking](https://docs.aws.amazon.com/vpc/)

## 🤝 Contributing

Feel free to fork, modify, and use this code for learning or production purposes!

## 📄 License

MIT License - Free to use and modify

---

**Author:** Gaffar Ahmed Mohammed 
**LinkedIn:** [Your Profile URL]  
**GitHub:** [Your GitHub]  
**Date:** February 2026

**#Python #NetworkProgramming #CloudComputing #DevOps #SocketProgramming #AWS #Azure #GCP #Kubernetes #Docker**
