file_name = "settings.ini"
settings = {"deltime":20,"intval":6}

def save():
 global file_name
 global settings
 file = open(file_name,"w")
 for key,value in settings.items():
  file.write(f"{key}:{value}\n")
 file.close()

def load():
 global file_name
 global settings
 newdic = {}
 file = open(file_name,"r")
 for line in file:
  key=line.split(":")[0]
  value=line.split(":")[1]
  newdic[key] = int(value)
 settings = newdic
 file.close()

def peek():
 global file_name
 file = open(file_name,"r")
 txt = ""
 for line in file:
  txt += line
 file.close()
 return txt

