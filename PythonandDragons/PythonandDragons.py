"""
moduleName.py

This is where all the functions, classes, variables, etc lie in your custom module.
"""
import random
import math
#class item

class item():
  def __init__(self, worth):
    self.worth = worth

  def getworth():
    return self.worth

class weapon():
  def __init__(self, worth, name, damagedie, type):
    self.name = name
    self.damagedie = damagedie
    self.type = type
    self.worth = worth

  def getworth():
    return self.worth

  def weaname(self):
    return self.name

  def weadamagedie(self):ji
    return self.damagedie

  def weatype(self):
    return self.type



# class player
class player():
  def __init__(self, name, clas, level, race, str, dex, con, int, wis, cha, inventorylist, health, hitdie, xp, proficiencylist, gold, proficiencybonus, size, ac, speed, skills, pasper):
    #self.varible = varible stuff
    self.name = name
    self.level = level
    self.clas = clas
    self.race = race
    self.str = str
    self.dex = dex
    self.con = con
    self.int = int
    self.wis = wis
    self.cha = cha
    self.inventorylist = inventorylist
    self.health = health
    self.hitdie = hitdie
    self.xp = xp
    self.proficiencylist = proficiencylist
    self.gold = gold
    self.proficiencybonus = proficiencybonus
    self.size = size
    self.ac = ac
    self.speed = speed
    self.skills = skills
    self.magic = magic
    self.pasper = pasper
    

#defining the functions to get each varible DIRECTLY from the class
  def charname(self):
    return self.name

  def charclas(self):
    return self.clas

  def charlevel(self):
    return self.level

  def charrace(self):
    return self.race

  def charstr(self):
    return self.str

  def chardex(self):
    return self.dex

  def charcon(self):
    return self.con

  def charint(self):
    return self.int

  def charwis(self):
    return self.wis

  def charcha(self):
    return self.cha
    
  def charinventorylist(self):
    return self.inventorylist

  def charhealth(self):
    return self.health

   def charhitdie(self):
    return self.hitdie

 def charxp(self):
    return self.xp

 def charproficiencylist(self):
    return self.proficiencylist

  def chargold(self):
    return self.gold

  def charproficiencybonus(self):
    return self.proficiencybonus

  def charsize(self):
    return self.size

  def charac(self):
    return self.ac

  def charspeed(self):
    return self.speed

  def charskills(self):
    return self.skills

  def charpasper(self):
    return self.pasper
  # caluculate modifiers and shut
  def charstrb(self):
    return math.floor(((int(self.str) - 10) / 2))
  def chardexb(self):
    return math.floor(((int(self.dex) - 10) / 2))
  def charconb(self):
    return math.floor(((int(self.con) - 10) / 2))
  def charintb(self):
    return math.floor(((int(self.int) - 10) / 2))
  def charwisb(self):
    return math.floor(((int(self.wis) - 10) / 2))
  def charchab(self):
    return math.floor(((int(self.cha) - 10) / 2))

def roll(number, modifier):
  return random.randint(1, number) + modifier


def makechar(name, clas, level, race, str, dex, con, int, wis, cha, inventorylist, classlist, racelist):
  makecharcheck = False
    #check if clas in classlist
    if clas in classlist:
      #level check
      if level > 0:
        #race check
        if race in racelist:
          print("Error: This function of PythonandDragons is not working yet :9")
        else:
          makecharcheck = False
          print("race not in race list")
      else:
        makecharcheck = False
        print("Error: level less then 1")
    else:
      makecharcheck = False
      print("Clas not in Classlist")
    
