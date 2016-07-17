#!python
import csv
from os import walk
from os.path import join, dirname, abspath


這馬所在 = dirname(dirname(abspath(__file__)))


def 轉規類(來源, 類):
    欄位表 = {
        'luipiat': '類別',
        'chokchia': '作者',
        'piautoe': '標題',
        'tongmia': '檔名',
        'nitai': '年代',
        'lamlu': '男女',
    }
    目錄 = {}
    with open(join(來源, 類 + '.csv')) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            資料 = {}
            for 欄位, 內容 in row.items():
                try:
                    資料[欄位表[欄位]] = 內容
                except:
                    pass
            資料['男女'] = {'b': '查某', 'p': '查甫', 'm': '毋知'}[資料['男女']]
            檔名 = 資料.pop('檔名')
            目錄[檔名] = 資料

    資料來源 = {'名': '台語文語料庫蒐集及語料庫為本台語書面語音節詞頻統計'}
    全部資料 = []
    for 所在, _資料夾, 檔名陣列 in walk(join(來源, 類)):
        for 檔名 in 檔名陣列:
            with open(join(所在, 檔名)) as 檔:
                try:
                    來源內容 = 目錄.pop(檔名[:-4])
                    來源內容.update(資料來源)
                except:
                    來源內容 = 資料來源
                    print(類, '無檔案資料', 檔名)
                for 一逝 in 檔.readlines():
                    資料 = {
                        來源: 來源內容,
                        '文本資料': 一逝.strip(),
                    }
                    全部資料.append(資料)
    print('目錄賰：', 目錄.keys())
    return 全部資料

if __name__ == '__main__':
    轉規類(join(這馬所在, '轉換後資料'), 'HL')
    轉規類(join(這馬所在, '轉換後資料'), 'POJ')
