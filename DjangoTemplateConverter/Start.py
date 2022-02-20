import argparse
import os
import importlib.util
from bs4 import BeautifulSoup
from pathlib import Path


# DjangoTemplateConverter
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--su', help='arg1 help')
    parser.add_argument('--rl', help='arg2 help')
    args = parser.parse_args()
    print("arg1 {}, arg2 {}".format(args.su, args.rl))
    removeLength = args.rl if args.rl else 9
    staticUrl = args.su if args.su else 'static'
    loadStatic="{% load static %}"
    cwd = os.getcwd()
    lol =Path(cwd).resolve()
    BASE_DIR = [lol /'templates']
    print(BASE_DIR)
    for temPath in BASE_DIR:
        print(temPath)
        files = os.listdir(temPath)
    # shutil.copy(settings.BASE_DIR / "writenow/build/index.html", settings.BASE_DIR / "template/index.html")
        for f in files:
            split_up = os.path.splitext(f)
            if(split_up[-1] == '.html' and len(split_up)>1):
                file_path = temPath / f
                with open(file_path, 'r+') as file:
                    data = file.read()
                    soup = BeautifulSoup(data, "html.parser")
                    for link in soup.find_all('link', href=True):
                        splitt = link['href'].split('.')
                        # if(len(splitt)>1 and splitt[-1]=='css' and link.parent.name=='head'):
                        if(len(splitt)>1 and splitt[-1]=='css'):
                            newHref = "{% "+staticUrl+" '" +link['href'][removeLength:] +"' %}"
                            link['href']=newHref
                            
                    for script in soup.find_all('script', src=True):
                        splitt = script['src'].split('.')
                        # if(len(splitt)>1 and splitt[-1]=='js' and script.parent.name=='body'):
                        if(len(splitt)>1 and splitt[-1]=='js'):
                            newSrc = "{% "+staticUrl+" '" +script['src'][removeLength:] +"' %}"
                            script['src']=newSrc
                    
                    # print(soup)
                    file.truncate(0)
                    file.seek(0)
                    file.write(loadStatic+'\n')
                    file.write(str(soup))
                    file.close()




main()