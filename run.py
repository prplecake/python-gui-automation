from PIL import Image
import pyautogui as ag

size = ag.size()

ag.moveTo(599, 357, 0)
ag.click()
ag.moveTo(1024, 44, 0)
ag.click()
ag.moveTo(410, 92, 0)
ag.click()

ag.press('backspace')
ag.typewrite('jrgnsn.net', interval=0)
ag.press('enter')
