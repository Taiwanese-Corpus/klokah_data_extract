from bs4 import BeautifulSoup
from os.path import dirname, join, abspath


class 句型篇解析:
    專案目錄 = join(dirname(abspath(__file__)), '..', '..')

    def 解析一個句型篇檔案(self, 級, 方言編號, 檔案編號):
        資料陣列 = []
        with open(join(self.專案目錄, '資料', '補充教材', 級, str(方言編號), str(檔案編號) + '.xml')) as 檔案:
            for 方言 in BeautifulSoup(檔案.read(), 'lxml').find_all('item'):
                一筆資料 = {}
                for 資料內容 in 方言.find_all(True):
                    一筆資料[資料內容.name] = 資料內容.get_text(strip=True)
                資料陣列.append(一筆資料)
        return 資料陣列

print(句型篇解析().解析一個句型篇檔案('senior', 2, 16))
