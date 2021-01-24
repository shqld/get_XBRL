#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib.parse
import urllib.request
import json
import requests
import xml.etree.ElementTree as ET


companies = {}
def d():
    query={"limit":150, "hasXBRL":1}
    r = requests.get("https://webapi.yanoshin.jp/webapi/edinet/list/20160425.json?", params=query)
    data = r.json()["items"]
    for n in range(len(data)):
        if "有価証券報告書" in data[n]["Edinet"]["title"]:
            if "訂正" not in data[n]["Edinet"]["title"]:
                url = data[n]["Edinet"]["xbrl_url"]
                name = data[n]["Edinet"]["publisher_name"]
                companies[name] = url

                file_name="/Users/sho/Documents/IR_downloads/" + name + ".zip"
                urllib.request.urlretrieve(url,file_name)

    print(companies.keys())
        
def getTool(url):
    r = requests.get(url)
    file_name = input("name is ... \n")
    file_name = "/Users/sho/Documents/" + file_name
    f = open(file_name,"r+")
    f.write(str(r))
    f.close()



if __name__ == "__main__":
    d()
