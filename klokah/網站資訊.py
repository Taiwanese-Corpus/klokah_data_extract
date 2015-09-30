from os.path import join, dirname, abspath

from bs4 import BeautifulSoup


專案目錄 = join(dirname(abspath(__file__)), '..')


def 網站方言編號():
    方言編號 = []
    with open(join(專案目錄, '資料', 'dialectView.xml')) as 檔案:
        for 方言 in BeautifulSoup(檔案.read(), 'xml').find_all('dialectId'):
            方言編號.append(方言.get_text().strip())
    return 方言編號
