import os
import sys
from cfonts import *
from colorama import *
def clear():
  os.system('clear')
  logo = render("FILES",colors=["blue","yellow"],align="center")
  dialog = (f"{Fore.BLUE}<{Fore.GREEN}/{Fore.BLUE}> {Fore.WHITE}Script By{Fore.RED} Mohamed Bougrina{Fore.YELLOW} <{Fore.BLUE}/{Fore.YELLOW}>\n")
  print(logo+"\n\t"+dialog)
clear()
def search(file,text):
  test = input(f"\t{Fore.GREEN}[{Fore.BLUE}?{Fore.GREEN}]{Fore.CYAN}Show files {Fore.RED}({Fore.WHITE}y{Fore.BLUE}/{Fore.WHITE}n{Fore.RED}){Fore.BLUE}? {Fore.GREEN}: {Fore.WHITE}")
  number = int(0)
  for root,dirs,files in os.walk(file):
    for search in files:
      if search.endswith(text):
        number+=1
        print(f"\t{Fore.GREEN}[{Fore.BLUE}?{Fore.GREEN}]{Fore.CYAN}Files {Fore.BLUE}: {Fore.WHITE}",number,end="\r")
        if test=='y' or test == 'yes' or test == 'Yes' or test == 'YES':
           print(f"\t{Fore.WHITE}{number}{Fore.BLUE}:{Fore.YELLOW}"+os.path.join(root,search))
  print(f"\t{Fore.GREEN}[{Fore.BLUE}!{Fore.GREEN}]{Fore.CYAN}Number Files {Fore.BLUE}: {Fore.WHITE}",number)
data = input(f"\t{Fore.GREEN}[{Fore.BLUE}?{Fore.GREEN}]{Fore.CYAN}Folder{Fore.BLUE} :{Fore.WHITE} ")
mot = input(f"\t{Fore.GREEN}[{Fore.BLUE}?{Fore.GREEN}]{Fore.CYAN}Search {Fore.BLUE}:{Fore.WHITE} ")
search(file=data,text=mot)
