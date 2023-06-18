import xmltodict
import json
xml_file = open("leabharlann.xml","r", encoding="utf-8")
xml_string = xml_file.read()
xml_string = xml_string.encode(encoding='UTF-8', errors = 'strict')
python_dict=xmltodict.parse(xml_string)
#file = open("leabharlan.json", "w", encoding="utf-8")
#json.dump(python_dict,file)
#file.close()

print(python_dict)

