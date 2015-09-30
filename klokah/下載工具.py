import io
from os import makedirs
from os.path import dirname, isdir

import pycurl


def 下載(網址, 檔名):
    下載物件 = pycurl.Curl()
    下載物件.setopt(pycurl.URL, 網址)
    with io.BytesIO() as 緩衝:
        下載物件.setopt(pycurl.WRITEDATA, 緩衝)
        下載物件.setopt(pycurl.MAXREDIRS, 10)
        下載物件.setopt(pycurl.ENCODING, 'gzip, deflate')
        # if redirected, follow it
        下載物件.setopt(pycurl.FOLLOWLOCATION, True)
        下載物件.perform()
        下載物件.close()
        目錄 = dirname(檔名)
        if not isdir(目錄):
            makedirs(目錄)
        with io.open(檔名, 'w') as 檔案:
            print(緩衝.getvalue().decode('utf-8'), file=檔案)
