# coding: utf-8
import xml.etree.ElementTree as ET
import json
import os, re, csv
from ElementTree_pretty import prettify

#ディレクトリ配下のファイルのうちis_xbrl_fileがTrueのもののみ取得する
aaaaa = """def fild_all_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if not is_xbrl_file(root,file):
                continue
            yield os.path.join(root, file)

def is_xbrl_file(root_path,file_name):
    #xbrlファイルでなければ対象外
    if not file_name.endswith('.xbrl'):
        return False
    #AuditDocは対象外
    if u'AuditDoc' in str(root_path):
        return False
    return True"""




with open("/Users/sho/Documents/get_XBRL_py/taxonomy_lite.json", 'r', encoding='utf8') as f:
    json_root = json.load(f)
    elements = json_root["sheet_7"]
    # シートを自動で選択できるようにする。どこで業種の識別ができるか探す。

# 自動でxbrlファイルを取ってくるようにする
f = open("/Users/sho/Documents/ir3.xbrl", 'r', encoding='utf8')
tree = ET.parse(f)
root = tree.getroot()
# fs_info：財務情報を含む多くのタグのリスト
fs_info = root.findall('./')


### data range ###
for i in range(len(fs_info)):
    if 'NumberOfSubmission' in fs_info[i].tag:
        fs_start = i
    elif 'DocumentTitleCoverPage' in fs_info[i].tag:
        fs_end = i



value_prior = []
value_current = []

label_prior = []
label_current = []


# fs_sphere：財務情報が載っている範囲
fs_sphere = fs_info[fs_start:fs_end]


# parse by lines
for i in range(len(fs_sphere)):

    try:
        # fs_infoのタグをタクソノミjsonのキーワードに代入してラベルを取得
        # 弾くURLも全てのケースに対応するようにする
        data = elements[fs_sphere[i].tag.replace("{http://disclosure.edinet-fsa.go.jp/taxonomy/jppfs/2015-03-31/jppfs_cor}",'')]

        if "Prior" in fs_sphere[i].get('contextRef'):
            value_prior.append(fs_sphere[i].text)
            label_prior.append(data["label"])


        elif "Current" in fs_sphere[i].get('contextRef'):
            value_current.append(fs_sphere[i].text)
            label_current.append(data["label"])

    except KeyError:
        pass


# 前期分のラベルと数値をまとめたデータをリストにし、
# {1:[label, value], 2: [ ] }のように辞書に変換（jsonに書き出すため）
prior = {}
for i in range(len(label_prior)):
    prior[i] = [label_prior[i],value_prior[i]]


# 書き出すときのファイル名は証券コードを使う
with open("/Users/sho/Documents/get_XBRL_py/ir3.json", 'a', encoding='utf8') as w:
    json.dump(prior, w, ensure_ascii=False, indent=3)



#for i in range(len(label_prior)):
#    print(label_prior[i],value_prior[i])

#for i in range(len(label_current)):
#    print(label_current[i],value_current[i])

     



if __name__ == '__main__':

    pass
