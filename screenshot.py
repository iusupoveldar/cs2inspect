import time
import pyautogui
import pydirectinput
 
# cvar_unhide_all
# sv_cheats 1
# @panorama_disable_draw_text 1
 
#         "Bayonet",
#         "Bowie_Knife",
#         "Butterfly_Knife",
#         "Classic_Knife",
#         "Falchion_Knife",
#         "Flip_Knife",
#         "Gut_Knife",
#         "Huntsman_Knife",
#         "Karambit",
#         "M9_Bayonet",
#         "Navaja_Knife",
#         "Nomad_Knife",
#         "Paracord_Knife",
#         "Shadow_Daggers",
#         "Skeleton_Knife",
#         "Stiletto_Knife",
#         "Survival_Knife",
#         "Talon_Knife",
#         "Ursus_Knife",
 
if __name__ == "__main__":
    files = [
        "Butterfly_Knife"
    ]
    time.sleep(5)
    width = 1920
    height = 1080 

    for file in files:
        pattern = 0
        with open(f"./inspect/{file}_commands.txt") as f:
            for line in f:
                pydirectinput.press('`')
                time.sleep(.5)
                pyautogui.write(line)
                time.sleep(1)
                pydirectinput.press('enter')
                time.sleep(.5)
                pydirectinput.press('`')
                time.sleep(3)
                # click on maps
                pyautogui.moveTo(750, 1025)
                time.sleep(.2)
                pyautogui.click()
                print("Clicked Overppas")
                # click on overpass
                time.sleep(.2)
                pyautogui.moveTo(850, 990)
                time.sleep(.2)
                pyautogui.click()
                time.sleep(.2)
                # click on Nuke
                pyautogui.moveTo(750, 1025)
                time.sleep(.2)
                pyautogui.click()
                print("Clicked nuke")
                time.sleep(.2)
                pyautogui.moveTo(850, 870)
                time.sleep(.2)
                pyautogui.click()
 
 
                for i in range(4):
                    pyautogui.moveTo(100, 750)
                    pyautogui.dragTo(1000, 750, .5, button='left')
                time.sleep(2)
                myScreenshot = pyautogui.screenshot()
                myScreenshot.save(f'./cs2_screen/{file}/{pattern}_first.png')
                # time.sleep(1)
                # pyautogui.moveTo(1600, 750)
                # time.sleep(.2)
                # pyautogui.dragTo(390, 750, .5, button='left')
                # time.sleep(2)
                # myScreenshot = pyautogui.screenshot()
                # myScreenshot.save(f'./cs2_screen/{file}/{pattern}_second.png')
                # time.sleep(1)
 
                if pattern % 25 == 0:
                    print(pattern)
                pattern += 1