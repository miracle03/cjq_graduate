from socket import *

import datetime as datetime
import pymysql
import datetime
import md5
import time
import os
from multiprocessing import Process
import threading
threads = []
print("请输入服务器IP地址")
ip = input()
def insert_result(ip, path, filename):
    ip = ip.replace(".", "_", 3)
    db = pymysql.connect("169.254.252.154", "root", "981911", "md5_c")
    dt = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = f"insert into result \
                  values (%s,%s,%s,%s)" % ( "'" + ip + "'", "'" + path + "'", "'" + filename + "'" \
                                                               ,"'"+dt+"'")

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表

    except:
        print("Error: unable to fecth data")

    # 关闭数据库连接
    db.close()

def check():
    client = socket()
    ip_port = (ip, 8080)
    client.connect(ip_port)
    print("请输入检查目录及方法(以.分界。m代表MD5检查，s代表时间检查")
    path = input()

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

        for i in change_list_l[0:-1]:
            md5.insert_result(ip,path1,i)
            #print(i)
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
if __name__ == '__main__':
    result = md5.display_dir(ip)
    print("当前服务器文件目录为")
    md5.print_all(result)



        # p = Process(target=check, args=(path,))
        # p.start()
    check()
