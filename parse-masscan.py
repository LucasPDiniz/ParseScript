import sys
import string

#https://github.com/robertdavidgraham/masscan
#The ip:businesscorp domain is allowed for studies.

dic_masscan = {}

def parse():
    with open('masscan.txt') as file:
        for line in file:
            dic_masscan['address'] = line.rstrip('\n').split(' ')[5]
            dic_masscan['port'] = line.rstrip('\n').split(' ')[3].split('/')[0]
            dic_masscan['protocol'] = line.rstrip('\n').split(' ')[3].split('/')[1]
            dic_masscan['state'] = line.rstrip('\n').split(' ')[1]
            print(dic_masscan)

def main():
    parse()

if __name__=='__main__':
    main()