
# coding:utf-8
from socket import *
import os
import time
import md5
PORT = 80
print("请输入服务器IP地址")
ip = input()
client = socket()
ip_port = (ip, 80)
client.connect(ip_port)
while 1:
    result = md5.display_dir(ip)
    print("当前服务器文件目录为")
    md5.print_all(result)
    print("请输入检查目录及方法(以，分界。m代表MD5检查，s代表时间检查)")
    path = input()
    path_b = str.encode(path)

    client.send(path_b)
    change_list_b = client.recv(1024)
    change_list_s = bytes.decode(change_list_b)
    change_list_l = md5.sring_to_list(change_list_s)
    print("共检查" + change_list_l[-1] + "个文件，" + str(len(change_list_l) - 1) + "个文件发生改变：")


client.close()