# PyJudge

Preparations:

1. Docker: https://docs.docker.com/engine/installation/
2. Place user into the docker group:   ```sudo usermod -aG docker $USER ```
3. Tango: https://github.com/autolab/Tango/wiki/Set-up-Tango
4. In setting up, Tango when preparing the config.py file set these variables to these specific values:
```python
COURSELABS = "courselabs/"
OUTPUT_FOLDER = "output"
VMMS_NAME = "localDocker"
KEYS = ["pyjudge"]
```

Setting Up PyJudge:

1. When cloning PyJudge, clone it so that is has the same parent directory as the cloned Tango. 
3. Install required packages found in repo:   ```pip3 install -r requirements.txt```
4. Instantiate User DB: ```python3 dummy.py```

Running PyJudge

1. Launch Servers: ```./pyjudge start```
2. Stop Servers:   ```./pyjudge stop```

Once running you can access the preliminary pages with: http://localhost:4003/
