from pynput.keyboard import Key, Controller
keyboard = Controller()
import time
while True:
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)
    keyboard.press("a")
    keyboard.release("a")

#time kütüphanesini asla unutmayın yada sonsuz döngü içerisnde kullanmayın aksi taktirde 0 saniyede sonsuz işlem 
#yapmaya çalışıp bilgisayara zarar verir
