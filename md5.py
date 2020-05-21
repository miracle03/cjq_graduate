# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Time: 17-11-29 下午10:26
# Author: sty
# File: compare_file.py
import datetime
import hashlib
import os
import socket
import pymysql


# file_1 = r'C:\Users\Administrator\Desktop\graduate\开题报告陈锦前.docx'
# file_2 = r'C:\Users\Administrator\Desktop\graduate\开题报告陈锦前 - Copy.docx'

def string_md5(value):
    m = hashlib.md5()
    m.update(value.encode('UTF-8'))
    return m.hexdigest()

def get_file_md5(f):
    m = hashlib.md5()
    while True:
        data = f.read(4096)  # 将文件分块读取
        if not data:
            break
        m.update(data)
    return m.hexdigest()
def create_table(ip):
    ip = ip.replace(".","_",3)
    db = pymysql.connect("169.254.252.154", "root", "981911", "md5_c")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句


    sql = f"create table  %s \
             ( location varchar(100) ,filename varchar (100) ,\
             md5 varchar (255),filesize varchar (255),\
             changedtime varchar (255),\
                primary  key(location,filename));" % (ip)
    try:

       cursor.execute(sql)
        # 获取所有记录列表
    except:
        print("Error:existed table")

    db.close()


# file_a = input()
# file_b = input()
def md5_insert(location, filename, ip):
    file_1 = location + '/' + filename

    with open(file_1, 'rb') as f1:
        file1_md5 = get_file_md5(f1)
        db = pymysql.connect("169.254.252.154", "root", "981911", "md5_c")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = f"insert into %s \
               values (%s,%s,%s,%s,%s)" % (ip, "'" + location + "'", "'" + filename + "'", "'" + file1_md5 + "'" \
                                                               , str(os.path.getsize(file_1)), \
                                           str(os.path.getctime(file_1)))

        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表

        except:
            print("Error: unable to fecth data")

        # 关闭数据库连接
        db.close()


def md5_update(location, filename, ip):
    file_1 = location + '/' + filename
    with open(file_1, 'rb') as f1:
        file1_md5 = get_file_md5(f1)
        db = pymysql.connect("169.254.252.154", "root", "981911", "md5_c")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = f"update %s \
                 set md5 = %s,filesize = %s,changedtime = %s  \
             where location like %s and filename like %s" % ( \
              ip, "'" + file1_md5 + "'", "'" + str(os.path.getsize(file_1)) + "'", \
                "'" + str(os.path.getctime(file_1)) + "'", "'" + location + "'", "'" + filename + "'")

        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表

        except:
            print("Error: unable to fecth data")

        # 关闭数据库连接
        db.close()


def display_dir(ip):
    db = pymysql.connect("localhost", "root", "981911", "md5_c")
    ip = ip.replace(".", "_", 3)
    dir = []
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = f"select distinct location from %s \
                   " % (ip)

    try:
        # 执行SQL语句
        cursor.execute(sql)

        # 获取所有记录列表
        result = cursor.fetchall()
        for row in result:
            dir.append(row[0])
        return dir



    except:
        print("Error: unable to fecth data")

    # 关闭数据库连接
    db.close()


def md5_compare(location, filename, list, ip):
    file_1 = location + '/' + filename
    with open(file_1, 'rb') as f1:
        file1_md5 = get_file_md5(f1)
        db = pymysql.connect("169.254.252.154", "root", "981911", "md5_c")

        # 使用cursor()方法获取操作游标
        cursor = db.cursor()
        # SQL 查询语句
        sql = f"select md5 from %s \
                where location like %s and filename like %s" % (ip, "'" + location + "'", "'" + filename + "'")

        try:
            # 执行SQL语句
            cursor.execute(sql)

            # 获取所有记录列表
            result = cursor.fetchall()
            for row in result:
                file2_md5 = row[0]
            if file1_md5 == file2_md5:
                i = 0
            else:
                # print("file: "+filename+" has changed")
                list.append(filename)


        except:
            print("Error: unable to fecth data")

        # 关闭数据库连接
        db.close()


def sizetime_compare(location, filename, list, ip):
    file_1 = location + '/' + filename

    file1_size = str(os.path.getsize(file_1))
    file1_time = str(os.path.getctime(file_1))
    db = pymysql.connect("169.254.252.154", "root", "981911", "md5_c")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL 查询语句
    sql = f"select filesize,changedtime from %s \
                where location like %s and filename like %s" % (ip, "'" + location + "'", "'" + filename + "'")

    try:
        # 执行SQL语句
        cursor.execute(sql)

        # 获取所有记录列表
        result = cursor.fetchall()
        for row in result:
            file2_size = row[0]
            file2_time = row[1]

        if file2_size == file1_size and file1_time == file2_time:
            i = 0
        else:
            list.append(filename)

    except:
        print("Error: unable to fecth data")

    # 关闭数据库连接
    db.close()


def delete_substr_method2(in_str, in_substr):
    start_loc = in_str.find(in_substr)
    len_substr = len(in_substr)
    res_str = in_str[:start_loc] + in_str[start_loc + len_substr:]
    return res_str


def dir_md5_compare(path, ip):
    ip = ip.replace(".", "_", 3)
    file_result = get_file_name_list(path)

    i = 0
    changelist = []
    for name in file_result:
        md5_compare(path, name, changelist, ip)

    changelist.append(str(len(file_result)))
    return changelist

def dir_sizetime_compare(path, ip):
    file_result = get_file_name_list(path)
    ip = ip.replace(".", "_", 3)
    i = 0
    changelist = []
    for name in file_result:
        sizetime_compare(path, name, changelist, ip)

    changelist.append(str(len(file_result)))
    return changelist


def dir_md5_insert(path, ip):
    ip = ip.replace(".", "_", 3)
    file_result = get_file_name_list(path)
    for name in file_result:
        md5_insert(path, name, ip)


def dir_md5_update(path, ip):
    file_result = get_file_name_list(path)
    ip = ip.replace(".", "_", 3)
    for name in file_result:
        md5_update(path, name, ip)


def get_file_name_list(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files


def get_dir_name_list(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return dirs


def print_all(list):
    for name in list:
        print(name)


def get_size(location, filename):
    file_1 = location + '\\' + filename
    return os.path.getsize(file_1)


def get_time(location, filename):
    file_1 = location + '\\' + filename
    return os.path.getmtime(file_1)
def list_to_string(list):
    s=""
    for i in list:
        s=s+i+","
    return s
def sring_to_list(string):
    s = string.split(",")
    s_1 = s[0:-1]
    return s_1
def get_ip():
    myname = socket.getfqdn(socket.gethostname())
    ip = socket.gethostbyname(myname)
    return  ip
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
# path: str = input()
# path = path.replace("\\", "/")
# myname = socket.getfqdn(socket.gethostname())
# ip = socket.gethostbyname(myname)
# # print(a)
# # print(b)
# #dir_md5_insert(path, ip)
# # dir_md5_update(path,ip)
# a=dir_md5_compare(path,ip)
# print_all(a)
# a_s=list_to_string(a)
# print(a_s)
# a_l=sring_to_list(a_s)
# for i in a_l[0:-1]:
#     print(i)



#result = display_dir(ip)
#print_all(result)
# dir_sizetime_compare(path,ip)
# print(str(os.path.getsize(path)))
# file_result=get_file_name_list(path)
# print_all_files(file_result)
# sizetime_compare(b,a)
# md5_update(b, a )
# dir_name=get_dir_name_list(path)
# print_all_files(dir_name)
