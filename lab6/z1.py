import os
def list(path):
    directors=[]
    file=[]
    all_directories_files = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            directors.append(item)
            all_directories_files.append(item)
        elif os.path.isfile(item_path):
            file.append(item)
            all_directories_files.append(item)
    print(directors)
    print(file)
    print(all_directories_files)
path =r"C:/Users/Admin"
list(path)
