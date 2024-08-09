import tkinter as tk
import os
import time
import random
import sys

class corvid():

    def __init__(self):
        self.window = tk.Tk()
        self.gif_size = '196x196'

        # placeholder image
        # Asset provided at: https://www.deviantart.com/ravencorona/art/Pixel-Art-Birb-Icon-908712952
        self.flapping_wings = [tk.PhotoImage(file=os.path.join(os.getcwd(), 'Assets', 'corvid.gif'), format='gif -index %i' % (i)) for i in range(9)]
        self.frame_index = 0
        self.img = self.flapping_wings[self.frame_index]

        # timestamp to check whether to advance frame
        # timer to not let it run that long
        self.timer = self.timestamp = time.time()

        # set focushighlight to black when the window does not have focus
        self.window.config(highlightbackground='white')

        # make window frameless
        self.window.overrideredirect(True)

        # make window draw over all others
        self.window.attributes('-topmost', True)

        # turn black into transparency
        self.window.wm_attributes('-transparentcolor', 'white')

        # create a label as a container for our image
        self.label = tk.Label(self.window, bd=0, bg='white')

        # create a window of size 128x128 pixels, at coordinates 0,0
        self.x = 0
        self.y = 0
        self.window.geometry('{size}+{x}+{y}'.format(size=self.gif_size, x=str(self.x), y=str(self.y)))

        # add the image to our label
        self.label.configure(image=self.img)

        # give window to geometry manager (so it will appear)
        self.label.pack()

        # run self.update() after 0ms when mainloop starts
        self.window.after(0, self.update)
        self.window.mainloop()
        
    def update(self):
        # move right by one pixel
        self.x += 1
        self.y += 1
        # self.timer += 1

        # advance frame if 50ms have passed
        if time.time() > self.timestamp + 0.2:
            self.timestamp = time.time()
            # advance the frame by one, wrap back to 0 at the end
            self.frame_index = (self.frame_index + 1) % 4
            self.img = self.flapping_wings[self.frame_index]
        
        if time.time() > self.timer + 10:
            sys.exit()

        # create the window
        self.window.geometry('{size}+{x}+{y}'.format(size=self.gif_size, x=str(self.x), y=str(self.y)))
        # add the image to our label
        self.label.configure(image=self.img)
        # give window to geometry manager (so it will appear)
        self.label.pack()

        # call update after 10ms
        self.window.after(10, self.update)
        
corvid()