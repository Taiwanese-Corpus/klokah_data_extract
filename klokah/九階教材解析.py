from bs4 import BeautifulSoup
from os.path import dirname, join, abspath
from klokah.網站資訊 import 專案目錄
from itertools import product


class 九階教材解析:

    def 解析全部檔案(self):
        with open(join(專案目錄, '資料', 'dialectView.xml')) as 檔案:
            for 方言 in BeautifulSoup(檔案.read(), 'xml').find_all('item'):
                語言名 = 方言.find('languageCh').get_text(strip=True)
                方言編號 = 方言.find('dialectId').get_text(strip=True)
                方言名 = 方言.find('dialectCh').get_text(strip=True)
                for 一筆資料 in self.解析一個方言檔案(方言編號):
                    一筆資料['languageCh'] = 語言名
                    一筆資料['dialectCh'] = 方言名
                    yield 一筆資料

    def 解析一個方言檔案(self, 方言編號):
        for 階, 課 in product(range(1, 10), range(1, 11)):
            for 一筆資料 in self.解析一個句型篇檔案(方言編號, 階, 課):
                yield 一筆資料

    def 解析一個句型篇檔案(self, 方言編號, 階, 課):
        資料陣列 = []
        with open(join(專案目錄, '資料', '九階教材', str(方言編號), '{}_{}.xml'.format(階, 課))) as 檔案:
            xml資料 = BeautifulSoup(檔案.read(), 'xml')
            標題 = {
                'title': xml資料.title.get_text(strip=True),
                'titleCh': xml資料.titleCh.get_text(strip=True)
            }
            for 方言 in xml資料.find_all('item'):
                一筆資料 = {}
                for 資料內容 in 方言.find_all(True):
                    一筆資料[資料內容.name] = 資料內容.get_text(strip=True)
                一筆資料.update(標題)
                資料陣列.append(一筆資料)
        return 資料陣列
