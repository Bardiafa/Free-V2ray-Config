import requests
import os
import base64

open("vmess.txt", "w").close()
open("vless.txt", "w").close()
open("trojan.txt", "w").close()
open("ss.txt", "w").close()
open("ssr.txt", "w").close()

vless = ""
trojan = ""
ss = ""
ssr = ""
respnse = requests.get("https://github.com/hossein-mohseni/Free-V2ray-Config/blob/main/configs.txt").text
for config in respnse.splitlines():
    if config.startswith("vmess"):
        open("vmess.txt", "a").write(config + "\n")     
    if config.startswith("vless"):
        vless += config + "\n"  
    if config.startswith("trojan"):
        trojan += config + "\n"   
    if config.startswith("ss"):   
        ss += config + "\n"
    if config.startswith("ssr"):
        ssr += config + "\n"
 
open("vless.txt", "w").write(base64.b64encode(vless.encode("utf-8")).decode("utf-8"))  
print("vless sorted")
open("trojan.txt", "w").write(base64.b64encode(trojan.encode("utf-8")).decode("utf-8"))  
print("trojan sorted")
open("ss.txt", "w").write(base64.b64encode(ss.encode("utf-8")).decode("utf-8"))  
print("ss sorted")
open("ssr.txt", "w").write(base64.b64encode(ssr.encode("utf-8")).decode("utf-8"))  
print("ssr sorted")
