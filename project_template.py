import os

#Define the folders and subfolders you require
dirs = [
    os.path.join("data","raw"),
    os.path.join("data", "processed"),
    "notebooks",
    "saved_models",
    "src"
]
#create directories and git keep file(as empty folder creating will be an issue with the git)
for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass


#Similarly create files
files = [
    "requirements.txt",
    ".gitignore",
    "README.md",
    os.path.join("src","__init__.py"),
    "dvc.yaml",
    "params.yaml",    
]

#create files
for file_ in files:
    with open(file_, "w") as f:
        pass