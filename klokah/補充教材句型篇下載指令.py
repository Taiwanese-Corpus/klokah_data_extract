from bs4 import BeautifulSoup
from os.path import dirname, join, abspath, basename
from urllib.request import urlopen


class 句型篇下載:
    專案目錄 = join(dirname(abspath(__file__)), '..')

    def 下載句型篇指令(self, 網站網址):
        指令 = []
        for 級 in ['junior', 'senior']:
            指令.extend(self._下載一個句型篇指令(join(網站網址, 級)))
        return 指令

    def _下載一個句型篇指令(self, 網址):
        方言編號 = []
        with open(join(self.專案目錄, '資料', '補充教材', 'dialectView.xml')) as 檔案:
            for 方言 in BeautifulSoup(檔案.read(), 'xml').find_all('dialectId'):
                方言編號.append(方言.get_text().strip())
        項目編號 = []
        分類檔 = 'classView.xml'
        with urlopen(join(網址, 分類檔)) as 檔案:
            for 項目 in BeautifulSoup(檔案.read(), 'xml').find_all('classId'):
                項目編號.append(項目.get_text().strip())
        下載xml網址 = r'curl "{}/{{{}}}/{{{}}}.xml"  --create-dirs -o "資料/補充教材/{}/#1/#2.xml"'.format(
            網址,
            ','.join(方言編號),
            ','.join(項目編號),
            basename(網址),
        )
        下載分類檔網址 = r'curl "{}"  --create-dirs -o "資料/補充教材/{}/{}"'.format(
            join(網址, 分類檔),
            basename(網址),
            分類檔
        )
        return 下載xml網址,下載分類檔網址


print('\n'.join(句型篇下載().下載句型篇指令('http://web.klokah.tw/extension/sp_data/')))
