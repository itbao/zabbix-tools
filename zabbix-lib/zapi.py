#!/bin/env python
#coding=utf-8
#
#Written by Xu Changbao
#Date 20150904

import json
import urllib2
import yaml
import json
import random
import sys
import re
import os



class ZabbixTool:
    def __init__(self):
        self.login_yaml=open('./config/login.yaml')
        self.login_dict=yaml.load(self.login_yaml)
        self.url=self.login_dict.pop('login_url')
        self.send={"jsonrpc": "2.0","auth":self.user_login(),"id": random.randint(100, 999)}

    def user_login(self):
        data=json.dumps(self.login_dict,indent=4)
        request=urllib2.Request(self.url,data)
        request.add_header('Content-Type','application/json')
        response=urllib2.urlopen(request)
        result=json.loads(response.read())
        auth_id=result['result']
        return auth_id

    def zabbix_request(self,send_dict,retries=10):
        try:
            if retries >= 1:
                data=json.dumps(send_dict,indent=4)
                request=urllib2.Request(self.url,data)
                request.add_header('Content-Type','application/json')
                response=urllib2.urlopen(request)
                result=json.loads(response.read())
                return result
        except:
                self.zabbix_request(send_dict,retries-1)


    def get(self,filter_dict=False,method='host.get',output_list=['output'],params_dict=False):
        params={'output':'extend'}
        for out in output_list: params.update({out:'extend'})
        if filter_dict: params.update({"filter":filter_dict})
        if params_dict: params.update(params_dict)
        send=self.send
        send.update({'method': method})
        send.update({'params':params})
        #print json.dumps(send)
        return self.zabbix_request(send_dict=send)
