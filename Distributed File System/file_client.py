import socket
import os

class FileClient:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))

    def upload_file(self, filename):
        if os.path.exists(filename):
            self.client_socket.send(f"UPLOAD {filename} {os.path.getsize(filename)}".encode())
            with open(filename, 'rb') as f:
                bytes_read = f.read(1024)
                while bytes_read:
                    self.client_socket.send(bytes_read)
                    bytes_read = f.read(1024)
            print(f"{filename} uploaded successfully.")
        else:
            print("File does not exist.")

    def download_file(self, filename):
        self.client_socket.send(f"DOWNLOAD {filename}".encode())
        response = self.client_socket.recv(1024).decode()
        if response.startswith("EXISTS"):
            filesize = int(response.split()[1])
            with open(filename, 'wb') as f:
                bytes_received = 0
                while bytes_received < filesize:
                    data = self.client_socket.recv(1024)
                    f.write(data)
                    bytes_received += len(data)
            print(f"{filename} downloaded successfully.")
        else:
            print("File not found on server.")

    def close(self):
        self.client_socket.close()

if __name__ == "__main__":
    client = FileClient()
    while True:
        command = input("Enter command (upload/download/exit): ")
        if command == "upload":
            filename = input("Enter filename to upload: ")
            client.upload_file(filename)
        elif command == "download":
            filename = input("Enter filename to download: ")
            client.download_file(filename)
        elif command == "exit":
            break
        else:
            print("Invalid command.")
    client.close()