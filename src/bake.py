#!/usr/bin/env python3

import os
import json

srcFile = os.path.join('src', 'm3u.json')
outFile = 'cool-webradios.m3u'


def bake():
    with open(srcFile, 'r') as fSrc:
        data = json.load(fSrc)
        with open(outFile, 'w') as fOut:
            fOut.write('#EXTM3U\n')
            for v in sorted(data, key=lambda v: v['name'].lower()):
                fOut.write('#EXTINF:0,{name}\n{url}\n'.format(**v))




if __name__ == '__main__':
    bake()
