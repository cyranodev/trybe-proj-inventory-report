#### <a name="top"></a> This repo is a clone of an individual project part of [Trybe](https://www.betrybe.com/) junior web developer course.
##### https://www.betrybe.com/ (in Portuguese)

# Stock reports  ![!project status](https://img.shields.io/badge/status-development-yellow)   ![!python](https://img.shields.io/badge/python-3.6-green) ![!lxml](https://img.shields.io/badge/lxml-4.6-darkorange) ![!black](https://img.shields.io/badge/black-20.8b1-red) ![!flake8](https://img.shields.io/badge/flake8-3.8-blue) ![!pytest](https://img.shields.io/badge/pytest-6.1-orange)
- [Requisites](#requisites)
- [Instructions](#instructions)


## Requisites <a name="requisites"></a>

**Stock report** is a small app to read CSV, JSON or XML files, providing console reports and Iterable instances. 🐍

This project covers **Python**, intro to **Object Oriented Programming** and **design patterns** (using _Iterable_ and _Strategy_).


Project's filenames and architecture are defined by the project and must be unchanged to pass the course tests.

Original requirements and instructions (in Portuguese) for the project are [**here**](README_original.md).


**Requisites sum-up:**

- Create console report methods and classes
- Create file importer and reader classes
- Refat Report class to become an Iterable
- Create method to receive arguments from terminal command and run the app.

##### [back to top](#top)

## Instructions <a name="instructions"></a>

**Clone** the repo or **download** the zip.

Be sure to have Python installed in your system.

Go to the project folder, start a virtual environment, and run phyton's default command to install.
**Example** (in Ubuntu):
```bash
python3 -m venv .venv && source .venv/bin/activate
python3 -m pip install -r dev-requirements.txt
```

Sometimes one might stumble upon an error related to Python Wheel lib when running the `pip install ...` command above.  
Run `pip install wheel` in project folder and run the `pip install...` command again.

To **run** the app:
```bash
inventory_report param1 param2
```
##### (where _param1_ is the file path and _param2_ is the type of report: `'simples'` or `'completo'` (meaning 'simple' or 'complete')

To run **tests** (within project folder):
```bash
$ python3 -m pytest
```

##### [back to top](#top)

