import ssl
import socket

def print_ssl_handshake_and_cert_location(hostname, port=443):
    # Create a default SSL context
    context = ssl.create_default_context()

    # Retrieve the trusted certificates
    certs = context.get_ca_certs()

    # Print the information about the trusted certificates
    if certs:
        print("Trusted certificates used by the SSL context:")
        for cert in certs:
            print(f"  - Subject: {cert.get('subject')}")
            print(f"    Issuer: {cert.get('issuer')}")
            print(f"    Expire: {cert.get('notAfter')}\n")
    else:
        print("No CA certificates found.")

    # Connect to the server and initiate the SSL handshake
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssl_sock:
            # Perform the SSL handshake
            ssl_sock.do_handshake()

            # Print SSL handshake details
            print("\nSSL Handshake completed.")
            print(f"SSL Version: {ssl_sock.version()}")
            print(f"Cipher: {ssl_sock.cipher()}")
            print(f"Server certificate:\n{ssl_sock.getpeercert()}")

if __name__ == "__main__":
    hostname = "www.google.com"  # Change this to any server you want to connect to
    print_ssl_handshake_and_cert_location(hostname)
