#zabbix-lib


#### 1. 配置登陆

```
mv config/{login.yaml-example,login.yaml}
vim  config/login.yaml 
```

#### 2. py Sample

```
import sys
sys.path.append("./zabbix-lib")
from zapi import ZabbixTool

zabbix=ZabbixTool()

print zabbix.get()
```
