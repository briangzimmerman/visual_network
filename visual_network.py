from Tkinter import *
from sniffer import Sniffer
import threading

class VisualNetwork:
    BACKGROUND_COLOR = '#002B36'
    TITLE = 'Network Traffic'

    def __init__(self, master=None):
        self.master = master
        master.title = self.TITLE
        master.wm_title(self.TITLE)
        width = master.winfo_screenwidth()
        height = master.winfo_screenheight()

        self.canvas = Canvas(
            width=master.winfo_screenwidth(),
            height=master.winfo_screenheight(),
            bg=self.BACKGROUND_COLOR,
            highlightthickness=0
        )
        self.canvas.pack(expand=YES, fill=BOTH)
        self.canvas.create_line(
            width - (width/10),
            0,
            width - (width/10),
            height,
            width = 10,
            fill = '#839496'
        )
        self.sniffer = Sniffer(self.canvas, width, height)
        thread = threading.Thread(target=self.sniffer.sniff)
        thread.start()

root = Tk()
gui = VisualNetwork(root)
root.mainloop()
gui.sniffer.run = False
