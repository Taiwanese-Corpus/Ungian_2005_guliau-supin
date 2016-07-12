# 台語文語料庫蒐集及語料庫為本台語書面語音節詞頻統計

## 論文
* http://ip194097.ntcu.edu.tw/giankiu/keoe/KKH/guliau-supin/guliau-supin.asp

## 語料來源
本計畫的語料來源，主要來自以下幾個部分：[ Pún kè-ōe ê gú-liāu lâi-gôan chú-iàu ū í-hā kúi-ê p\ue029-hūn : ]
  1. 台文刊物：包括《台文通訊》(1991年創刊)、《台文罔報》(1996年創刊)、《TGB通訊》(1999年創刊)、《蓮蕉花》(1999年創刊)、《台灣字》(2000年創刊，全羅馬字)、《湠根》母語文雜誌(2002年創刊，現已停刊)、《台灣公論報》蕃薯園台文專刊(2003年創刊)、...等。[ Tâi-bûn khan-b\ue031t : pau-koah “Tâi-bûn Thong-sìn”(1991 nî chhòng-khan), “Tâi-bûn Bóng-pò” ( 1996 nî chhòng-khan ), “TGB Thong-sìn” ( 1999 nî chhòng-khan ) , “Liân-chiau-hoe” ( 1999 nî chhòng-khan ), “Tâi-ôan-jī” ( 2000 nî chhòng-khan ) , “Thòaⁿ-kun bó-gú-bûn” ch\ue001p-chì ( 2002 nî chhòng-khan, chit-má í-keng thêng-khan ), “Tâi-ôan kong-lūn-pò” Han-chû-h\ue015g Tâi-bûn choan-khan ( 2003 nî chhòng-khan ), ... téng-téng .]
  2. 專書或論文：主要由作者或編者提供。[ Choan-su iah-sī lūn-bûn :chú-iàu sī chok-chiá iah-sī pian-chiá thê-kiong .  ]11NSC 93-2213-E-122-001- 台語文語料庫蒐集及語料庫為本台語書面語音節詞頻統計
  3. 研究計畫成果：主要為國家台灣文學館籌備處委託成功大學台灣文學系執行的「台灣白話字文學資料蒐集整理計畫」中已經數位化的電子檔。計畫主持人為呂興昌教授。[ Gián-kiù kè-ōe sêng-kó : chú-iàu sī kok-ka Tâi-ôan Bûn-h\ue001k-kóan Tiû-pī-chhù úi-thok Sêng-kong Tāi-h\ue001k Tâi-ôan-bûn-h\ue001k-hē ch\ue007p-hêng ê “Tâi-ôan P\ue003h-ōe-jībûn-h\ue001k chu-liāu s\ue021-ch\ue007p chéng-lí kè-ōe” lāi-tóe í-keng s\ue025-ūi-hòa ê tiān-chú tóng-àn. Kè-ōe chú-chhî-jîn sī Lī Heng-chhiong kàu-siū.

## 解釋
* HL
  * 漢羅
  * 部份漢字，部分羅馬字
* POJ
  * 白話字
  * 全部攏是羅馬字
  
## 資料夾紹介
### 原始資料
文檔是big5編碼
* `HL`
  * 漢羅文章資料夾
* `POJ`
  * 白話字文章資料夾
* `tgbgl.mdb`
  * 資料目錄

### 轉換後資料
* `HL.csv`、`POJ.csv`
  * 用`mdbtools-gmdb`共`tgbgl.mdb`的表export轉做`csv`檔
* `HL`、`POJ`資料夾
  * 對`原始資料`的big5檔案轉做utf8編碼
```
sudo apt-get install -y python3 python-virtualenv g++ python3-dev zlib1g-dev libbz2-dev liblzma-dev tofrodos
virtualenv --python=python3 venv; . venv/bin/activate; pip install --upgrade pip; pip install tai5-uan5_gian5-gi2_kang1-ku7; python 轉換資料.py
```
  * 人工用`notepad`共有`333pigu-`的檔案另存新檔做`UTF-8`格式
  * 斷行攏轉做linux格式
    * `find 轉換後資料/ -name '*txt' -exec fromdos {} \;`
  * 全部的資料攏是純文字格式
  * `./轉換後資料/HL/散文/楊允言/Miiome-鄒族紀事.txt`本底是asp的html格式，有半人工共asp、html的標仔提掉，改做純文字格式