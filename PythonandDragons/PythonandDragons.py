"""
moduleName.py

This is where all the functions, classes, variables, etc lie in your custom module.
"""
import random

#class item

class item():
  def __init__(self, worth):
    self.worth = worth

  def getworth():
    return self.worth

#class clas():
  #def __init__(self, )

class weapon():
  def __init__(self, name, damagedie, type):
    self.name = name
    self.damagedie = damagedie
    self.type = type

  def weaname(self):
    return self.name

  def weadamagedie(self):
    return self.damagedie

  def weatype(self):
    return self.type





# class player
class player():
  def __init__(self, name, clas, level, race, str, dex, con, int, wis, cha, inventorylist, health, hitdie, xp, proficiencylist, gold, proficiencybonus, size, ac, speed, skills, pasper):
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


def roll(number, modifier):
  return random.randint(1, number) + modifier


def makechar(name, clas, level, race, str, dex, con, int, wis, cha, inventorylist, classlist, racelist):
  print("Error: This function of PythonandDragons is not working yet :9")
    
