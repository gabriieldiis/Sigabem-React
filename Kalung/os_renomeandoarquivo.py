import os
 
dir = r'C:\Users\internet07\Desktop\renamepython'
old_file = os.path.join(dir, 'new_filename.txt')
new_file = os.path.join(dir, 'barros.txt')
 
os.rename(old_file, new_file)    