import yaml
from klokah.九階教材解析 import 九階教材解析
from klokah.補充教材句型篇解析 import 補充教材句型篇解析


class 轉到臺灣言語資料庫:
    目標檔名 = '族語E樂園.yaml'

    def 轉成資料庫yaml(self):
        全部資料 = {
            '來源': {'名': '族語E樂園'},
            '版權': 'Creative Commons 姓名標示-非商業性 3.0 Unported License',
            '著作所在地': '臺灣',
            '著作年': '1996',
            '相關資料組': [],

        }
        相關資料組 = 全部資料['相關資料組']
        for 族語, 華語, 方言, 種類 in self._全部族語華語對齊詞條():
            這筆資料 = {
                '語言腔口': 方言,
                '種類': 種類,
                '外語語言': '華語',
                '外語資料': 華語,
                '下層': [{'文本資料': 族語}],
            }
            相關資料組.append(這筆資料)
        with open(self.目標檔名, 'w') as 檔案:
            yaml.dump(全部資料, 檔案, default_flow_style=False, allow_unicode=True)

    def _全部族語華語對齊詞條(self):
        for 結果 in self._九階():
            yield 結果
        for 結果 in self._補充句型篇():
            yield 結果

    def _九階(self):
        上一個標題 = None
        for 一筆資料 in 九階教材解析().解析全部檔案():
            族語標題, 華語標題 = 一筆資料['title'], 一筆資料['titleCh']
            if 上一個標題 != (族語標題, 華語標題):
                yield ' '.join(族語標題.split()), 華語標題, 一筆資料['dialectCh'], '語句'
                上一個標題 = (族語標題, 華語標題)
            族語, 華語 = 一筆資料['text'], 一筆資料['chinese']
            yield ' '.join(族語.split()), 華語, 一筆資料['dialectCh'], '語句'

    def _補充句型篇(self):
        for 一筆資料 in 補充教材句型篇解析().解析全部檔案():
            if type == '1':
                種類 = '字詞'
            else:
                種類 = '語句'
            for 族語, 華語 in 一筆資料['資料']:
                yield ' '.join(族語.split()), 華語, 一筆資料['dialectCh'], 種類

轉到臺灣言語資料庫().轉成資料庫yaml()
