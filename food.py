from turtle import Turtle
import random
from random import Random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(0.5,0.5)
        self.color("chartreuse2")
        self.speed(0)
        self.goto(random.randint(-280,280),random.randint(-280,280))
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))