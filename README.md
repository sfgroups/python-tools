# python tools - Collection of script for reference 

# Install Python:
  * Mac: `brew install python@3.10`
  * relink: `brew unlink python@3.9 && brew link python@3.10`
  * `echo 'export PATH="/usr/local/opt/python@3.10/bin:$PATH"' >> $HOME/.bash_profile`

# Pip file location

* On Unix the default configuration file is: `$HOME/.config/pip/pip.conf`
* On Windows the configuration file is `%APPDATA%\pip\pip.ini`.
* Check cert file path
    `python3 -c 'import ssl; print(ssl.get_default_verify_paths())'`

# Install module dependency:

* Create virtual environment: `python -m venv venv`
* Activate virtual environment:  `source venv/bin/activate`    
* install dependencies:   `pip3 install -r requirements.txt`

# Setup Virtual Environment**
```
python3 -m venv venv

venv\Scripts\Activate.ps1  # Windows PowerShell
source venv/Scripts/activate  # Git bash
source venv/bin/activate   # Linux

source venv/bin/activate
```

```
./python-tools/venv/bin/python -m pip install --upgrade pip
pip install --upgrade --force-reinstall chromedriver-binary-auto

```

# Python Docker:

    Docker bases image:  https://pythonspeed.com/articles/base-image-python-docker-images/


# workday:
https://github.com/WPIRoboticsEngineering/Workday-Automation/blob/master/invoice.py
