from builtins import map
from itertools import product
from os.path import join, isdir


from klokah.網站資訊 import 網站方言編號
from klokah.下載工具 import 下載
from klokah.網站資訊 import 專案目錄
from time import sleep
from os import makedirs


class 九階教材下載:
    網站網址 = 'http://web.klokah.tw/nine/php/getText.php'

    def 一個一個下載(self):
        for 方言, 階, 課 in product(
            網站方言編號(),
            range(1, 10),
            range(1, 11)
        ):
            print(方言, 階, 課)
            資料目錄 = join(專案目錄, '資料', '九階教材', str(方言))
            if not isdir(資料目錄):
                makedirs(資料目錄)
            下載(
                '{}?d={}&l={}&c={}'.format(self.網站網址, 方言, 階, 課),
                join(資料目錄, '{}_{}.xml'.format(階, 課))
            )
            sleep(10)

    def 下載指令(self):
        下載xml網址 = r'curl "{}?d={{{}}}&l={{{}}}&c={{{}}}"  --create-dirs -o "資料/九階教材/#1/#2_#3.xml"'.format(
            self.網站網址,
            ','.join(網站方言編號()),
            ','.join(map(str, range(1, 10))),
            ','.join(map(str, range(1, 11))),
        )
        return 下載xml網址


print(九階教材下載().下載指令())
九階教材下載().一個一個下載()
