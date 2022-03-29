import xml.etree.ElementTree as ET
import pandas as pd

tree = ET.parse('./module_3_test/menu.xml')    
root = tree.getroot()  
print(root[0][1])
for elem in root:  
    for subelem in elem:  
        print(elem.attrib['name'], subelem.tag, subelem.text)  
    print() 

df_index = ['name', 'price', 'weight', 'class']  
df = pd.DataFrame(columns=df_index)  
  
for elem in root:  
    elements = [elem.get('name'), elem[0].text, elem[1].text, elem[2].text]  
    df = df.append(pd.Series(elements, index=df_index), ignore_index=True) 

print(df)    

import xmljson  
parker_json = xmljson.parker.data(root)  
print(parker_json)
back_to_xml = xmljson.parker.etree(parker_json) 

# создение xml

new_root = ET.Element('menu')  
dish_1 = ET.SubElement(new_root, 'dish')  
dish_2 = ET.SubElement(new_root, 'dish')  
print(new_root.getchildren() )
dish_1.set('name', 'Кура')  
dish_1.text = 'Белок'

# Теперь запишем получившийся XML-файл на диск, используя стандартные средства Python. Сначала превратим объект типа ElementTree.Element в строку (str) c помощью метода tostring(), передав наше новое дерево как аргумент:

new_root_string = ET.tostring(new_root)  
with open("./module_3_test/new_menu.xml", "wb") as f:  
    f.write(new_root_string)
# или так
ET.ElementTree(new_root).write('./module_3_test/new_menu_good.xml', encoding="utf-8")      



