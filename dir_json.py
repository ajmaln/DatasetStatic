import os
import json

json_file = open('files.json', 'w')

def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir\
(path)]
    else:
        d['type'] = "file"
    d['path'] = path
    return d

print(json.dumps(path_to_dict('download'), indent=4, sort_keys=True), file=json_file)
