from os import walk, makedirs
from os.path import join, dirname
from 臺灣言語工具.系統整合.程式腳本 import 程式腳本
import re

舊資料夾 = '原始資料'
新資料夾 = '轉換後資料'


def _轉碼(檔名, 檔案原來編碼):
    新檔名 = 檔名.replace(舊資料夾, 新資料夾)
    makedirs(dirname(新檔名), exist_ok=True)
    程式腳本._走指令([
        'iconv', '-f', 檔案原來編碼,
        '-t', 'utf8',
        '-o', 新檔名,
        檔名
    ])
    return 新檔名


def _試轉碼(檔名):
    try:
        return _轉碼(檔名,  'utf8')
    except:
        pass
    try:
        return _轉碼(檔名,  'BIG5')
    except:
        pass
    try:
        return _轉碼(檔名,  'BIG5HKSCS')
    except:
        pass
    try:
        return _轉碼(檔名,  'GB2312')
    except:
        #         print(檔名)
        #         程式腳本._走指令(['file',檔名],True)
        #         程式腳本._走指令(['enca',檔名],True)
        #         raise RuntimeError(檔名 + '無法度轉！！')
        程式腳本._走指令([
            'iconv', '-f', 'big5',
            '-t', 'utf8', '-c',  # 忽略有問題的字元
            '-o', 新檔名,
            檔名
        ])
        return 新檔名


def _提掉x02_b控制字元(檔名):
    with open(檔名, 'rb') as 檔案:
        原本資料 = 檔案.read()
    新資料 = (原本資料
           .replace(b'\x02', b'')
           .replace(b'\x0d', b'')
           )
    with open(檔名, 'wb') as 檔案:
        檔案.write(新資料)


if __name__ == '__main__':
    for 所在, 資料夾, 檔案檔名 in walk(舊資料夾):
        for 檔案 in 檔案檔名:
            if 檔案.endswith('txt'):
                檔名 = join(所在, 檔案)
                新檔名 = _試轉碼(檔名)
                _提掉x02_b控制字元(新檔名)
