#!/usr/bin/env python3

import sys
import json
import tempfile
import shutil
import os

args = sys.argv

new_json_fp = tempfile.NamedTemporaryFile(mode='a', delete=False)

with open(args[1]) as f:
    for line in f:
        json_dat = json.loads(line)
        for i in range(2, len(args), 2):
            key = args[i]
            dat = args[i+1]
            if key in json_dat:
                json_dat[key] = dat
                print("{}, {}".format(key, dat))
        new_json_fp.write(json.dumps(json_dat) + os.linesep)

shutil.move(args[1], args[1] + ".bak")
shutil.move(new_json_fp.name, args[1])
