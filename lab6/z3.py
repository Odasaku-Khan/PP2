import os
result=os.path.exists("justforcheck")
print(result)
path=r'C:\Users\Admin'
check=os.path.exists(path)
print(check)
filename=os.path.basename(path)
print(filename)
directory=os.path.dirname(path)
print(directory)