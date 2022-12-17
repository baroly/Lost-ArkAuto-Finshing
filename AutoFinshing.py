import pyautogui
import time
import pyperclip
import pathlib
import os

#判斷 '附近沒有可以捕獲的魚' 時間1,信任度0.6


if __name__ == '__main__':
    path = str(os.getcwd()) + '\\'
    picD = ['01.png','02.png','03.png','04.png']
    judgeErr = False
    
    skillkey = input('輸入釣魚技能按鍵:').lower()
    print()

    for i in range(5, 0, -1):
        print('開始釣魚倒數 ' + str(i))
        time.sleep(1)

    if pyautogui.locateCenterOnScreen(path + '01.png') is None:
        pyautogui.press('b')

    print()
    while True:

        errortime = 0
        i = 0

        #img = path+picD[i]
        # location = None
        # location = pyautogui.locateCenterOnScreen(img,confidence=0.8)
        # time.sleep(0.5)
        # print(location)
        # #location=pyautogui.locateCenterOnScreen(img,confidence=0.8)
        # #location=pyautogui.locateCenterOnScreen(img,confidence=0.9)
        # if location is None:
        #     pyautogui.press('b')
        #     print('\texchange skill to life')

        time.sleep(1)

        i = i + 1
        img = path + picD[i]
        
        print('\t開始釣魚')
        pyautogui.press(skillkey)
        time.sleep(0.5)

        #judge area is correct or not
        while pyautogui.locateCenterOnScreen(img,confidence=0.6) is not None:
            if errortime > 2:
                break
            errortime = errortime + 1
            print('\tmouse isn\'t on the correct loaction. Retry ' + str(errortime))
            time.sleep(2)
            pyautogui.press(skillkey)
            time.sleep(0.5)
        #if error time large than 3, then break 
        if errortime > 2:
            break

        i = i + 1
        img = path + picD[i]
        fishingtime = 0
        print('\t釣魚中...')
        #=====================================
        #while裡面的confidence可以調整信任度	越接近 1.0 要求相似度越高
        while pyautogui.locateCenterOnScreen(img,confidence=0.6) is None:
            time.sleep(0.01)
            fishingtime = fishingtime + 1

            if fishingtime > 1000:
                break

        if fishingtime > 1000:
            print('\t釣魚失敗!\n')
            continue
        
        #print(str(pyautogui.locateCenterOnScreen(img,confidence=0.5)))
        pyautogui.press(skillkey)
        print('\t釣魚成功 獲取漁獲...\n')

        #=====================================
        #這邊是要控制觀察到裝備損壞後自動停止	如不需要此區間可以註解
        i = i + 1
        img = path + picD[i]
        if pyautogui.locateCenterOnScreen(img,confidence=0.7) is not None:
            print('釣魚已結束 請維修工具')
            break
        #=====================================

        time.sleep(5)
        
    os.system('pause any key to end')