import json
import xmltodict, json


xmlstring = xmltodict.parse('''<args>
						<arg>2</arg>
						<arg>2</arg>
					    </args>''')

jstr = json.dumps(xmlstring, indent=4)
print(jstr)

xmlstring = xmltodict.unparse(json.loads(jstr), pretty=True)
print(xmlstring)
