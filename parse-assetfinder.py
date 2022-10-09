import sys
import string 
import json

#https://github.com/tomnomnom/assetfinder
#The businesscorp domain is allowed for studies.

dic_assetfinder = {}

def parse():
    with open('assetfinder.txt') as file:
        for line in file:
            dic_assetfinder['subdomain'] = line.rstrip('\n')
            print(dic_assetfinder)

def main():
    parse()

if __name__=='__main__':
    main()