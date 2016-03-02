# coding:utf-8
# http://stackoverflow.com/questions/23120974/python-requests-post-multipart-form-data-without-filename-in-http-request
from __future__ import print_function

import json
from os.path import basename
import requests
import sys

from .svn_getuser import getUser


def apk_post((p, f), label):
    #获取user
    user = getUser()

#     p, f, user = ('com.wunding.wdxuexi/3.2.0-wdxuexi-release-1501271726.apk',
#                 '/home/ray/develop/working/mlplayer4.0/branch/enterprise/'
#                 'android-padTmp/bin/mlplayer_ulp-release-unsigned.apk',
#                 'bh')
    if [p, f, user].count("") >= 1:
        print("error ", file=sys.stderr)
        print((p, f, user), file=sys.stderr)
    else:
        try:
            files = {'file': (basename(f), open(f, 'rb'),
                              'application/vnd.android.package-archive'),
                     'path': ('', p),
                     'user': ('', user)}
            if label != "":
                files['label'] = ('', label)
            files['certification'] = 'wunding.keystore'
            print("uploading...")
            print(files)
            print("")
            rep = requests.post("http://192.168.0.33/publish/apksign/",
                                files=files)
            if rep.status_code == 200:
                ret = json.loads(rep.content)
                if 'url' in ret:
                    print("success upload and sign. url is:")
                    print(ret['url'])
                    return ret['url']
                else:
                    print(rep.content, file=sys.stderr)
            else:
                print(rep.content, file=sys.stderr)
        except Exception, e:
            print(e, file=sys.stderr)
    return ""
