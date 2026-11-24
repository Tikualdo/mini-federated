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

def read_local_dataset_info() -> str:
	"""Read this node's local dataset description from the mounted volume.

    Returns:
			The contents of /data/info.txt, or a placeholder string if the
			file is missing.
    """
	path = "/data/info.txt"
	if not os.path.exists(path):
		return "no dataset found"
	with open(path, "r") as file:
		return file.read().strip()


def main() -> None:
	"""Connect to the aggregator, send an identifying message, and exit.

	Waits a few seconds before connecting to give the aggregator
	time to start listening (a naive workaround for container
	startup ordering). The message includes this node's local
  dataset description, read from its mounted volume.
	"""

	time.sleep(3)
	client_name = os.environ.get("CLIENT_NAME", "unknown-client")
	dataset_info = read_local_dataset_info()

	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(("aggregator", 9000))
	client.send(f"Hello from {client_name}, dataset: {dataset_info}".encode())
	client.close()
	print(f"{client_name}: message sent")

if __name__ == "__main__":
	main()