from klokah.補充教材句型篇解析 import 補充教材句型篇解析
from collections import OrderedDict
from csv import DictWriter


class 補充教材句型篇動詞時態比較:
    _補充教材句型篇解析 = 補充教材句型篇解析()

    祈使對應表 = {'看': '看(如看電視、看東西)', '坐下': '坐著', '起立': '站著'}
    否定對應表 = {'看': '看(如看電視、看東西)'}

    欄位名 = ['華語', '肯定', '祈使', '否定']

    def 輸出檔案(self, 方言編號, 檔名):
        with open(檔名, 'w') as 檔案:
            輸出 = DictWriter(檔案, fieldnames=self.欄位名)
            輸出.writeheader()
            for 資料 in self.資料物件(方言編號).values():
                輸出.writerow(資料)

    def 資料物件(self, 方言編號):
        結果 = OrderedDict()
        for 族語, 華語 in self._取資料(方言編號, 14):  # 肯定資料
            結果[華語] = {'華語': 華語, '肯定': 族語}
        for 族語, 華語 in self._取資料(方言編號, 15):  # 祈使資料
            if 華語 in self.祈使對應表:
                華語 = self.祈使對應表[華語]
            結果[華語]['祈使'] = 族語
        for 族語, 華語 in self._取資料(方言編號, 211):  # 否定資料
            if 華語 in self.否定對應表:
                華語 = self.否定對應表[華語]
            結果[華語]['否定'] = 族語
        return 結果

    def _取資料(self, 方言編號, 項目編號):
        for 一筆 in self._補充教材句型篇解析.解析一個句型篇檔案('senior', 方言編號, 項目編號):
            yield 一筆['資料'][0]
