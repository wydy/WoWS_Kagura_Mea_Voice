import xml.etree.ElementTree
import copy
import os

def backup_mod(path):
  if os.path.exists(path + os.path.sep + "mod.xml.bak"):
    i = 1
    while os.path.exists(path + os.path.sep + "mod.xml.bak" + str(i)):
      i += 1
    for j in range(i, 1, -1):
      os.rename(path + os.path.sep + "mod.xml.bak" + str(j - 1), path + os.path.sep + "mod.xml.bak" + str(j))
    os.rename(path + os.path.sep + "mod.xml.bak", path + os.path.sep + "mod.xml.bak1")
  os.rename(path + os.path.sep + "mod.xml", path + os.path.sep + "mod.xml.bak")

def check_valid_path():
  global path
  path = raw_input("Mod directory: ")
  if os.path.exists(path + os.path.sep + "mod.xml"):
    return True
  print("mod.xml not found in that directory.")
  return None

def process_event(event):
  eventnamenode = event.find("Name")
  eventname = eventnamenode.text
  assoceventnode = evtlist.find(eventname)
  
  if eventnamenode.text == "Play_Avatar_Damage":
    duplicate = copy.deepcopy(event)
    duplicate.find("Name").text = "Play_Avatar_Flooding"
    process_event(duplicate)
    treeroot.append(duplicate)
    
  if assoceventnode is not None:
    eventnamenode.text = assoceventnode.find("Name").text
    
  containers = event.findall("Container")
  for container in containers:
    if container.find("Name").text == "Voice" and assoceventnode is not None:
      container.find("ExternalId").text = assoceventnode.find("ExternalId").text
    paths = container.findall("Path")
    for path in paths:
      states = path.find("StateList").findall("State")
      for state in states:
        statenamenode = state.find("Name")
        statevaluenode = state.find("Value")
        statename = statenamenode.text
        assocstatenode = statelist.find(statename)
        if assocstatenode is not None:
          statenamenode.text = assocstatenode.find("Name").text
          assocstatevalnode = assocstatenode.find("ValueList").find(statevaluenode.text)
          if assocstatevalnode is not None:
            statevaluenode.text = assocstatevalnode.find("Name").text

if __name__ == "__main__":

  folder_exists = None
  while(folder_exists is None):
    folder_exists = check_valid_path()
    
  updtree = xml.etree.ElementTree.parse("modupdate.xml")
  tree = xml.etree.ElementTree.parse(path + os.path.sep + "mod.xml")

  evtlist = updtree.getroot()[0]
  statelist = updtree.getroot()[1]

  treeroot = tree.getroot()[0]

  events = treeroot.findall("ExternalEvent")

  for event in events:
    process_event(event)

  backup_mod(path)
  
  with open(path + os.path.sep + "mod.xml", "wb") as f:
    f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write(xml.etree.ElementTree.tostring(tree.getroot(), encoding="utf-8"))
