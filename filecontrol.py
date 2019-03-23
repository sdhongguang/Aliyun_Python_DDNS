#! /usr/bin/env python
# coding=utf-8
import os


# 检查获得的ip地址是否和文件中相同，如果没有文件，就建立文件
def ip_file_verify(ip):
    try:
        fr = open('ipAddress')
        fr_read = fr.readline()
        fr.close()

        if len(fr_read) <= 0 or ip != fr_read:

            return True
        else:

            return False

    except FileNotFoundError:
        os.mknod('ipAddress')
        ip_file_update(ip)
        return True


def ip_file_update(ip):
    try:
        fw = open('ipAddress', mode='w')
        fw.writelines(ip)
        fw.close()
    except Exception as result:
        print("未知错误 ", result)


if __name__ == '__main__':

    print(ip_file_verify('120.130.11.23'))
