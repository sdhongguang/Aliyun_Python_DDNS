#! /usr/bin/env python
# coding=utf-8
import os
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import json
from filecontrol import *
import account


def get_ip(): #获取ip
    get_ip = os.popen('(curl -s http://txt.go.sohu.com/ip/soip) | grep -P -o -i "(\d+.\d+.\d+.\d+)"')
    ip = get_ip.read()
    print ("get_ip is running, got_ip is %s" % ip)
    return ip


# print(type(get_ip()))
# print(get_ip())


def get_record(): #获取阿里云的DNS信息
    client = AcsClient(account.ak, account.sc, 'default')
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('alidns.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https') # https | http
    request.set_version('2015-01-09')
    request.set_action_name('DescribeSubDomainRecords')
    request.add_query_param('SubDomain', account.SubDomain)
    response = client.do_action(request)
    # python2: print(response)
    record = json.loads(response.decode())
    print("get_record is running, record_ip is %s" % record['DomainRecords']['Record'][0]['Value'])
    # 提取并返回阿里云的DNS信息，列表格式
    return record['DomainRecords']['Record']


# if __name__ == '__main__':
#     print(get_record())


def change_record(ip): # 解析DNS的ip地址，传入本地公网IP地址
    client = AcsClient(account.ak, account.sc, 'default')
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('alidns.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2015-01-09')
    request.set_action_name('UpdateDomainRecord')
    request.add_query_param('RecordId', got_record[0]['RecordId'])
    request.add_query_param('RR', got_record[0]['RR'])
    request.add_query_param('Type', 'A')
    request.add_query_param('Value', ip)
    response = client.do_action(request)
    # python2: print(response)
    print("change_record is running,")
    return response
    # print(str(response, encoding='utf-8'))


got_ip = get_ip()
# print(filecontrol.ip_file_verify(got_ip))
ip_not_confirm = ip_file_verify(got_ip)
# print(ip_not_confirm)
if ip_not_confirm:    #如果获取到的IP地址和 文件中记载的IP地址不符。
    got_record = get_record()    # 获取DNS解析信息
    # print(type(got_record[0]['Value']))
    if got_ip != got_record[0]['Value']:    # 将获取的本地公网IP 与DNS解析对比，如果不符。
        change_record(got_ip)    # 更新DNS解析
        ip_file_update(got_ip)    # 将获取的本地公网IP 写入文件，留作下次对比
        print("OriginalIP is %s" % got_record[0]['Value'])
        print("ChangedIP is %s" % got_ip)





