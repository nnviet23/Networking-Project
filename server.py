import socket
import threading

HOST = '127.0.0.1'
PORT = 12345
ADDR = (HOST, PORT)
FORMAT = 'utf8'

def sendFile(filename, conn: socket):
    with open(filename, "rb") as file:
        data = file.read()
        conn.sendall(data)

def handleClient(conn: socket, addr):
    print("Client address: ", addr)
    print("conn: ", conn.getsockname())
    file_list = []
    with open("text.txt", "r") as file:
        for line in file:
            filename = line.strip()
            a = filename.split()
            b, d = map(str, a)
            file_list.append(b)
        filename_STR = "\n".join(file_list)
        conn.sendall(filename_STR.encode(FORMAT))
    
    msg = None
    while msg != "x":
        msg = conn.recv(1024).decode(FORMAT)
        if msg:
            for line in file_list:
                if line.lower().startswith(msg.lower()):
                    sendFile(line, conn)
        else:
            break
    print("Client", addr, "finished")
    conn.close()

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(ADDR)
    s.listen(5)  # accept 5 clients

    print("SERVER SIDE")
    print("Server: ", ADDR)
    print("Waiting for client")
    
    nClient = 0
    while nClient <= 1:
        try:
            c, a = s.accept()
            thr = threading.Thread(target=handleClient, args=(c, a))
            thr.daemon = True
            thr.start()
        except Exception as e:
            print(f"Error: {e}")
        
        nClient += 1

    s.close()
    input()

if __name__ == "__main__":
    main()