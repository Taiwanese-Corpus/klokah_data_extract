from xml.etree import ElementTree

class 文件檔資料擷取:
	def 列出(self, 檔案位置):
		try:
			return self.列出對話資料(檔案位置)
		except:
			pass
		try:
			return self.列出對話資料(檔案位置)
		except:
			pass
	def 列出對話資料(self, 檔案位置):
		樹 = ElementTree.parse(檔案位置)
		根 = 樹.getroot()
		for item in 根:
			# 檢查type
			資料編號 = self._找出元素資料(item, 'sentenceOrder')
			資料 = []
			
			族語資料 = [
				self._找出元素資料(item, 'sentenceAAb'),
				self._找出元素資料(item, 'sentenceBAb'),
				self._找出元素資料(item, 'sentenceCAb'),
				]
			華語資料 = [
				self._找出元素資料(item, 'sentenceACh'),
				self._找出元素資料(item, 'sentenceBCh'),
				self._找出元素資料(item, 'sentenceCCh'),
				]
			for 族語, 華語 in zip(族語資料, 華語資料):
				if 族語:
					資料.append((族語.strip(), 華語.strip()))
			yield 資料編號, 資料
	def _找出元素資料(self, 物件, 底下tag):
		結果 = 'None'
		for 編號, 資料 in enumerate(物件.iter(底下tag)):
			結果 = 資料.text
			if 編號 > 0:
				raise RuntimeError('資料超過一個！！')
		if 結果 == 'None':
			raise RuntimeError('沒此子資料！！')
		return 結果

if __name__ == '__main__':
	檔案位置 = '/home/tshau/klokah資料/全部語料/senior/xml/{0}/{1}.xml'
	語言編號 = '03'
	分類號碼 = [18]
	for 號碼 in 分類號碼:
		for 資料編號, 資料 in 文件檔資料擷取()\
				.列出對話資料(檔案位置.format(語言編號, 號碼)):
			print('{}_{}'.format(號碼, 資料編號))
			for 族語, _ in 資料:
				print(族語)
			print()
	for 號碼 in 分類號碼:
		for 資料編號, 資料 in 文件檔資料擷取()\
				.列出對話資料(檔案位置.format(語言編號, 號碼)):
			print('{}_{}'.format(號碼, 資料編號))
			for _, 華語 in 資料:
				print(華語)
			print()
