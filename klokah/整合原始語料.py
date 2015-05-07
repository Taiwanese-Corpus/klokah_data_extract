import os
import shutil
import filecmp

def 複製到目的(資料夾, 目標):
	聲音資料夾 = os.listdir(os.path.join(資料夾, 'sound'))
	if len(聲音資料夾) != 1:
		raise RuntimeError('聲音資料夾毋是一個' + str(聲音資料夾))
	編號 = 聲音資料夾[0]
	print(編號, 資料夾, 目標,)
	shutil.rmtree(os.path.join(目標, 'sound', '{0:02}'.format(int(編號))),
		ignore_errors=True)		
	shutil.copytree(os.path.join(資料夾, 'sound', 編號),
				os.path.join(目標, 'sound', '{0:02}'.format(int(編號))))
	
	shutil.rmtree(os.path.join(目標, 'xml', '{0:02}'.format(int(編號))),
		ignore_errors=True)		
	shutil.copytree(os.path.join(資料夾, 'xml', 編號),
				os.path.join(目標, 'xml', '{0:02}'.format(int(編號))))
	
	for 通用檔案 in ['classView.xml', 'dialectView.xml',
				'languageView.xml', 'typeView.xml']:
		比較複製(os.path.join(資料夾, 'xml', 通用檔案), os.path.join(目標, 'xml', 通用檔案))

def 比較複製(來源, 目標):
	if not os.path.isfile(目標):
		shutil.copy(來源, 目標)
	if not filecmp.cmp(來源, 目標):
		print('檔案不一樣：{}，{}'.format(來源, 目標))

if __name__ == '__main__':
	目標路徑 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	for 	路徑, 資料夾名, 檔案名 in os.walk(os.path.dirname(os.path.abspath(__file__))):
		if 'practice' in 資料夾名:
			if 'junior' in 資料夾名:
				等級 = 'junior'
			elif 'senior' in 資料夾名:
				等級 = 'senior'
			else:
				continue
			複製到目的(os.path.join(os.path.abspath(路徑), 等級),
				os.path.join(目標路徑, '全部語料', 等級))
	
