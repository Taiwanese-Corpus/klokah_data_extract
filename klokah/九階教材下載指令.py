from bs4 import BeautifulSoup
from builtins import map
from os.path import dirname, join, abspath
from urllib.parse import urlparse


class 九階教材下載:
    專案目錄 = join(dirname(abspath(__file__)), '..')

    def 下載指令(self, 網站網址, 學習頁面網址):
        方言編號 = []
        with open(join(self.專案目錄, '資料', '補充教材', 'dialectView.xml')) as 檔案:
            for 方言 in BeautifulSoup(檔案.read(), 'xml').find_all('dialectId'):
                方言編號.append(方言.get_text().strip())
        下載xml網址 = r'curl "{}?d={{{}}}&l={{{}}}&c={{{}}}"  --create-dirs -o "資料/九階教材/#1/#2_#3.xml" -H "Host: {}" -e {} -w 2'.format(
            網站網址,
            ','.join(方言編號),
            ','.join(map(str, range(1, 10))),
            ','.join(map(str, range(1, 11))),
            urlparse(學習頁面網址).netloc,
            學習頁面網址,
        )
        return 下載xml網址


print(九階教材下載().下載指令(
    'http://web.klokah.tw/nine/php/getText.php',
    'http://web.klokah.tw/nine/learn.php'
))
