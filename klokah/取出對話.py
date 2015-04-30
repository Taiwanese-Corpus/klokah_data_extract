from xml.etree import ElementTree

class 文件檔資料擷取:
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
					資料.append((族語, 華語))
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
	檔案位置 = '/home/tshau/下載/南排/26原住民學生補充教材離線系統（高中版）/senior/xml/3/16.xml'
	for 資料編號, 資料 in 文件檔資料擷取().列出對話資料(檔案位置):
		print(資料編號)
		for 族語, _ in 資料:
			print(族語)
		print()
	for 資料編號, 資料 in 文件檔資料擷取().列出對話資料(檔案位置):
		print(資料編號)
		for _, 華語 in 資料:
			print(華語)
		print()
