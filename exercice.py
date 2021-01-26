#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
pi = math.pi
def square_root(a: float) -> float:
    return math.sqrt(a)
    # return a**(1/2) si on souhaite sous forme de puissance


def square(a: float) -> float:
    return a**2


def average(a: float, b: float, c: float) -> float:
    s = a+b+c
    aver = s/3
    return aver


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    #correction prof
    deg = angle_degs+(angle_mins/60)+(angle_secs/3600)
    rad = math.radians(deg)
    return rad


def to_degrees(angle_rads: float) -> tuple:
    #correction prof
    deg = math.degrees(angle_rads) #90.706 degree
    min = (deg-math.floor(deg))*60 #42.36 minute d'arc
    sec = (min-math.floor(min))*60
    return math.floor(deg), math.floor(min), sec


def to_celsius(temperature: float) -> float:
    varFarenheit = (temperature-32)/1.8
    return varFarenheit


def to_farenheit(temperature: float) -> float:
    varCelsius = temperature*1.8+32
    return varCelsius


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 180 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
