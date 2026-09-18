import socket

def forward_dns_lookup(domain_name):
    try:
        # Get the IP address for the domain name
        ip_address = socket.gethostbyname(domain_name)
        print(f"Domain: {domain_name}")
        print(f"IP Address: {ip_address}")
    except socket.gaierror as e:
        # Handle cases where the domain name cannot be resolved
        print(f"Error: Unable to resolve '{domain_name}': {e}")

if __name__ == "__main__":
    # Example usage
    hostname = input("Enter a domain name (e.g., google.com): ")
    forward_dns_lookup(hostname)
