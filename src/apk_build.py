# coding:utf-8
from __future__ import print_function

import os
import re
import subprocess
import sys


def apk_build(cfg):

    rule = re.compile(
        r"^.+\s+post-to-server upload path is ([A-Za-z0-9\.\-\/\_]+)"
        r" and upload file is ([A-Za-z0-9\.\-\_\/\\\:]+)")
    p = subprocess.Popen('ant auto-release '+'-Dcfg=ant'+cfg+'.properties',
                         stdout=subprocess.PIPE, env=os.environ, shell=True)

    path = ''
    f = ''
    while True:
        line = p.stdout.readline()
        if not line:
            break
        print(line)

        mt = rule.match(line)
        if mt:
            path = mt.group(1)
            f = mt.group(2)

    err = p.wait()
    if err != 0:
        print("apk build failed", file=sys.stderr)
        return ('', '')

    return (path, f)
