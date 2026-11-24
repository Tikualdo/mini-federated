"""
TCP aggregator for the mini-federado system.

Listens for incoming client connections and logs the message each
client sends. In a federated learning architecture, this is the role
of the central aggregator: receiving updates from client nodes to
later combine them (e.g. via FedAvg).

Author: Paulo Padilla Domingues
Project: mini-federado
"""
import socket

def main() -> None:
  """Start the TCP server and process incoming client messages forever.

  Binds a socket to all network interfaces on port 9000, accepts
  connections one at a time, and prints whatever message each
  client sends before closing that connection.
  """

  print("Aggregator waiting for connections...")
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind(("0.0.0.0", 9000))
  server.listen(5)

  while True:
    connection, address = server.accept()
    message = connection.recv(1024).decode()
    print(f"Received message: {message}")
    connection.close()

if __name__ == "__main__":
  main()


