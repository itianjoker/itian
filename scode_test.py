import requests
url ='https://abc.go.kr/waitingroom/clear.html'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
html = requests.get(url, headers = headers).text
print(html)
#error_server = open('/var/tmp/nirs.log', 'a')
#error_server.write(html)
#error_server.write("\n")
#error_server.close()
f = open("nirs.log", "a")
f.write("Update Python")
f.close()
 
