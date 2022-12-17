# Lost-ArkAuto-Finshing

## 說明

使用Python pyautogui套件，來解析畫面實現自動拋收桿

## 套件

使用前要先安裝python與相關套件

- Pthon版本
  -  3.10

- 套件安裝指令
  - pip install pyperclip
  - pip install pyautogui==0.9.50
  - pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple
  - pip install pillow

## 使用方式

1. 安裝好環境後，確定01~04的png檔、AutoFinshing.py與Autofishing.bat
2. 雙擊Autofishing.bat
3. 輸入釣魚所使用的技能案件(qwerasdf--其中之一)
4. 程式會開始到數，之後開始釣魚
5. 在倒數過程中，要回到遊戲中，再把鼠標放在可釣魚區域(海面上)
6. 如果一切程式正常，會自動停止

## 備註

1. 第一次執行時，會先判斷是否切到生活技能，如果沒有會自動切換，但有時候會誤判，導致切到戰鬥技能
   1. 只要手動切換到生活技能就可以解決，之後就繼續掛機

2. 程式在設計時有設想自動關閉，但有時候會配對不到，直接釣到釣竿壞掉
3. 電腦的CPU好壞，會直接影響運算效率，進而導致收桿時間過晚，以致收桿失敗
   1. 這個目前沒有解