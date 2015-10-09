# 族語E樂園

原住民族委員會，為了解決原住民族語瀕危困境，並落實原住民族教育法第21條「對學前教育之原住民學生提供其學習族語、歷史及文化之機會」，原民會參考了國外毛利語、夏威夷語及屏東縣客語沉浸式教學幼兒園之經驗，確立族語復振邁入「向下扎根」的新方向，培育出族語沉浸式教學師資、研發族語沉浸式教學教材及發展出都會型、原鄉型、瀕危型幼兒園族語沉浸式教學模式外，更希望透過本計畫之成果效益評估作為未來全面推廣之參據。

族語數位中心聯絡信箱: pqwasan@gmail.com
族語學習入口網站 : http://klokah.tw/

## 資料種類
* 九階教材
  * 九階 x 十課
  * 有族語句、華語翻譯句、族語句聲音檔
* 補充教材句型篇
  * 10種格式，有句有詞
  * 有族語、華語翻譯、族語聲音檔
    * 族語聲音可能包含許多多詞，許多多句
  * 語者姓名
    * 「資源下載-教材檔案-【句型篇】學習手冊（中級）」最後一頁
  * 編號意義
    * 「資源下載-數位教具-【句型篇】離線版學習系統」壓縮檔拆開
* 補充教材歌謠篇
  * 有歌謠音檔
  * 有逐句族語歌詞跟華語逐句翻譯
    * http://web.klokah.tw/video/song_embed.php?vid=1191
* 補充教材生活會話篇
  * 有逐句會話音檔
  * 有逐句族語歌詞跟華語逐句翻譯
    * http://web.klokah.tw/extension/con_data/xml/42/conversation.xml
* 補充教材圖畫故事篇
  * 有音檔
  * 族語文章和華語文章是圖片，需人工手打
* 補充教材閱讀書寫篇
  * 有音標、族語文章和華語文章
* 影音中心
  * 有音檔，標時間的族語語句跟華語語句
    * http://web.klokah.tw/video/watch.php?vid=2945
* 資源下載-教材檔案-千詞表
  * 「【千詞表】學習手冊」有族語和華語解釋
  * 「【千詞表】音檔」有音標
  
## 產生檔案
### 準備python環境
```bash
sudo apt-get install -y python3 python-virtualenv g++ python-dev libxml2-dev libxslt1-dev libcurl4-openssl-dev
virtualenv --python=python3 venv
. venv/bin/activate
pip install beautifulsoup4 lxml pyyaml
```

### 下載資料
```bash
PYTHONPATH=. python klokah/九階教材下載.py
PYTHONPATH=. python klokah/補充教材句型篇下載.py
```

### 輸出文字語料
```bash
PYTHONPATH=. python klokah/輸出對齊語料.py
PYTHONPATH=. python klokah/輸出動詞語料.py
```

### 臺灣言語資料庫
#### 產生檔案
```bash
PYTHONPATH=. python klokah/轉到臺灣言語資料庫.py
```

#### 匯入檔案
```bash
python manage.py 匯入資料 http://Taiwanese-Corpus.github.io/klokah_data_extract/族語E樂園.yaml
```

## 開發

### 試驗
```bash
python -m unittest
```