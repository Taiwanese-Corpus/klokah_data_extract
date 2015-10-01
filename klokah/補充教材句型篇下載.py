from itertools import product
from os.path import join, basename
from time import sleep
from urllib.request import urlopen

from bs4 import BeautifulSoup


from klokah.網站資訊 import 網站方言編號
from klokah.下載工具 import 下載
from klokah.網站資訊 import 專案目錄


class 句型篇下載:
    網站網址 = 'http://web.klokah.tw/extension/sp_data/'
    分級 = ['junior', 'senior']
    分類檔名 = 'classView.xml'

    def 一個一個下載(self):
        for 級 in self.分級:
            下載(
                self._分類檔網址(級),
                join(
                    專案目錄, '資料', '補充教材', 級, self.分類檔名
                )
            )
            for 方言, 項目 in product(
                    網站方言編號(),
                    self._項目編號(級)
            ):
                print(級, 方言, 項目)
                下載(
                    '{}/{}/{}/{}.xml'.format(self.網站網址, 級, 方言, 項目),
                    join(
                        專案目錄, '資料', '補充教材', 級, str(
                            方言), '{}.xml'.format(項目)
                    )
                )
                sleep(10)

    def 下載句型篇指令(self):
        指令 = []
        for 級 in self.分級:
            指令.extend(self._下載一個句型篇指令(join(self.網站網址, 級)))
        return 指令

    def _分類檔網址(self, 級):
        return join(self.網站網址, 級, self.分類檔名)

    def _項目編號(self, 級):
        項目編號 = []
        with urlopen(self._分類檔網址(級)) as 檔案:
            for 項目 in BeautifulSoup(檔案.read(), 'xml').find_all('classId'):
                項目編號.append(項目.get_text().strip())
        return 項目編號

    def _下載一個句型篇指令(self, 網址):
        項目編號 = []
        分類檔 = 'classView.xml'
        with urlopen(join(網址, 分類檔)) as 檔案:
            for 項目 in BeautifulSoup(檔案.read(), 'xml').find_all('classId'):
                項目編號.append(項目.get_text().strip())
        下載xml網址 = r'curl "{}/{{{}}}/{{{}}}.xml"  --create-dirs -o "資料/補充教材/{}/#1/#2.xml"'.format(
            網址,
            ','.join(網站方言編號()),
            ','.join(項目編號),
            basename(網址),
        )
        下載分類檔網址 = r'curl "{}"  --create-dirs -o "資料/補充教材/{}/{}"'.format(
            join(網址, 分類檔),
            basename(網址),
            分類檔
        )
        return 下載xml網址, 下載分類檔網址


print('\n'.join(句型篇下載().下載句型篇指令()))
句型篇下載().一個一個下載()
