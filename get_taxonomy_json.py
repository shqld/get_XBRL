#coding:utf-8
import xml.etree.ElementTree as ET
import json

with open("/Users/sho/Documents/get_XBRL_py/taxonomy_new.xml", 'r',encoding='utf8') as f:
    tree = ET.parse(f)
    root = tree.getroot()

#{sheet_num:
# element{element_name:{depth: ,label:, etc:{}}},sheet_num:{element_name:...}

sheets = root.findall('./')


aa,bb,cc = {},{},{}


for a in range(len(sheets)):
    elements = sheets[a].findall('./')
    for b in range(len(elements)):
        contents = elements[b].findall('./')
        cc["depth"] = contents[22].text.replace('.0','')
        cc["label"] = contents[1].text
        bb[elements[b].get('id')] = cc
        cc={}
    aa["sheet_" + str(a)] = bb




w = open("/Users/sho/Documents/get_XBRL_py/aaa.json",'w',encoding='utf8')
json.dump(aa, w,ensure_ascii=False, indent=3)
w.close()
