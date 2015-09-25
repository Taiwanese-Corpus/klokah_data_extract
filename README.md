# 族語E樂園

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
### 準備curl
```bash
```

### 準備python環境
```bash
virtualenv --python=python3 venv
. venv/bin/activate
pip install beautifulsoup4 lxml
```

### 下載資料
```bash
python 下載資料 程式/補充教材句型篇.py | bash
```