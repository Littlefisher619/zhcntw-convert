# -*- coding: utf-8 -*-

import zhconv
import sys
import os
import re

def convertToZhcn(inputTsPath, outTsPath,encoding='UTF-8',convertto='zh-cn'):
	with open(inputTsPath,'r', encoding=encoding) as f:
		content = f.read()
		with open(outTsPath,'w+',encoding=encoding) as f1:
			f1.write(zhconv.convert(content, convertto))


def batchConvert(path,savepath,convertto,encoding='UTF-8',namefilter='.*'):
	for dirpath, dirnames, filenames in os.walk(path):
		for filename in filenames:
			if not re.match(namefilter,filename):
				continue

			outfolder=os.path.join(savepath,dirpath)
			if not os.path.exists(outfolder):
				os.makedirs(outfolder)

			filepath=os.path.join(dirpath, filename)
			outpath=os.path.join(outfolder,filename)

			print(filepath,end='...')
			try:
				convertToZhcn(filepath,outpath,encoding=encoding)
				print("ok")
			except Exception as e:
				print("error")
				print(e)


			



batchConvert(r'Localization',r'trans',r'zh_cn',r'utf-16-le',r'.*\.CHT')
# convertToZhcn(r'buildings.CHT', r'buildings.zhcn.CHT',encoding='utf-16-le')
