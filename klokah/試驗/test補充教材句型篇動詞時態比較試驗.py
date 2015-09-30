from collections import OrderedDict
from unittest.case import TestCase
from klokah.補充教材句型篇動詞時態比較 import 補充教材句型篇動詞時態比較


class 補充教材句型篇動詞時態比較試驗(TestCase):

    def setUp(self):
        self.時態比較 = 補充教材句型篇動詞時態比較()

    def test_傳出資料檔(self):
        self.物件對照(
            self.時態比較.資料物件(2),
            OrderedDict([
                ('好(見面問候用)', {'肯定': "nga'ay ho", '華語': '好(見面問候用)'}),
                ('再見', {'肯定': "'arayom", '華語': '再見'}),
                ('謝謝', {'肯定': 'aray', '華語': '謝謝'}),
                ('來', {'否定': 'katayni / kati', '祈使': 'katayni',
                       '肯定': 'tayni / ati', '華語': '來'}),
                ('要來', {'肯定': 'tatayni', '華語': '要來'}),
                ('來過', {'肯定': 'tayniay to', '華語': '來過'}),
                ('去', {'否定': 'katayra / oli', '祈使': 'katayra',
                       '肯定': 'tayra / oli', '華語': '去'}),
                ('要去', {'肯定': 'tatayra', '華語': '要去'}
                 ), ('去了', {'肯定': 'tayra to', '華語': '去了'}),
                ('去過', {'肯定': 'natayra to / tayraay to', '華語': '去過'}),
                ('出現；出來', {'否定': 'kasadak', '肯定': 'masadak', '華語': '出現；出來'}),
                ('吃(東西)', {
                 '否定': 'kakomaen', '祈使': 'kakomaen', '肯定': 'komaen', '華語': '吃(東西)'}),
                ('起床', {
                 '否定': 'kalomowad', '祈使': 'kalomowad', '肯定': 'lomowad', '華語': '起床'}),
                ('睡覺', {
                 '否定': "kafoti'", '祈使': "kafoti'", '肯定': "mafoti'", '華語': '睡覺'}),
                ('讀書', {'否定': 'piasip to codad / micodad', '祈使':
                        'piasip to codad / picodad', '肯定': 'miasip to codad', '華語': '讀書'}),
                ('唱歌', {
                 '否定': 'karomadiw', '祈使': 'karomadiw', '肯定': 'romadiw', '華語': '唱歌'}),
                ('跳舞', {
                 '否定': 'kasakero', '祈使': 'kasakero', '肯定': 'masakero', '華語': '跳舞'}),
                ('畫圖', {
                 '否定': 'pirenaf', '祈使': 'pirenaf', '肯定': 'mirenaf', '華語': '畫圖'}),
                ('玩耍', {'否定': 'pisalama', '祈使':
                        'misalama', '肯定': 'misalama', '華語': '玩耍'}),
                ('洗(如洗澡)', {'否定': 'pililoc / pingingoy', '祈使': 'mililoc /mingingoy',
                            '肯定': 'mililoc / mingingoy', '華語': '洗(如洗澡)'}),
                ('洗(如洗臉)', {
                 '否定': "kalalo'op", '祈使': "malalo'op", '肯定': "malalo'op", '華語': '洗(如洗臉)'}),
                ('洗(如洗衣服)', {
                 '否定': "pifaca'", '祈使': "mifaca'", '肯定': "mifaca'", '華語': '洗(如洗衣服)'}),
                ('生病', {'否定': 'kaadada', '肯定': 'adada', '華語': '生病'}),
                ('痛(如頭痛)', {'否定': 'kaadada(ko tangal)', '肯定': 'adada / taroktok',
                            '華語': '痛(如頭痛)'}),
                ('攜帶(如帶傘)', {'否定': 'pihawikid(to linay)', '祈使': 'pihawikid',
                             '肯定': 'ci linay / mihawikid (to linay)', '華語': '攜帶(如帶傘)'}),
                ('下雨', {'否定': "ka'orad", '肯定': "ma'orad", '華語': '下雨'}),
                ('說', {
                 '否定': 'kasomowal', '祈使': 'kasomowal', '肯定': 'somowal', '華語': '說'}),
                ('聽', {
                 '否定': 'pitengil', '祈使': 'mitengil', '肯定': 'mitengil', '華語': '聽'}),
                ('看(如看電視、看東西)', {'肯定': 'minengneng', '華語': '看(如看電視、看東西)'}),
                ('看起來', {
                    '肯定': "nengneng han / 'araw han", '華語': '看起來'}),
                ('拜訪；探望', {'肯定': "miliso'", '華語': '拜訪；探望'}),
                ('喜歡', {'否定': 'kaolah', '肯定': 'maolah', '華語': '喜歡'}),
                ('會；能(做某事)', {
                 '否定': "kafana'", '肯定': "mafana'", '華語': '會；能(做某事)'}),
                ('可以(做某事)', {'肯定': "manga'ay", '華語': '可以(做某事)'}),
                ('遲到', {'肯定': 'maapac', '華語': '遲到'}),
                ('隨便', {'肯定': "pacefa' / simaan", '華語': '隨便'}),
                ('浪費', {'肯定': "mila'om", '華語': '浪費'}),
                ('大', {'否定': "katata'ak / katata'ang", '肯定':
                       "tata'ak / tata'ang",     '華語': '大'}),
                ('小', {'否定': 'kamamang', '肯定': 'mamang', '華語': '小'}),
                ('多', {'否定': "kaadihay (指物件) / ka'aloman (指人)",
                       '肯定': "adihay (指物件) / 'aloman (指人)", '華語': '多'}),
                ('少', {'否定': 'kamamang', '肯定': 'mamang', '華語': '少'}),
                ('重', {'否定': 'kakareteng / kafaeket',
                       '肯定': 'kareteng / faeket', '華語': '重'}),
                ('輕', {'否定': 'kadahemaw / kakahemaw',
                       '肯定': 'dahemaw / kahemaw', '華語': '輕'}),
                ('長', {'否定': "kakaya' / kararaya'",
                       '肯定': "kakaya' / raraya'", '華語': '長'}),
                ('短', {'否定': "kamamoko' / kamamoyo'",
                       '肯定': "mamoko' / papoyo'", '華語': '短'}),
                ('高', {'否定': 'katakaraw', '肯定': 'takaraw', '華語': '高'}),
                ('矮', {'否定': 'kapoener', '肯定': 'poener', '華語': '矮'}),
                ('低', {'否定': 'kapoener', '肯定': 'apener / laeno', '華語': '低'}),
                ('美麗；好看；漂亮', {
                 '否定': 'kamakapah', '肯定': 'makapah', '華語': '美麗；好看；漂亮'}),
                ('英俊', {'否定': 'katanestes', '肯定': 'tanestes', '華語': '英俊'}),
                ('快樂', {'否定': 'kalipahak', '肯定': 'lipahak', '華語': '快樂'}),
                ('勤勞', {'否定': 'kalalok', '肯定': 'malalok', '華語': '勤勞'}),
                ('懶惰', {'否定': 'katoka', '肯定': 'matoka', '華語': '懶惰'}),
                ('在(這裡)', {'肯定': 'i tini', '華語': '在(這裡)'}),
                ('在', {'肯定': 'i', '華語': '在'}),
                ('有；擁有', {'肯定': 'ira', '華語': '有；擁有'}),
                ('穿(如穿衣服)', {
                 '否定': "pica'edong", '祈使': "pica'edong", '肯定': "mica'edong", '華語': '穿(如穿衣服)'}),
                ('戴(如戴帽子)', {'否定': 'kacikafong', '祈使': 'kacikafong', '肯定': 'cikafong', '華語': '戴(如戴帽子)'}
                 ), ('走路', {'否定': 'karomakat', '祈使': 'karomakat', '肯定': 'romakat', '華語': '走路'}),
                ('出去', {
                 '否定': 'kasadak', '祈使': 'kasadak', '肯定': 'masadak', '華語': '出去'}),
                ('坐著', {'肯定': "maro'", '華語': '坐著'}),
                ('站著', {'肯定': 'tomireng', '華語': '站著'}),
                ('吃早餐', {'肯定': 'maranam', '華語': '吃早餐'}),
                ('吃午餐', {'肯定': 'malahok', '華語': '吃午餐'}),
                ('吃晚餐', {'肯定': 'malafi', '華語': '吃晚餐'}),
                ('(日)落', {'肯定': 'micelem ( ko cidal)', '華語': '(日)落'}),
                ('天黑', {'肯定': "to'eman", '華語': '天黑'}),
                ('雨停', {'肯定': "masalaw ( ko 'orad)", '華語': '雨停'}),
                ('刮颱風', {'肯定': 'mafaliyos', '華語': '刮颱風'}),
                ('炎熱', {'否定': 'kafaedet', '肯定': 'faedet', '華語': '炎熱'}),
                ('冷', {
                 '否定': 'kasienaw', '肯定': 'sienaw( 指天氣) / lietec(指東西)', '華語': '冷'}),
                ('開(門、窗)', {'肯定': 'mifohat / mafawah', '華語': '開(門、窗)'}),
                ('關(門、窗)', {'肯定': "mi'edef", '華語': '關(門、窗)'}),
                ('閉(眼睛)', {'肯定': 'mafotek', '華語': '閉(眼睛)'}),
                ('工作', {'肯定': 'matayal', '華語': '工作'}),
                ('休息(停止工作)', {'肯定': "pahanhan / masa'sa'", '華語': '休息(停止工作)'}),
                ('知道', {'肯定': "mafana'", '華語': '知道'}),
                ('忘記', {'肯定': 'mapawan / matawal', '華語': '忘記'}),
                ('長大(指人)', {'肯定': "mato'as", '華語': '長大(指人)'}),
                ('成熟(指水果)', {'肯定': 'marohem', '華語': '成熟(指水果)'}),
                ('想念', {'肯定': "ma'ilol", '華語': '想念'}),
                ('禱告；祈求', {'肯定': 'mitolon', '華語': '禱告；祈求'}),
                ('滿滿', {'肯定': 'tomes', '華語': '滿滿'})
            ])
        )

    def 物件對照(self, 結果, 答案):
        for 果, 答 in zip(結果, 答案):
            self.assertEqual(果, 答)
