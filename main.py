#!/usr/bin/env python

import requests
print(requests.__version__)
r = requests.get("https://raw.githubusercontent.com/hiufungk/cmput404lab1h05/master/main.py")
#print(dir(r))
print(r.text)
#print(r.status_code)


