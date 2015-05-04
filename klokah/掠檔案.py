from xml.etree import ElementTree
import os

if __name__ == '__main__':
	全部檔案位置 = ['http://klokah-file.com/017/{0:02}_junior_offline.zip',
		'http://klokah-file.com/018/{0:02}_senior_offline.zip',
		]
	for 檔案位置 in 全部檔案位置:
		for 編號 in range(1,44):
			檔案=檔案位置.format(編號)
			os.system("wget {0}".format(檔案))
	