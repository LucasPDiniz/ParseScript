import sys
import string
import json

#Sublist3r --> github.com/aboul3la/Sublist3r
#python3 sublist3r.py -d exemple.com -o domains.txt 

dic_sublist3r = {}

def parse():
    with open('/home/kali/Downloads/Sublist3r/strings.txt') as file:
        for line in file:
            dic_sublist3r['subdomain'] = line.rstrip('\n')
            print(dic_sublist3r)
def main():
    parse()

if __name__== '__main__':
    main()