#pip install pyautogui
import pyautogui
import keyboard

# تابعی برای تایپ کردن عبارت "عرفان" 10 بار
def type_erfan_10_times():
    for _ in range(100):
        pyautogui.typewrite("@eerfan")
        pyautogui.press('enter')  # اضافه کردن Enter برای تفکیک هر تایپ
        pyautogui.press('enter')

# تعیین کلید فعال‌ساز
activate_key = 'space'  # می‌توانید کلید دیگری انتخاب کنید

# منتظر فشردن کلید فعال‌ساز توسط کاربر شوید
keyboard.wait(activate_key)

# فراخوانی تابع برای تایپ کردن "عرفان" 10 بار
type_erfan_10_times()
