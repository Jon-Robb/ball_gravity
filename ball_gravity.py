
from abc import ABC, abstractmethod
import math
from tkinter import E, N, W, S, ttk, Tk 
import tkinter as tk
from turtle import bgcolor

#Mathématique:
    # rad * 180/PI = degrés
    # degré * PI/180 = rad 
    

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

class Updatable(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def tick(self):
        """Méthode abstraite qui sera redéfinie pour les balles
        """
        pass

class Gravitational(ABC):
    def __init__(self, masse):
        self._masse = masse
     
    @abstractmethod
    def pull(self, ball):
        pass
        

class Ball(Updatable, Gravitational):
    def __init__(self, position:Point, speed:Point, radius, color, density, acceleration:Point=None):
        Gravitational().__init__(density * (math.pi * radius ** 2))
        self.__position = position
        self.__speed = speed
        self.__acceleration = acceleration
        self.__radius = radius
        self.__color = color
        self.__density = density
             
    def move(self):
        self.__position.x += self.__speed + 0.5(self.__acceleration.x)**2
        self.__position.y += self.__speed + 0.5(self.__acceleration.y)**2
        self.speed.x += self.__acceleration.x
        self.speed.y += self.__acceleration.y

    
    def bounce(self, game_dimension:Point):
        if self.__position.x <= 0 or self.__position.x >= game_dimension.x:
            self.speed.x = -self.speed.x
        elif self.__position.y <= 0 or self.__position.y >= game_dimension.y:
            self.speed.y = -self.speed.y
            
    def pull(self, ball):
        pass 

class Game(ttk.Frame):
    def __init__(self, parent, size=Point(100, 100)):
        super().__init__(parent)
        self.size = size
        self.label = tk.Label(self, width=self.size.x, background='black', height=self.size.y)
        self.label.grid()

class Application(Tk):
    
    def __init__(self):
        super().__init__()
        
        self.title('Balls gravity')
        self.geometry("500x500")
        g = Game(self)
        
        g.grid(sticky=(N,E,W,S))
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        
def main():
    
    app = Application()
    app.mainloop()
    
if __name__ == '__main__':
    main()