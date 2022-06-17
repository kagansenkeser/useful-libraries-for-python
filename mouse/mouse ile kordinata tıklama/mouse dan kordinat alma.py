from pynput import*

def kordinatal(x,y):
    print("konum {}".format((x,y)))

with mouse.Listener(on_move = kordinatal) as listen:
    listen.join()
    
