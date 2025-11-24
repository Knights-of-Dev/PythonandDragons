"""
moduleName.py

This is where all the functions, classes, variables, etc lie in your custom module.
"""
import random

class player():
  def __init__(self, name, clas, level, race, str, dex, con, int, wis, cha, inventorylist, health, hitdie, xp, proficiencylist, gold, proficiencybonus, size, ac, speed, skills, magic, pasper):
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


  def charlevel(self):
    return self.level

  def charclas(self):
    return self.clas


def roll(number):
  return random.randint(1, number)


def makechar(name, clas, level, race, str, dex, con, int, wis, cha, inventorylist, classlist, racelist):
  print("Error: This function of PythonandDragons is not working yet :9")
    
