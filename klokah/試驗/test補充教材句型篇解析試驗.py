from unittest.case import TestCase
from klokah.補充教材句型篇解析 import 補充教材句型篇解析


class 補充教材句型篇解析試驗(TestCase):

    def setUp(self):
        self.解析 = 補充教材句型篇解析()

    def test_一個檔(self):
        self.解析.解析一個句型篇檔案('senior', 2, 16)

    def test_一個方言(self):
        for _一筆 in self.解析.解析一個方言檔案(2):
            pass

    def test_全部(self):
        for _一筆 in self.解析.解析全部檔案():
            pass
