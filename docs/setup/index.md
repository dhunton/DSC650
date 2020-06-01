# Overview

!!! warning "Documentation in Progress"
    Check back soon for more updates.
    
---
    
## Operating System Dependencies

See the pages [macOS](macOS.md), [Ubuntu](ubuntu.md), or [Windows 10](windows.md) for how to install the operating system specific dependencies for your computer.  

## Clone Github Repository

Start by cloning or downloading this repository to your local computer.  You can clone this repository using the [Github Desktop Client][github-desktop] or using the Git command line.

*Clone using SSH*

```
git clone git@github.com:bellevue-university/dsc650.git
```

*Clone using HTTPS*

```
git clone https://github.com/bellevue-university/dsc650.git
```

You will need access to this repository throughout the course, so place it in a reliable location.

## Python Dependencies

!!! note
    Some of the dependencies do not work with Python 3.8, so you will need to install Python 3.7. 

### Poetry

Poetry is a dependency management and packaging tool for Python.  You can use it to declare libraries for your project and manage (install/update) them for you. 

*macOS, Linux, or Bash on Windows*

```shell 
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

*Windows PowerShell*

```shell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

For this project you can use `poetry install` to install the project dependencies. This command will create a virtual environment for your project and install the dependencies.  You can use the `poetry shell` command to activate this virtual environment. 

Within the root directory of the `dsc650` repository, run the following commands to setup your Python environment using Poetry. 

```
$ poetry env use 3.7
Creating virtualenv dsc650-Q1YxCGsa-py3.7 in /usr/local/var/virtualenvs
Using virtualenv: /usr/local/var/virtualenvs/dsc650-Q1YxCGsa-py3.7
$ poetry install
Installing dependencies from lock file

Package operations: 143 installs, 0 updates, 0 removals

  - Installing decorator (4.4.2)
  - Installing ipython-genutils (0.2.0)
  - Installing six (1.14.0)
  - Installing zipp (3.1.0)
  - Installing attrs (19.3.0)
  . 
  . 
  . 
  - Installing tensorflow (2.1.0)
  - Installing tinydb (4.1.1)
  - Installing zodb (5.5.1)
  - Installing dsc650 (0.1.0)
```

Once completed, you can use `poetry shell` to activate the virtual environment. 

```shell
$ poetry shell  
Spawning shell within /usr/local/var/virtualenvs/dsc650-Q1YxCGsa-py3.7
```

You can add this interpreter to an existing PyCharm project by selecting the `PyCharm` menu and then select `Preferences` -> `Project` -> `Project Interpreter`.  In this example, you would add `/usr/local/var/virtualenvs/dsc650-Q1YxCGsa-py3.7/bin/python` as the interpreter. 

See [Poetry][poetry] for additional documentation on basic usage. 

### Virtualenv and Pip

You can use `virtualenv` and Pip if you don't want to use Poetry.  Simply use the following commands. 

```shell
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

You can add this interpreter to an existing PyCharm project by selecting the `PyCharm` menu and then select `Preferences` -> `Project` -> `Project Interpreter`.  In this example, you would add `venv/bin/python` as the interpreter. 

## PyCharm

After you are finished cloning or downloading the repository, you will open the repository directory using PyCharm.  You can do this by opening PyCharm and selecting the `File -> Open` option and choosing the directory containing the repository. [Download PyCharm][pycharm-download] if you do not already have it installed on your computer. You can also download [PyCharm for Anaconda][pycharm-anaconda] to install PyCharm with the Anaconda Python interpreter.


[dsc650-repo]: https://github.com/bellevue-university/dsc650
[github-desktop]: https://desktop.github.com/
[poetry]: https://python-poetry.org/docs/
[pycharm-anaconda]: https://www.jetbrains.com/pycharm/promo/anaconda/
[pycharm-download]: https://www.jetbrains.com/pycharm/download/
