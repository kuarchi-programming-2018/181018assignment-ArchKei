# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 23:11:01 2018

@author: KEI
"""

class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

    def say_hello(self):
        print(self.msg + " " + self.target)

class Hello(Greeting):
    # ここにオーバライドするメソッドを記述する
    def say_hello(self, target):
        self.target = target
        print(self.msg + " " + self.target)


player = Hello()
player.say_hello("python")

player2 = Greeting()
player2.say_hello()