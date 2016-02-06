from os import walk, makedirs
from os.path import join, dirname, basename
from 臺灣言語工具.系統整合.程式腳本 import 程式腳本
from shutil import copy2

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
        新檔名 = join(
            dirname(檔名).replace(舊資料夾, 新資料夾),
            '333pigu-' + basename(檔名)
        )
        copy2(檔名, 新檔名)
        return 新檔名


if __name__ == '__main__':
    for 所在, 資料夾, 檔案檔名 in walk(舊資料夾):
        for 檔案 in 檔案檔名:
            if 檔案.endswith('txt'):
                檔名 = join(所在, 檔案)
                _試轉碼(檔名)
