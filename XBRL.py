# coding: utf-8

import xml.etree.ElementTree as ET

class taxonomy:
    f = open("Users/sho/Documents/taxonomy.xml", 'r', encoding='utf8')
    tree = ET.parse(f)
    root = getroot()
    

f = open("/Users/sho/Documents/ir.xbrl", 'r', encoding='utf8')
tree = ET.parse(f)
root = tree.getroot()

root.
