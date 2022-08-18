import requests

rex = requests.get()
rex = requests.post()
rex = requests.request()

url = "https://test-newapi.shoplus.net/api/v1/user/ocean/email/register"
payload = ""



print(rex.status_code)#返回状态码
print(rex.reason)
print(rex.headers)
print(rex.text)