#!/bin/env python
#coding=utf-8
#
#Written by Xu Changbao

import sys
sys.path.append("./zabbix-lib")

from docopt import docopt
from zabbixHost import host_list


if __name__ == "__main__":
    zabbix_host_list=host_list()
    print zabbix_host_list
