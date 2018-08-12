#coding = utf-8

from requests import Request
import json
import paramiko

class tools:
    def __init__(self,func):
        self.host = ''
        self.uri = ''#从接口文档中调用过来的端口+uri

    def __call__(self,url, methord, param):
        print (url)
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        if methord =="post":
            response = requests.post(url,data= param,verify = False,headers=self.header,auth=("###admin###", "%%%zdns%%%"))
            is_ok = response.status_code
            print (response.status_code)
            if is_ok == 200:
                return "pass"
            else:
                return "fail"

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



class sendRequest:

    """
    被修饰函数需要构造出需要的参数param
    被装饰函数传：
    “methord”：接口文档获取
    "uri"：接口文档获取，对于需要在uri中定义视图，区的需要用*标识，以便替换
    "参数" ：方法自己构造

    """


    def __init__(self,func):
        self._func = func
        self.header = 'header'


    def __call__(self, *args, **kwargs):
        params = self._func()
        methord = params['methord']
        uri = params['uri']
        param = params['param']
        response = requests(methord,uri, data = param, verify = False,header = self.header,auth = ("###admin###", "%%%zdns%%%"))
        return response

    def postRequest(self,*args,**kwargs):
        uri = kwargs[uri]
        params = kwargs[params]
        res = requests.post(uri, data = )

    def putRequest(self,*args,**kwargs):
        pass

    def getRequest(self,*args,**kwargs):
        pass

    def delRequest(self,*args,**kwargs):
        pass


# #远程执行命令
#     def remote(self):
#         pass


requests()




