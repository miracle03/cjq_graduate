# coding:utf-8
from socket import *
from multiprocessing import Process
import _thread;

import time  # 导入time模块
import md5
import msvcrt
import time
from goto import with_goto

key = "f1c1e25b079d45b7962a9e34772633f5"

server = socket()
ip_port = ("169.254.252.154", 80)
server.bind(ip_port)
server.listen(5)

def talk(conn, addr):
    while 1:
        try:
            receive_data = conn.recv(1024)
            print(receive_data)
            if not receive_data: break
            recv = bytes.decode(receive_data)
            print(recv)
            recv_l = recv.split(",")
            method = recv_l[1]
            rev_path = recv_l[0]
            if method == "m":
                change_list = md5.dir_md5_compare(rev_path, "169.254.252.154")
                change_list_s = md5.list_to_string(change_list)
                change_list_b = str.encode(change_list_s)
                conn.send(change_list_b)
            if method == "s":
                change_list = md5.dir_sizetime_compare(rev_path,"169.254.252.154")
                change_list_s = md5.list_to_string(change_list)
                change_list_b = str.encode(change_list_s)
                conn.sendto(change_list_b)

        except Exception:
            break


def main():
    print("1、添加目录 2、更新目录")
    a = input()
    if a == "1":
        print("输入想要添加的文件夹目录")
        path = input()
        path = path.replace("\\", "/")
        md5.dir_md5_insert(path, "169.254.252.154")
        with_goto(main())
    if a == "2":
        print("请输入密码：")
        key_1 = input()
        if (md5.string_md5(key_1) == key):
            print("输入想要更新的文件夹目录")
            path = input()
            path = path.replace("\\", "/")
            md5.dir_md5_update(path, "169.254.252.154")
            with_goto(main())
        else:
            print("密码错误")
            with_goto(main())


def listen():


    while 1:
        conn, client_addr = server.accept()
        print(conn, client_addr)
        p = Process(target=talk, args=(conn, client_addr))
        p.start()


md5.create_table("169.254.252.154")
#_thread.start_new_thread(main, ());
listen()
