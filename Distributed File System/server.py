import socket
import threading
import os

class FileServer:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server started at {self.host}:{self.port}")

    def handle_client(self, client_socket):
        while True:
            request = client_socket.recv(1024).decode()
            if not request:
                break

            command, *args = request.split()
            if command == 'UPLOAD':
                filename = args[0]
                filesize = int(args[1])
                with open(filename, 'wb') as f:
                    bytes_received = 0
                    while bytes_received < filesize:
                        data = client_socket.recv(1024)
                        f.write(data)
                        bytes_received += len(data)
                print(f"{filename} uploaded successfully.")
            elif command == 'DOWNLOAD':
                filename = args[0]
                if os.path.exists(filename):
                    client_socket.send(f"EXISTS {os.path.getsize(filename)}".encode())
                    with open(filename, 'rb') as f:
                        bytes_read = f.read(1024)
                        while bytes_read:
                            client_socket.send(bytes_read)
                            bytes_read = f.read(1024)
                    print(f"{filename} downloaded successfully.")
                else:
                    client_socket.send(b"NOT FOUND")
            else:
                print("Invalid command.")

        client_socket.close()

    def run(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Connection from {addr}")
            client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_handler.start()

if __name__ == "__main__":
    server = FileServer()
    server.run()