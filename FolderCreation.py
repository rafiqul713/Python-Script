import os
root_path = 'path'

for folder in range(1,85):
    os.mkdir(os.path.join(root_path,str(folder)))
    print(folder)
