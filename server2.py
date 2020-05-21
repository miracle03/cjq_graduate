from socket import *
import md5
import time
import threading
threads = []
print("请输入服务器IP地址")
ip = input()

def check():
    client = socket()
    ip_port = (ip, 8080)
    client.connect(ip_port)
    result = md5.display_dir(ip)
    print("当前服务器文件目录为")
    md5.print_all(result)
    path = input("请输入检查目录及方法(以.分界。m代表MD5检查，s代表时间检查>>>:").strip()
    path1 = path.split(".")[0]
    path2 = path.split(".")[1]
    while 1:

        path_b_1 = str.encode(path1)
        path_b_2 = str.encode(path2)
        client.send(path_b_1)
        client.send(path_b_2)
        change_list_b = client.recv(1024)
        # print(change_list_b)
        change_list_s = bytes.decode(change_list_b)
        change_list_l = md5.sring_to_list(change_list_s)
        print("共检查" + change_list_l[-1] + "个文件，" + str(len(change_list_l) - 1) + "个文件发生改变：")
        for i in change_list_l[0:-1]:
            print(i)
        time.sleep(1)

# t1 = threading.Thread(target=check)
# threads.append(t1)
# t2 = threading.Thread(target=check2)
# threads.append(t2)
# if __name__=='__main__':
#     for t in threads:
#         t.start()
#     for t in threads:
#         t.join()
# print ("退出线程")
check()