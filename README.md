# python tools - Collection of script for reference 

# Install Python:
  * Mac: `brew install python@3.10`
  * relink: `brew unlink python@3.9 && brew link python@3.10`
  * `echo 'export PATH="/usr/local/opt/python@3.10/bin:$PATH"' >> $HOME/.bash_profile`


# Install module dependency:

* Create virtual environment: `python -m venv venv`
* Activate virtual environment:  `source venv/bin/activate`    
* install dependencies:   `pip3 install -r requirements.txt`

```
./python-tools/venv/bin/python -m pip install --upgrade pip
pip install --upgrade --force-reinstall chromedriver-binary-auto

```

# Python Docker:

    Docker bases image:  https://pythonspeed.com/articles/base-image-python-docker-images/


# workday:
https://github.com/WPIRoboticsEngineering/Workday-Automation/blob/master/invoice.py
