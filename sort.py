import requests
import os
import base64

ptt =  os.path.dirname(__file__)
vmess_file = os.path.join(ptt, 'vmess.txt')
vless_file = os.path.join(ptt, 'vless.txt')
trojan_file = os.path.join(ptt, 'trojan.txt')
ss_file = os.path.join(ptt, 'ss.txt')
ssr_file = os.path.join(ptt, 'ssr.txt')

open(vmess_file, "w").close()
open(vless_file, "w").close()
open(trojan_file, "w").close()
open(ss_file, "w").close()
open(ssr_file, "w").close()

vless = ""
trojan = ""
ss = ""
ssr = ""
respnse = requests.get("https://github.com/hossein-mohseni/Free-V2ray-Config/blob/main/configs.txt").text
for config in respnse.splitlines():
    if config.startswith("vmess"):
        open(vmess_file, "a").write(config + "\n")     
    if config.startswith("vless"):
        vless += config + "\n"  
    if config.startswith("trojan"):
        trojan += config + "\n"   
    if config.startswith("ss"):   
        ss += config + "\n"
    if config.startswith("ssr"):
        ssr += config + "\n"
 
open(vless_file, "w").write(base64.b64encode(vless.encode("utf-8")).decode("utf-8"))  
open(trojan_file, "w").write(base64.b64encode(trojan.encode("utf-8")).decode("utf-8"))  
open(ss_file, "w").write(base64.b64encode(ss.encode("utf-8")).decode("utf-8"))  
open(ssr_file, "w").write(base64.b64encode(ssr.encode("utf-8")).decode("utf-8"))  
