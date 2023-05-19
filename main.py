from requests import get
from requests import post
from decouple import config

try:
    f = open('ipAddress.txt', 'r')
    prevIpAddress = f.read()
    f.close()
    currentIpAddress = get('https://api.ipify.org').content.decode('utf8')
    if prevIpAddress == currentIpAddress:
        exit
    else:
        url = "https://notify-api.line.me/api/notify" 
        token = config('TOKEN')
        headers = {"Authorization" : "Bearer "+ token} 
        message =  "IP address has changed recently:" + currentIpAddress
        payload = {"message" :  message} 
        r = post(url, headers = headers, params=payload)
        f = open('ipAddress.txt', 'w')
        f.write(currentIpAddress)
        f.close()
except Exception as err:
    print("error occurred")
    print(err)
exit