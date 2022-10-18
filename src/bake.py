#!/usr/bin/env python3

import os
import json


srcFile = os.path.join('src', 'webradios.json')
outFileM3U = 'cool-webradios.m3u'
outFileHTML = 'cool-webradios.html'
htmlPageTplFile = os.path.join('src', 'html-page.tpl')
htmlPageStyleTplFile = os.path.join('src', 'html-page-style.tpl')
htmlListTplFile = os.path.join('src', 'html-list.tpl')
htmlListItemTplFile = os.path.join('src', 'html-list-item.tpl')




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
            fOut.write('#EXTINF:0,{name} - {about} [{websiteURL}]\n{listenURL}\n'.format(**v))


def bakeHTML(srcData):
    with open(outFileHTML, 'w') as fOut, \
         open(htmlPageTplFile, 'r') as fPageTpl, \
         open(htmlPageStyleTplFile, 'r') as fPageStyleTpl, \
         open(htmlListTplFile, 'r') as fListTpl, \
         open(htmlListItemTplFile, 'r') as fListItemTpl:
        print('loading template from {} ...'.format(htmlPageTplFile))
        htmlPageTpl = fPageTpl.read()
        print('loading template from {} ...'.format(htmlPageStyleTplFile))
        htmlPageStyleTpl = fPageStyleTpl.read()
        print('loading template from {} ...'.format(htmlListTplFile))
        htmlListTpl = fListTpl.read()
        print('loading template from {} ...'.format(htmlListItemTplFile))
        htmlListItemTpl = fListItemTpl.read()
        listItems = ''
        for v in sorted(srcData, key=lambda v: v['name'].lower()):
            listItems += htmlListItemTpl.format(**v)
        htmlList = htmlListTpl.format(listItems=listItems)
        htmlPage = htmlPageTpl.format(list=htmlList, style=htmlPageStyleTpl)
        print('writing to {} ...'.format(outFileHTML))
        fOut.write(htmlPage)




if __name__ == '__main__':
    bake()
