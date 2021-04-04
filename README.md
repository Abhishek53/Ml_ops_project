create a project structure
```bash
python3 project_template.py
```

create a virtual enviromnment
```bash
python3 -m venv mlops_project1
```

activate virtual environment
```bash
source ./mlops_project1/bin/activate
```

add requried libraries to requirements.txt
```bash
pip3 install -r requirements.txt
```

configure git and dvc
```bash
git init
dvc init
dvc add data_given/winequality.csv
git add datagiven/winequality.csv
git add .
git commit -m "organized project structure"
git push orgin master
```