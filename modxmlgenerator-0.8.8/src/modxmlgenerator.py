import os, sys
from collections import defaultdict

folder_names = ["Voice", "SFX", "Loop"]

def generate_xml(tree):
    whitelist = ['MainGun', 'SecondaryGun', 'AAC0', 'AAC1', 'AAC2', 'TA']
    modname = os.path.basename(os.getcwd())
    out_file = open('mod.xml', 'w')
    out_file.write('<?xml version="1.0"?>\n<AudioModification.xml>\n    <AudioModification>\n        <Name>' + modname + "</Name>\n")
    for event, ele in tree.items():
        if any(e is not None for e in ele):
            if event in whitelist:
                out_file.write("        <ExternalEvent>\n            <Name>" + event + "</Name>\n            <Container>\n")
            else:
                out_file.write("        <ExternalEvent>\n            <Name>Play_" + event + "</Name>\n            <Container>\n")
            for i in range(3):
                if ele[i] is not None:
                    out_file.write("                <Name>" + folder_names[i] + "</Name>\n                <ExternalId>" + folder_names[i][0] + event + "</ExternalId>\n")
                    for states, files in ele[i].items():
                        out_file.write("                <Path>\n                    <StateList>\n")
                        for state in states:
                            namevalue = state.split("__")
                            out_file.write("                        <State>\n                            <Name>" + namevalue[0] + "</Name>\n                            <Value>" + namevalue[1] + "</Value>\n                        </State>\n")
                        out_file.write("                    </StateList>\n                    <FilesList>\n")
                        for file in files:
                            out_file.write("                        <File>\n                            <Name>" + file + "</Name>\n                        </File>\n")
                        out_file.write("                    </FilesList>\n                </Path>\n")
            out_file.write("            </Container>\n        </ExternalEvent>\n")
    out_file.write('    </AudioModification>\n</AudioModification.xml>\n')
    out_file.close()

def parse_event(event, folder):
    filelist = []
    states = defaultdict(list)
    for dirpath, dirnames, filenames in os.walk(os.path.join(folder, event)):
        for filename in filenames:
            filelist.append(os.path.join(dirpath, filename))
    for f in filelist:
        states[frozenset([i for i in f.split(os.path.sep) if "__" in i])].append(f.replace(os.path.sep, "/"))
    if not states:
        states = None
    return states

def combine_dicts(voice_tree, sfx_tree, loop_tree):
    tree = defaultdict(lambda: [None, None, None])
    for event, element in voice_tree.items():
        tree[event][0] = element
    for event, element in sfx_tree.items():
        tree[event][1] = element
    for event, element in loop_tree.items():
        tree[event][2] = element
    return tree

def check_valid_path():
    folder_exists = [False, False, False]
    path = raw_input("Mod directory: ")
    try:
        os.chdir(path)
    except OSError as e:
        print(e)
        return None
    except:
        print("Unknown error.")
        return None
    for i in range(3):
        if os.path.exists(folder_names[i]):
            folder_exists[i] = True
    if folder_exists == [False, False, False]:
        print("Voice/SFX/Loop folder not found in that directory.")
        return None
    return folder_exists

if __name__ == '__main__':

    folder_exists = None
    while(folder_exists is None):
        folder_exists = check_valid_path()

    trees = [{}, {}, {}]
    for i in range(3):
        if(folder_exists[i]):
            trees[i] = dict((event, defaultdict(list)) for event in next(os.walk(folder_names[i]))[1])
            for event in trees[i].keys():
                trees[i][event] = parse_event(event, folder_names[i])

    tree = combine_dicts(trees[0], trees[1], trees[2])
    generate_xml(tree)

    
