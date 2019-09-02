# -*- coding=utf-8 -*-
#!/usr/bin/env python3

import os

if os.environ.get('GO_KEY') is None:
    print('attention, il y a un probleme avec la clé google')
    GO_KEY = "YOUR TOKEN"
else:
    GO_KEY = os.environ['GO_KEY']