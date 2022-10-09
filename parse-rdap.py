import sys
import string 
import requests
import json

#https://github.com/openrdap/rdap/
#The businesscorp domain is allowed for studies.

dic_openrdap = {}
idc_openrdap_ip ={}

def parse():
    r = requests.get('https://rdap.registro.br/domain/businesscorp.com.br')
    retorno_rdap = r.text
    json_rdap = json.loads(retorno_rdap)
    dic_openrdap['domain'] = json_rdap['handle']
    
    for name in json_rdap['nameservers']:
        dic_openrdap['nameservers'] = name['ldhName']
        dic_openrdap['responsavel'] = json_rdap['entities'][1]['vcardArray'][1][2][3]
        print(dic_openrdap)
   
def main():
    parse()

if __name__=='__main__':
    main()