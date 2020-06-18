#pyqueen v1.0 - 03/01/2020
#Copyright (C) 2020 Thomas Pochart
#This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#You should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.

from microbit import *
from machine import *
from math import *
from neopixel import NeoPixel

addr=0x10

def motorL(n):
	if n>100:
		n=100
	if n<-100:
		n=-100
	if n>=0:
		direc=0x0
	else:
		direc=0x1
	v=abs(floor(n))*255//100
	i2c.write(addr,bytearray([0x0,direc,v]))

def motorR(n):
	if n>100:
		n=100
	if n<-100:
		n=-100
	if n>=0:
		direc=0x0
	else:
		direc=0x1
	v=abs(floor(n))*255//100
	i2c.write(addr,bytearray([0x2,direc,v]))
	
def motors(n):
	if n==0:
		f=0
	elif n>0:
		f=floor(4*n/5)+1
	else:
		f=-floor(-4*n/5)-1
	motorL(f)
	motorR(n)
	
def distance():
	if pin1.read_digital()==1:
		pin1.write_digital(0)
		sleep(10)
	pin1.write_digital(1)
	pin1.write_digital(0)	
	pin2.read_digital()	
	T=time_pulse_us(pin2, 1, 10000)
	if T<0:
		return(1000000)
	else:
		d=340*T/20000
		return(d)
	
def ledL_on():
	pin8.write_digital(0x01)
	
def ledL_off():
	pin8.write_digital(0x00)
	
def ledR_on():
	pin12.write_digital(0x01)

def ledR_off():
	pin12.write_digital(0x00)
	
def leds_on():
	ledL_on()
	ledR_on()

def leds_off():
	ledL_off()
	ledR_off()
	
def ledrgb(n,r,g,b):
    n=min(max(n,0),3)
    r=min(max(r,0),255)
    g=min(max(g,0),255)
    b=min(max(b,0),255)
    np=NeoPixel(pin15,4)
    np[floor(n)]=(floor(r),floor(g),floor(b))
    np.show()

def lineL():
    if pin13.read_digital()==1:
        return True
    else:
        return False

def lineR():
	if pin14.read_digital()==1:
		return True
	else:
		return False