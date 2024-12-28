import os
print('Exist:',os.access('C:/Users/Admin/AppData/Local/Programs/Python/Python312/python.exe',os.F_OK))
print('Readable:',os.access('C:/Users/Admin/AppData/Local/Programs/Python/Python312/python.exe',os.R_OK))
print('Writable:',os.access('C:/Users/Admin/AppData/Local/Programs/Python/Python312/python.exe',os.W_OK))
print('Executable:',os.access('C:/Users/Admin/AppData/Local/Programs/Python/Python312/python.exe',os.X_OK))
