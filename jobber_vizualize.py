import math
import time
import numpy

from Tkinter import *

class RushHourVisualization:
    def __init__(self, board, delay = 1, moves = 0):
        self.delay = delay
        self.moves = moves
        self.board = board
        self.board.arraynp = numpy.transpose(self.board.arraynp)

        self.width = self.board.width
        self.height = self.board.height
        self.max_dim = max(self.width, self.height)

        # Initialize a drawing surface
        self.master = Tk()
        self.w = Canvas(self.master, width = 500, height = 500)
        self.w.pack()
        self.master.update()

        # Draw a backing and lines
        x1, y1 = self._map_coords(0, 0)
        x2, y2 = self._map_coords(self.width, self.height)
        self.w.create_rectangle(x1, y1, x2, y2, fill = "grey")

        # draw gridlines
        for i in range(self.width+1):
            x1, y1 = self._map_coords(i,0)
            x2, y2 = self._map_coords(i,self.height)
            self.w.create_line(x1, y1, x2, y2)
        for i in range(self.height):
            x1, y1 = self._map_coords(0, i)
            x2, y2 = self._map_coords(self.width, i)
            self.w.create_line(x1, y1, x2, y2)

        self.cars = None
        self.text = self.w.create_text(25, 0, anchor = NW, text = self._status_string())
        self.time = 0
        self.master.update()

    def _status_string(self):
        "Returns an appropriate status string to print."
        self.moves = self.moves + 1
        return "moves: ", self.moves

    def _map_coords(self, x, y):
        "Maps grid positions to window positions (in pixels)."
        return (250 + 450 * ((x - self.width / 2.0) / self.max_dim),
                250 + 450 * ((self.height / 2.0 - y) / self.max_dim))

    def _draw_cars(self, car, color = "blue"):
        if car.id == 1:
            color = "red"
        elif car.orientation == 1:
            color = "green"
        else:
            color = "blue"
        x = car.position[0] - 1
        y = self.height - car.position[1] + 1
        x1, y1 = self._map_coords(x, y)
        if car.orientation == 1:
            x2, y2 = self._map_coords(x+1, y-2)
            if car.length == 3:
                x2, y2 = self._map_coords(x+1, y-3)
            return self.w.create_rectangle(x1, y1, x2, y2, fill = color)
        elif car.orientation == 2:
            x2, y2 = self._map_coords(x+2, y-1)
            if car.length == 3:
                x2, y2 = self._map_coords(x+3, y-1)
            return self.w.create_rectangle(x1, y1, x2, y2, fill = color)

    def update(self, board):
        # remove cars
        if self.cars:
            for car in self.cars:
                self.w.delete(car)
                self.master.update_idletasks()
        # draw cars
        self.cars = []
        for car in self.board.cars:
            self.cars.append(self._draw_cars(car))

        # update text
        self.w.delete(self.text)
        self.time += 1
        self.text = self.w.create_text(25, 0, anchor = NW, text = self._status_string())
        self.master.update()
        time.sleep(self.delay)

    def done(self):
        mainloop()
