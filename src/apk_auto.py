# -*- coding: utf-8 -*-

import sys

from apk_build import apk_build
from apk_post4sign import apk_post

def apk_auto(label):
#     os.chdir("/home/ray/develop/working/mlplayer4.0/branch/enterprise/android-pad")
    apk_post(apk_build(),label)
    
