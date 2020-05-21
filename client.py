# coding:utf-8
from socket import *
from multiprocessing import Process
import md5
ip=md5.get_ip()
def talk(server_socket):
    while 1:
        try:
            receive_path = server_socket.recv(1024)
            rev_path = bytes.decode(receive_path)
            #print(rev_path)
            receive_method = server_socket.recv(1024)
            rev_method = bytes.decode(receive_method)
            #print(rev_method)

            if rev_method == "m":
                change_list = md5.dir_md5_compare(rev_path, ip)
                change_list_s = md5.list_to_string(change_list)
                change_list_b = str.encode(change_list_s)
                server_socket.send(change_list_b)
            if rev_method == "s":
                change_list = md5.dir_sizetime_compare(rev_path, ip)
                change_list_s = md5.list_to_string(change_list)
                change_list_b = str.encode(change_list_s)
                server_socket.send(change_list_b)
            if not receive_path : break

        except Exception:
            break


if __name__ == '__main__':
    print("主进程开始.")
    server = socket()
    ip_port = (ip, 8080)
    server.bind(ip_port)
    server.listen(5)
    while 1:
        conn, client_addr = server.accept()
        print(conn, client_addr)
        p = Process(target=talk, args=(conn,))
        p.start()