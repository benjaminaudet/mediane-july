import PIL.Image
from PIL import ImageTk
from tkinter import *
import time
import random
import _thread


class ExampleApp(Frame):
    def __init__(self, master):
        Frame.__init__(self, master=None)
        self.x = self.y = 0
        self.canvas = Canvas(master, height=1000, width=1000)

        self.canvas.grid(row=0, column=0, sticky=N+S+E+W)

        self.rect = None

        self.start_x = None
        self.start_y = None

        self.wazil, self.lard = 1000, 1000
        self.canvas.config(scrollregion=(0, 0, self.wazil, self.lard))


class Snake():
    def __init__(self, master, x, y, id) -> None:
        global app
        self.x = x
        self.y = y
        self.dir = 0
        self.len = 3
        self.alive = True
        self.app = app
        self.master = master
        if id == 1:
            self.master.bind("z", self.on_up)
            self.master.bind("q", self.on_left)
            self.master.bind("s", self.on_down)
            self.master.bind("d", self.on_right)
            self.master.bind("<Escape>", self.escape)
        elif id == 2:
            self.master.bind("<Up>", self.on_up)
            self.master.bind("<Left>", self.on_left)
            self.master.bind("<Down>", self.on_down)
            self.master.bind("<Right>", self.on_right)
            self.master.bind("<Escape>", self.escape)
        self.moved = True
        self.prev_rect = None

    def tick(self):
        self.app.canvas.delete(self.prev_rect)
        if self.dir == 0:
            self.y += 1
        elif self.dir == 1:
            self.x += 1
        elif self.dir == 2:
            self.y -= 1
        elif self.dir == 3:
            self.x -= 1
        self.prev_rect = self.app.canvas.create_rectangle(
            self.x, self.y, self.x + 20, self.y + 20, fill="red", outline="", tags="snake-" + str(id))
        self.app.canvas.delete("this")
        self.app.canvas.after(10, self.tick)
        self.moved = True

    def on_up(self, event):
        if self.moved and not self.dir == "2":
            self.dir = 2

    def on_down(self, event):
        if self.moved and not self.dir == "0":
            self.dir = 0

    def on_left(self, event):
        if self.moved and not self.dir == "3":
            self.dir = 3

    def on_right(self, event):
        if self.moved and not self.dir == "1":
            self.dir = 1

    def escape(self, event):
        self.master.destroy()
        exit()


if __name__ == "__main__":
    root = Tk()
    app = ExampleApp(root)
    snake1 = Snake(root, 0, 0, 1)
    snake2 = Snake(root, 50, 50, 2)
    snake1.tick()
    snake2.tick()
    # _thread.start_new_thread(snake1.tick)
    # _thread.start_new_thread(snake2.tick)
    root.mainloop()
