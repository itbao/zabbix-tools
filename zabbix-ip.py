#!/bin/env python
#coding=utf-8
#
#Written by Xu Changbao
#Date 20150813

import json
import os

import sys
sys.path.append("./zabbix-lib")

from zapi import ZabbixTool


zabbix=ZabbixTool()

hosts_info=zabbix.get(method='host.get',output_list=['selectInterfaces'])

hosts = {}
for host in hosts_info['result']:
    name=host['host']
    ip=host['interfaces'][0]['ip']
    status=host['status']
    hostid=host['hostid']
    print {"hostname": name, "ip":ip, "hostid":hostid, "status":status}

