import tkinter
from Frames import Frames

def main():
    root = tkinter.Tk()
    frames = Frames(root)
    frames.setup_all_frames() #sets up all frames in root
    frames.root.mainloop()

    return None

main()
