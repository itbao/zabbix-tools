#!/bin/env python
#coding=utf-8
#
#Written by Xu Changbao
#Date 20150813

import json
import os
import sys
sys.path.append("./zabbix-lib")

from docopt import docopt
from zapi import ZabbixTool


zabbix=ZabbixTool()

def host_list():
    host_list={}
    host_status={}
    hosts_info=zabbix.get(method='host.get',output_list=['selectInterfaces'])
    for host in hosts_info['result']:
        host_name=host['host']
        if host['status'] == '0' :
            status="on"
        else:
            status="off"
        host_status={'host_name':host_name,'host_status':status}
        host_ip=host['interfaces'][0]['ip']
        host_list.update({host_ip:host_status})
    return host_list

def host_list_download_yaml():
    os.system('echo --- > data/uoshost.yml')
    hosts_info=zabbix.get(method='host.get',output_list=['selectInterfaces'])
    uoshost=file('data/uoshost.yml','a+')
    for host in hosts_info['result']:
        name=host['host']
        ip=host['interfaces'][0]['ip']
        if host['status'] == '0' :
            status="on"
        else:
            status="off"
        uoshost.write("- Host name: " + name  + '\n')
        uoshost.write("  ip: " + ip  + '\n')
        uoshost.write("  status: " + status + "\n")
    print "plese view to data/uoshost.yml ...."
    uoshost.close()

if __name__ == "__main__":
    pass
