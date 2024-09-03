import ssl
import socket
import sys

def ssl_trace(hostname, port):
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE  # Disable certificate verification for testing

    # Create a TCP/IP socket
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            print(f"SSL established. Peer: {ssock.getpeercert()}")
            print(f"Cipher: {ssock.cipher()}")
            print(f"SSL version: {ssock.version()}")

def main():
    if len(sys.argv) < 3:
        print("Usage: python ssl_trace.py <hostname> <port>")
        sys.exit(1)

    hostname = sys.argv[1]
    port = int(sys.argv[2])

    # Trigger the SSL handshake and trace it
    ssl_trace(hostname, port)

if __name__ == "__main__":
    main()
