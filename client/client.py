"""
TCP client for the mini-federado system.

Connects to the aggregator and sends a single identifying message
before exiting. In a federated learning architecture, this represents
a client node reporting in to the aggregator.

Author: Paulo Padilla Domingues
Project: mini-federado
"""
import socket
import time
import os

def main() -> None:
	"""Connect to the aggregator, send an identifying message, and exit.

	Waits a few seconds before connecting to give the aggregator
	time to start listening (a naive workaround for container
	startup ordering).
	"""

	time.sleep(3)
	client_name = os.environ.get("CLIENT_NAME", "unknown-client")

	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(("aggregator", 9000))
	client.send(f"Hello from {client_name}".encode())
	client.close()
	print(f"{client_name}: message sent")

if __name__ == "__main__":
	main()