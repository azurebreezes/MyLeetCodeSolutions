#Create a folder with a txt file and a py file in it

import os
folder="1480. Running Sum of 1d Array"
if not os.path.exists(folder):
    os.makedirs(folder)
    write_path=f'{folder}/{folder}.txt'
    f=open(write_path, 'w')
    f.write("Empty")
    f.close()
    write_path=f'{folder}/{folder}.py'
    f=open(write_path, 'w')
    f.write("#Empty")
    f.close()
    print("Folder Created")
else:
    print("Folder exist")