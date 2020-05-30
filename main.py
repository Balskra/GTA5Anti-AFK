import pyautogui
import time


DELAY_BETWEEN_COMMANDS=1.00


def main():
    InitializePyAutoGUI()
    countdowntimer()
    i=1
    while i<500:
        i+=1
        print(i)
        holdKey('w', 2.00)
        holdKey('s', 2.00)
        holdKey('a', 2.00)
        holdKey('d', 2.00)
        holdKey('d', 2.00)
        holdKey('a', 2.00)

    print("Сделано")

def countdowntimer():
    print("Загрузка", end="")
    for i in range(0, 10):
        print(".", end="")
        time.sleep(1)
    print("Поехали")

def InitializePyAutoGUI():
    pyautogui.FAILSAFE = True


def holdKey(key, seconds=1.00):
        pyautogui.keyDown(key)
        time.sleep(seconds)
        pyautogui.keyUp(key)
        time.sleep(DELAY_BETWEEN_COMMANDS)


if __name__ == "__main__":
    main()

