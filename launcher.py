'''
Created on 16 Jan 2017

@author: admin
'''

from tkinter import *
from tkinter import ttk
from character import *

import random

class WorldMap:
    def __init__(self, frame):
        self.frame = frame
        self.DrawMap()
    
    def DrawMap(self):
        canvas = Canvas(self.frame) 
        canvas.pack()
        
        canvas.create_rectangle(50,25,100,100)
        
class Dice:
    def __init__(self, frame):
        self.frame = frame
        self.BuildDice()
    
    def BuildDice(self):
        Button(self.frame, text='D20', command=self.rollD20).grid(row=0, column=0)
        Button(self.frame, text='D10', command=self.rollD10).grid(row=1, column=0)
        Button(self.frame, text='D8', command=self.rollD8).grid(row=2,column=0)
        Button(self.frame, text='D6', command=self.rollD6).grid(row=3, column=0)
        Button(self.frame, text='D4', command=self.rollD4).grid(row=4, column=0)
        Button(self.frame, text='Percentage', command=self.rollPercentage).grid(row=5, column=0)
        self.result = Entry(self.frame)
        self.result.grid(row=6,column=0)
        
    def rollD20(self):
        self.result.delete(0, END)
        self.result.insert(0, str(random.randint(1,20)))
    
    def rollD10(self):
        self.result.delete(0, END)
        self.result.insert(0, str(random.randint(1,10)))
        
    def rollD8(self):
        self.result.delete(0, END)
        self.result.insert(0, random.randint(1,8))
    
    def rollD6(self):
        self.result.delete(0, END)
        self.result.insert(0, random.randint(1,6))
        
    def rollD4(self):
        self.result.delete(0, END)
        self.result.insert(0, random.randint(1,4))    
    
    def rollPercentage(self):
        self.result.delete(0, END)
        self.result.insert(0, random.randint(1,100))

class launcher:
    def __init__(self, master):
        self.master = master
        self.master.attributes('-fullscreen',True)
        
        characterSheet = {'characterId':123, 'characterName': 'dave', 'class': '', 'level': 0, 'background': '', 'playerName': '', 'faction': '', 'race': 'race', 'alignment': '', 'experiencePoints': '', 'dciNumber': '', 'vitals': {'strength': 0, 'dexterity': 0, 'constitution': 0, 'intelligence': 0, 'wisdom': 0, 'charisma': 0}, 'passiveWisdom': 0, 'otherProficiencies': 'jasodijasio\nauishduihasuhaiuhsdiuhas\n', 'armourClass': 0, 'initiative': 0, 'speed': 0, 'hitPoints': {'hitpointMax': 0, 'currentHitPoints': 0, 'temporaryHitPoints': 0}, 'savingThrows': {'strength': 0, 'dexterity': 0, 'constitution': 0, 'intelligence': 0, 'wisdom': 0, 'charisma': 0}, 'skills': {'acrobatics': {'value': 0, 'enabled': False}, 'animalHandling': {'value': 0, 'enabled': False}, 'arcana': {'value': 0, 'enabled': False}, 'athletics': {'value': 0, 'enabled': False}, 'deception': {'value': 0, 'enabled': False}, 'history': {'value': 0, 'enabled': False}, 'insight': {'value': 0, 'enabled': False}, 'intimidation': {'value': 0, 'enabled': False}, 'investigation': {'value': 0, 'enabled': False}, 'medicine': {'value': 0, 'enabled': False}, 'nature': {'value': 0, 'enabled': False}, 'perception': {'value': 0, 'enabled': False}, 'performance': {'value': 0, 'enabled': False}, 'persuation': {'value': 0, 'enabled': False}, 'religion': {'value': 0, 'enabled': False}, 'slightOfHand': {'value': 0, 'enabled': False}, 'stealth': {'value': 0, 'enabled': False}, 'survival': {'value': 0, 'enabled': False}}, 'attacksSpellcasting': {'notes': '', 'attacks': [{'name': '', 'atkBonus': '', 'damageType': ''}]}, 'personalityTraits': '', 'ideals': '', 'bonds': '', 'flaws': '', 'featuresTraits': '', 'age': 0, 'height': '', 'weight': '', 'eyes': '', 'skin': '', 'hair': '', 'factionRank': '', 'additionalFeaturesTraits': '', 'Treasure': [], 'characterBackstory': ''}
        '''
        tk.Label(self.master, text='test window').pack()
        tk.Button(self.master, text='Test', command=self.buttonClickTest).pack()
        '''
        nb = ttk.Notebook(self.master)
        characters = ttk.Frame(nb)
        dice = ttk.Frame(nb)
        mapPane = ttk.Frame(nb) 
        
        
        
        char = MainSheet(characters, characterSheet)
        die = Dice(dice)
        worldMap = WorldMap(mapPane)
        

        nb.add(characters, text='Characters')
        nb.add(dice, text='Dice')
        nb.add(mapPane,text='World Map')
        
        nb.pack(expand=1, fill='both')
        
        
        '''
        window = tk.Toplevel()
        window.geometry('200x200')
        self.label1 = tk.Label(window, text= 'this is the second window')
        self.label1.pack()
        '''
        self.master.mainloop()
        
    def ProgLoop(self):
        self.master.mainloop()
        
    def buttonClickTest(self):
        self.label1['text']='dave'
        


if __name__ == '__main__':
    
    root = Tk()
    
    l = launcher(root)