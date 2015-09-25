from bs4 import BeautifulSoup
from os.path import dirname, join, abspath


class 句型篇解析:
    專案目錄 = join(dirname(abspath(__file__)), '..', '..')

    def 解析一個方言檔案(self, 方言編號):
        for 級 in ['junior', 'senior']:
            with open(join(self.專案目錄, '資料', '補充教材', 級, 'classView.xml')) as 檔案:
                for 檔案標仔 in BeautifulSoup(檔案.read(), 'xml').find_all('classId'):
                    for 一筆資料 in self.解析一個句型篇檔案(級, 方言編號, 檔案標仔.get_text(strip=True)):
                        yield 一筆資料

    def 解析一個句型篇檔案(self, 級, 方言編號, 檔案編號):
        資料陣列 = []
        with open(join(self.專案目錄, '資料', '補充教材', 級, str(方言編號), str(檔案編號) + '.xml')) as 檔案:
            for 方言 in BeautifulSoup(檔案.read(), 'xml').find_all('item'):
                一筆資料 = {}
                for 資料內容 in 方言.find_all(True):
                    一筆資料[資料內容.name] = 資料內容.get_text(strip=True)
                資料陣列.append(self._資料欄位正規化(一筆資料))
        return 資料陣列

    def _資料欄位正規化(self, 資料):
        正規化函式 = {
            '1': self._一基本詞彙,
            '2': self._二生活百句,
            '3': self._三看圖識字,
            '4': self._四選擇題一,
            '5': self._五選擇題二,
            '6': self._六配合題,
            '7': self._七選擇題三,
            '8': self._八唸唸看,
            '9': self._九簡短對話,
            '10': self._十看圖說話,
        }
        正規化函式[資料['typeId']](資料)
        return 資料

    def _一基本詞彙(self, 資料):
        資料['資料'] = [(資料['wordAb'], 資料['wordCh'])]

    def _二生活百句(self, 資料):
        self._傳欄位名正規化(
            [
                ('sentenceAAb', 'sentenceACh'),
                ('sentenceBAb', 'sentenceBCh'),
                ('sentenceCAb', 'sentenceCCh'),
            ],
            資料
        )

    def _三看圖識字(self, 資料):
        資料['資料'] = [(資料['recognizeAb'], 資料['recognizeCh'])]

    def _四選擇題一(self, 資料):
        self._傳欄位名正規化(
            [
                ('choiceOneAAb', 'choiceOneACh'),
                ('choiceOneBAb', 'choiceOneBCh'),
                ('choiceOneCAb', 'choiceOneCCh'),
            ],
            資料
        )

    def _傳欄位名正規化(self, 欄位對照, 資料):
        資料陣列 = []
        for 族欄位, 華欄位 in 欄位對照:
            if 資料[族欄位]:
                資料陣列.append((資料[族欄位], 資料[華欄位]))
        資料['資料'] = 資料陣列

    def _五選擇題二(self, 資料):
        self._傳欄位名正規化(
            [
                ('choiceTwoAAb', 'choiceTwoACh'),
                ('choiceTwoBAb', 'choiceTwoBCh'),
                ('choiceTwoCAb', 'choiceTwoCCh'),
            ],
            資料
        )

    def _六配合題(self, 資料):
        self._傳欄位名正規化(
            [
                ('matchAAbA', 'matchAChA'),
                ('matchAAbB', 'matchAChB'),
                ('matchBAbA', 'matchBChA'),
                ('matchBAbB', 'matchBChB'),
                ('matchCAbA', 'matchCChA'),
                ('matchCAbB', 'matchCChB'),
                ('matchDAbA', 'matchDChA'),
                ('matchDAbB', 'matchDChB'),
                ('matchEAbA', 'matchEChA'),
                ('matchEAbB', 'matchEChB'),
            ],
            資料
        )

    def _七選擇題三(self, 資料):
        資料['資料'] = [(資料['choiceThreeAb'], 資料['choiceThreeCh'])]

    def _八唸唸看(self, 資料):
        self._傳欄位名正規化(
            [
                ('oralReadingAAb', 'oralReadingACh'),
                ('oralReadingBAb', 'oralReadingBCh'),
                ('oralReadingCAb', 'oralReadingCCh'),
                ('oralReadingDAb', 'oralReadingDCh'),
                ('oralReadingEAb', 'oralReadingECh'),
            ],
            資料
        )

    def _九簡短對話(self, 資料):
        self._傳欄位名正規化(
            [
                ('dialogueAAb', 'dialogueACh'),
                ('dialogueBAb', 'dialogueBCh'),
                ('dialogueCAb', 'dialogueCCh'),
                ('dialogueDAb', 'dialogueDCh'),
                ('dialogueEAb', 'dialogueECh'),
            ],
            資料
        )

    def _十看圖說話(self, 資料):
        self._傳欄位名正規化(
            [
                ('pictureTalkAb', 'pictureTalkCh'),
            ],
            資料
        )

print(句型篇解析().解析一個句型篇檔案('senior', 2, 16))
for a in 句型篇解析().解析一個方言檔案(2):
    print(a)
