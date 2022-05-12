import os, sys
def clearscreen():
    if sys.platform == "linux2":
        os.system("clear")
    elif sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
        
clearscreen()
banner = """\033[1;31m _     _         ______               
| |   | |       (____  \         _    
| |   | | _____  ____)  )  ___  | |_  
| |   | |(___  )|  __  (  / _ \ |  _) 
| |___| | / __/ | |__)  )| |_| || |__ 
 \______|(_____)|______/  \___/  \___)
 	  """"""\033[1;32mcreated by @darknet_off1cial"""
print(banner)
