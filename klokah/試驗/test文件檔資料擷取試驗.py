# -*- coding: utf-8 -*-
import os
from os.path import join
from unittest.case import TestCase


from klokah.取出對話 import 文件檔資料擷取


class 文件檔資料擷取試驗(TestCase):
	def setUp(self):
		這馬目錄 = os.path.dirname(os.path.abspath(__file__))
		self.資料目錄 = os.path.join(這馬目錄, '語料')
		self.擷取=文件檔資料擷取()
	def tearDown(self):
		pass
	def test_掠對話資料長度(self):
		資料=self.擷取.列出(join(self.資料目錄,'19.xml'))
		self.assertEqual(len(list(資料)),11)
	def test_掠對話資料(self):
		資料=self.擷取.列出(join(self.資料目錄,'19.xml'))
		for 迴圈編號,(資料編號,對應) in enumerate(資料):
			self.assertEqual(迴圈編號+1, int(資料編號))
			for 秀姑巒,華 in 對應:
				self.assertIsInstance(秀姑巒, str)
				self.assertIsInstance(華, str)
		