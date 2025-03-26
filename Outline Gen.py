import pyautogui
import time
import argparse
k = 0
parser = argparse.ArgumentParser("Outline generator")
parser.add_argument("--slow",help="To have the algorithm run slow use 's'",default="f")
parser.add_argument("--mode", help="The mode of the script 'd' = default, 'h'= 2d house(start of line = roof corner, end of line = ground corner)",default="d")


def run_command(speed,delay,command):
    time.sleep(delay)
    pyautogui.press("t")
    time.sleep(delay)
    pyautogui.write(command,speed)
    pyautogui.press("enter")

def house_outline(Points,speed,delay):
    run_command(speed,delay,"//sel cuboid")
    for i in range(0,len(Points) - 1):
        run_command(speed,delay,"/tpll " + Points[i])
        run_command(speed,delay,"//pos1")
        run_command(speed,delay,"//pos2")
        run_command(speed,delay,"//set 57")
    run_command(speed,delay,"//sel poly")
    run_command(speed,delay,"/tpll " + Points[0])
    time.sleep(delay)
    pyautogui.keyDown("shift")
    time.sleep(0.02)
    pyautogui.keyUp("shift")
    time.sleep(delay)
    run_command(speed,delay,"//pos1")
    for i in range(1,len(Points) - 1):
        run_command(speed,delay,"/tpll " + Points[i])
        time.sleep(0.7)
        pyautogui.keyDown("shift")
        time.sleep(0.02)
        pyautogui.keyUp("shift")
        time.sleep(0.7)
        run_command(speed,delay,"//pos2")
    run_command(speed,delay,"//cut -m 57")
    run_command(speed,delay,"/tpll " +Points[len(Points) - 1])
    run_command(speed,delay,"//paste -m 57")
    


def outline(Points,speed,delay):
    time.sleep(delay)
    pyautogui.press("t")
    time.sleep(delay)
    pyautogui.write("/tpll " + Points[0],speed)
    pyautogui.press("enter")
    time.sleep(delay)
    for i in range(0,len(Points) - 1 ):
        time.sleep(delay)
        pyautogui.press("t")
        time.sleep(delay)
        pyautogui.write("//pos1",speed)
        pyautogui.press("enter")
        time.sleep(delay)
        pyautogui.press("t")
        time.sleep(delay)
        pyautogui.write("/tpll " + Points[i + 1],speed)
        pyautogui.press("enter")
        time.sleep(delay)
        pyautogui.press("t")
        time.sleep(delay)
        pyautogui.write("//pos2 ",speed)
        pyautogui.press("enter")
        time.sleep(delay)

        pyautogui.press("t")
        time.sleep(delay)
        pyautogui.write("//line 57",speed)
        pyautogui.press("enter")
        time.sleep(delay)
    pyautogui.press("t")
    time.sleep(delay)

args = parser.parse_args()
time.sleep(5)
speed = 0.01
delay = 0.5
if args.slow == "s":
    speed = 0.05
    delay = 2
pyautogui.press("t")
time.sleep(delay)
pyautogui.write("/gamemode spectator",speed)
pyautogui.press("enter")
time.sleep(delay)
pyautogui.press("t")
time.sleep(delay)
pyautogui.write("//sel cuboid",speed)
pyautogui.press("enter")
try:
    while True:



        k = k + 1
        file = open("path"+ str(k) + ".kml","r")
        Points = []
        IsCorrectLine = False
        for i in file.readlines():
            if IsCorrectLine:
                currentcoord = ""
                i = i.strip()
                i = i + " "
                for j in i :
                    if j == " " :
                        currentcoord = currentcoord + j
                        currentcoord = currentcoord.replace(",0 ","")
                        temp = currentcoord.split(",")
                        temp.reverse()
                        currentcoord = temp[0] + ", " + temp[1]
                        Points.append(currentcoord)
                        currentcoord = ""
                    else    :
                        currentcoord = currentcoord + j
                    if j == "<" :
                        break
                IsCorrectLine = False


            if i.find("<coordinates>") != -1 :
                IsCorrectLine = True
            
        file.close()
        if args.mode == "h":
            house_outline(Points,speed,delay)
        else:
            outline(Points,speed,delay)
        isroad = True
                 
except:
    run_command(speed,delay,"/gamemode creative")
    print("Done")

