#!/usr/bin/env python3

import os
import json


srcFile = os.path.join('src', 'webradios.json')
outFileM3U = 'cool-webradios.m3u'
outFileHTML = 'cool-webradios.html'

htmlHeaderTpl = '<!DOCTYPE html><html lang="en-US"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Cool Webradios</title></head><body><h1><a href="https://github.com/etrusci-org/cool-webradios">Cool Webradios</a></h1><ul>\n'
htmlFooterTpl = '</ul></body></html>'

def bake():
    with open(srcFile, 'r') as fSrc:
        print('loading data from {} ...'.format(srcFile))
        srcData = json.load(fSrc)
        bakeM3U(srcData)
        bakeHTML(srcData)
        print('done')


def bakeM3U(srcData):
    with open(outFileM3U, 'w') as fOut:
        print('writing to {} ...'.format(outFileM3U))
        fOut.write('#EXTM3U\n')
        for v in sorted(srcData, key=lambda v: v['name'].lower()):
            fOut.write('#EXTINF:0,{name}\n{listenURL}\n'.format(**v))


def bakeHTML(srcData):
    with open(outFileHTML, 'w') as fOut:
        print('writing to {} ...'.format(outFileHTML))
        fOut.write(htmlHeaderTpl)
        for v in sorted(srcData, key=lambda v: v['name'].lower()):
            fOut.write('<li><strong>{name}</strong><ul><li>website: <a href="{websiteURL}">{websiteURL}</a></li><li>tune-in: <a href="{listenURL}">{listenURL}</a></li></ul></li>\n'.format(**v))
        fOut.write(htmlFooterTpl)




if __name__ == '__main__':
    bake()
