import string 
import sys
import requests
import json


#The businesscorp.com.br domain is allowed for studies.

dic_nuclei = {}

def parse():
    with open('nuclei.json') as json_file:
        for linejson in json_file:
            jsonline = linejson.rstrip('\n')
            jsondata = json.loads(jsonline)
            for i in jsondata:
                dic_nuclei['template'] = jsondata['template']
                dic_nuclei['name'] = jsondata['info']['name']
                dic_nuclei['severity'] = jsondata['info']['severity']
                dic_nuclei['tags'] = jsondata['info']['tags']
                dic_nuclei['host'] = jsondata['host']
                dic_nuclei['ip'] = jsondata['ip']
            print(dic_nuclei)
                

def main():
    parse()

if __name__=='__main__':
    main()