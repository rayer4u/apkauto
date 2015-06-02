# -*- coding: utf-8 -*-
from __future__ import print_function

import sys
from apk_auto import apk_auto

if __name__ == "__main__":
    label = ""
    if len(sys.argv) > 1:
        label = sys.argv[1]
    if label == "":
        print("请输入标签（无标签的包可能被删除，无需标签直接按回车）：".decode('utf-8'))
        label = raw_input()

    #label转码成utf8
    if sys.version_info[0] > 2:
        tp = str
    else:
        tp = unicode
    if isinstance(label, tp):
        label = label.encode('utf-8')
    else:
        if sys.stdin.encoding.lower() != 'utf-8':
            label = label.decode(sys.stdin.encoding).encode('utf-8')

    #print(label)
    apk_auto(label)
    print("结束，按回车退出。".decode('utf-8'))
    raw_input()
