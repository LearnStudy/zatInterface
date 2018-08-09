#coding = utf-8

import requests
import json
import paramiko

class tools:
    def __init__(self):
        self.host = ''
        self.uri = ''#从接口文档中调用过来的端口+uri

    def send(self,url, methord, param):
        print (url)
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        if methord =="post":
            response = requests.post(url,data= param,verify = False,headers=self.header,auth=("###admin###", "%%%zdns%%%"))
            is_ok = response.status_code
            print (response.status_code)
            if is_ok == 200:
                return "pass"
            else:
                return "flase to run!!!!!!!!"

        elif methord =="get":
            response = requests.get(url, data = param, verify = False,headers=self.header,auth=("###admin###", "%%%zdns%%%"))
            is_ok = response.status_code
            if is_ok ==200:
                return pass
            else:
                return is_ok

        elif methord == "put":
            response = requests.put(url, data = param,verify = False,headers=self.header , auth=("###admin###", "%%%zdns%%%"))

            is_ok = response.status_code
            if is_ok ==200:
                return pass
            else:
                return is_ok

        else:
            #methord  == "delete"

            response = requests.delete(url,data = param,headers=self.header, verify = False, auth=("###admin###", "%%%zdns%%%"))

            is_ok = response.status_code
            if is_ok ==200:
                return pass
            else:
                return is_ok


#远程执行命令
    def remote(self):
        pass
