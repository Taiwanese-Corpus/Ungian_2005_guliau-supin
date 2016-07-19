#!python
import csv
from os import walk
from os.path import join, dirname, abspath, basename
from itertools import chain

import yaml

這馬所在 = dirname(dirname(abspath(__file__)))


def 轉規類(語料資料夾, 類):
    欄位表 = {
        'luipiat': '類別',
        'chokchia': '作者',
        'piautoe': '標題',
        'tongmia': '檔名',
        'nitai': '年代',
        'lamlu': '男女',
    }
    目錄 = {}
    with open(join(語料資料夾, 類 + '.csv')) as csvfile:
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
    for 所在, _資料夾, 檔名陣列 in walk(join(語料資料夾, 類)):
        for 檔名 in 檔名陣列:
            with open(join(所在, 檔名)) as 檔:
                try:
                    來源內容 = 目錄.pop(檔名[:-4])
                    來源內容.update(資料來源)
                except:
                    來源內容 = 資料來源
                    作者 = basename(所在)
                    類別 = basename(dirname(所在))
                    來源內容 = {'作者': 作者, '類別': 類別}
                    print(類,  檔名, 來源內容)
                    來源內容.update(資料來源)
                for 一逝 in 檔.readlines():
                    文本資料 = 一逝.strip()
                    if len(文本資料) > 0:
                        資料 = {
                            '來源': 來源內容,
                            '文本資料': 文本資料,
                        }
                        全部資料.append(資料)
    if len(目錄) > 0:
        print('目錄賰：', 目錄.keys())
        raise RuntimeError('表有物件無對著！！')
    return 全部資料

if __name__ == '__main__':
    資料 = {
        '版權': '會使公開',
        '種類': '語句',
        '語言腔口': '閩南語',
        '著作年': '2005',
        '著作所在地': '臺灣',
    }
    HL = 轉規類(join(這馬所在, '轉換後資料'), 'HL')
    POJ = 轉規類(join(這馬所在, '轉換後資料'), 'POJ')
    資料['下層'] = HL + POJ
    with open('台語文語料庫蒐集及語料庫為本台語書面語音節詞頻統計.yaml', 'w') as 檔案:
        yaml.dump(資料, 檔案, default_flow_style=False, allow_unicode=True)
