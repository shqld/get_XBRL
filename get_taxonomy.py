import xlrd
import xlwt
from xml.etree.ElementTree import Element, SubElement, Comment
from ElementTree_pretty import prettify

b = ["一般商工業","建設業","銀行・信託業","銀行・信託業（特定取引勘定設置銀行）",
    "建設保証業","第一種金融商品取引業","生命保険業","損害保険業","鉄道事業",
     "海運事業","高速道路事業","電気通信事業","電気事業","ガス事業","資産流動化業",
     "投資運用業","投資業","特定金融業","社会医療法人","学校法人","商品先物取引業",
     "リース事業","投資信託受益証券"]

book = xlrd.open_workbook('/Users/sho/Documents/get_XBRL_py/taxo.xls')

def get_sheet(n):
    global name,sheet,num
    sheet = book.sheet_by_index(n)
    name = b[n]
    num = n

get_sheet(0)


titles = {"classification":"科目分類","label_jp":"標準ラベル（日本語）",
          "label_redundant_jp":"冗長ラベル（日本語）","label_use_jp":"用途別ラベル（日本語）",
          "label_biz_jp":"業種ラベル（日本語）","is_consol":"連結",
          "q_indiv":"四半期個別","q_consol":"四半期連結",
          "h_indiv":"中間個別","h_consol":"中間連結",
          "label_eg":"標準ラベル（英語）","label_use_eg":"用途別ラベル（英語）",
          "label_biz_eg":"業種ラベル（英語）","namespace":"名前空間プレフィックス",
          "element":"要素名","type":"type","enum":"enumerations",
          "substit":"substitutionGroup","period_type":"periodType",
          "balance":"balance","is_abstract":"abstract",
          "nillable":"nillable","depth":"depth"}


title_list = ["classification","label_jp","label_redundant_jp","label_use_jp",
              "label_biz_jp","is_consol","q_indiv","q_consol","h_indiv",
              "h_consol","label_eg","label_use_eg","label_biz_eg",
              "namespace","element","type","enum","substit",
              "period_type","balance","is_abstract","nillable","depth"]

root = Element('root')

def get_xml():


    sheets = SubElement(root, str("sheet_" + str(num)), {'id':str(name)})
#    for i in range(10):
    for i in range(sheet.nrows):
        is_data = sheet.cell(i,0).value
        def get_data(col):
            data = str(sheet.cell(i,col).value)
            if "\n\n" in data:
                data = data.replace("\n\n", ", ")            
            return data

        if "A" == is_data or "B" == is_data or "-" == is_data:
    
            element = SubElement(sheets, str("element_" + str(i)), {'id':get_data(14), 'depth':get_data(22)})
            
            contents = [SubElement(element, str("content_" + str(j)), {'id':str(title_list[j])}) for j in range(len(title_list))]
            for j in range(len(title_list)):
                contents[j].text = get_data(j)


#### Type it later.

    f = open("/Users/sho/Documents/new.xml", 'w', encoding = 'utf8')
    f.write(prettify(root))


if __name__ == "__main__":
    for n in range(len(b)):
        get_sheet(n)
        get_xml()
#    get_sheet(22)
#    get_xml()

    pass

    

