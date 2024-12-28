import os
path=r'\justforcheck\idk'
result=os.path.exists(path)
if result== True:
    os.rmdir(path)
