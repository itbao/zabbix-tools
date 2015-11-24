#!/bin/env python
#coding=utf-8
#
#Written by Xu Changbao
#Date 20150813

#import json
#import urllib2
#import argparse
#import yaml
import json
#import random
#import sys
#import re
import os

import sys
sys.path.append("./zabbix-lib")

from docopt import docopt
from zapi import ZabbixTool


zabbix=ZabbixTool()


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



#    def host_get(self,filter_dict=False,method='host.get',output_list=['output']):
#
#        params={'output':'extend'}
#        for out in output_list: params.update({out:'extend'})
#
#        if filter_dict: params.update({"filter":filter_dict})
#
#        send=self.send
#        send.update({'method': method})
#        send.update({'params':params})
#        return self.zabbix_request(send_dict=send)
#
#    def host_update(self,hostid,groupid_list=False,host_name=False,status=False):
#        send=self.send
#        send.update({"method": "host.update"})
#        params={'hostid':hostid}
#        
#        if groupid_list:
#            groups=[ {"groupid":i} for i in groupid_list ]
#            params.update({'groups':groups})
#        if status: params.update({'status':status})
#
#        send.update({'params':params})
#        result=self.zabbix_request(send_dict=send)
#
#        if  result.has_key('error'):
#            print result['error']['data']
#        else:
#            if host_name:
#                print "%s update succeed" % (host_name)
#            else:
#                print "%s update succeed" % (hostid)
#
#
#
#
#
#
#def host_download():
#    os.system('echo --- > uoshost.yml')
#    hosts_info=zabbix.get(method='host.get',output_list=['selectInterfaces'])
#
#    uoshost=file('uoshost.yml','a+')
#    for host in hosts_info['result']:
#        name=host['host']
#        ip=host['interfaces'][0]['ip']
#        if host['status'] == '0' :
#            status="on"
#        else:
#            status="off"
#        uoshost.write("- Host name: " + name  + '\n') 
#        uoshost.write("  ip: " + ip  + '\n') 
#        uoshost.write("  status: " + status + "\n")
#
#    print "plese view to uoshost.yml ...."
#    uoshost.close()
#
#
#def host_upload():
#    host_yaml=open('uoshost.yml')
#    hosts=yaml.load(host_yaml)
#    #print json.dumps(hosts,indent=4)
#
#    for host in hosts:
#        name=host['Host name']
#        if host['status'] == True :
#            status="0"
#        else:
#            status="1"
#        
#        filter={"host":name}
#        host_info=zabbix.get(filter_dict=filter,method='host.get',output_list=['output'])
#        if host_info['result']:
#            host_id=host_info['result'][0]['hostid']
#            zabbix.host_update(hostid=host_id,status=status)
#        else:
#            print 'not find a',name
#
#
