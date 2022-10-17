import string 
import sys

#The businesscorp.com.br domain is allowed for studies.
#https://github.com/tomnomnom/waybackurls
#run echo "businesscorp.com.br" | waybackurls

dic_wayback = {}

def parse():
    with open('wayback.txt') as file:
        for line in file:
            dic_wayback['protocolo'] = line.rsplit(':')[0]
            dic_wayback['url'] = line.strip('\n')
            print(dic_wayback)
 
def main():
    parse()

if __name__=='__main__':
    main()