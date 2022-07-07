import PIL.Image
from PIL import ImageTk
from tkinter import *
import time
import random
import _thread
import math

SIZE = 20


class ExampleApp(Frame):
    def __init__(self, master):
        global SIZE
        Frame.__init__(self, master=None)
        self.x = self.y = 0
        self.canvas = Canvas(master, height=500, width=500)
        self.food = tuple()
        self.food_spawned = False
        self.prev_food = []
        self.canvas.grid(row=0, column=0, sticky=N+S+E+W)

        self.rect = None

        self.start_x = None
        self.start_y = None

        self.wazil, self.lard = 500, 500
        self.canvas.config(scrollregion=(0, 0, self.wazil, self.lard))

    def spawn_food(self):
        global SIZE
        self.food = (int(math.floor((random.random() * 20))) * SIZE,
                     int(math.floor((random.random() * 20))) * SIZE)
        for prev_food in self.prev_food:
            self.canvas.delete(prev_food)
        self.prev_food.insert(0, self.canvas.create_rectangle(
            self.food[0], self.food[1], self.food[0] + SIZE, self.food[1] + SIZE, fill="blue", outline=""))
        self.food_spawned = True


class Snake():
    def __init__(self, master, x, y, id) -> None:
        global app
        self.x = x
        self.y = y
        self.dir = 0
        self.len = 1
        self.alive = True
        self.app = app
        self.master = master
        self.log_positions = []

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
        self.prev_rect = []

    def is_touching_food(self):
        global SIZE
        if self.x == self.app.food[0] and self.y == self.app.food[1]:
            return True
        return False

    def increment(self, coords, dir):
        global SIZE
        x = coords[0]
        y = coords[1]
        if dir == 0:
            y = coords[1] + SIZE
        elif dir == 1:
            x = coords[0] + SIZE
        elif dir == 2:
            y = coords[1] - SIZE
        elif dir == 3:
            x = coords[0] - SIZE
        return x, y

    def tick(self):
        global SIZE
        if not self.app.food_spawned:
            print('1')
            self.app.spawn_food()
        if self.is_touching_food():
            print('2')
            self.app.spawn_food()
            self.app.spawn_food()
            self.len += 1
        for prev_rect in self.prev_rect:
            self.app.canvas.delete(prev_rect)
        self.x, self.y = self.increment((self.x, self.y), self.dir)
        self.prev_rect.insert(0, self.app.canvas.create_rectangle(
            self.x, self.y, self.x + SIZE, self.y + SIZE, fill="red", outline=""))
        print(self.log_positions)
        for i in range(0, self.len):
            if self.len > 1 and self.log_positions[i]:
                self.prev_rect.insert(0, self.app.canvas.create_rectangle(
                    self.log_positions[i][0], self.log_positions[i][1], self.log_positions[i][0] + SIZE, self.log_positions[i][1] + SIZE, fill="red", outline=""))
        if self.alive == True:
            self.app.canvas.after(200, self.tick)
        self.moved = True
        self.log_positions.insert(0, (self.x, self.y))
        self.log_positions = self.log_positions[0:self.len + 1]

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
    snake2 = Snake(root, 0, 0, 2)
    snake1.tick()
    snake2.tick()
    root.mainloop()
