'''
Created on 16 Jan 2017

@author: admin
'''

import tkinter as tk
from tkinter import ttk

import random



class WorldMap:
    def __init__(self, frame):
        self.frame = frame
        self.DrawMap()
    
    def DrawMap(self):
        canvas = tk.Canvas(self.frame) 
        canvas.pack()
        
        canvas.create_rectangle(50,25,100,100)

class CharacterDetails(tk.Frame):
    def __init__(self, master, characterSheet):
        tk.Frame.__init__(self, master)
        self.characterSheet = characterSheet
        
        tk.Label(self, text='characterName').grid(row=0, column=0, rowspan=3)
        self.characterName = tk.Entry(self)
        self.characterName.grid(row=0, column=1, rowspan=3)
        
        tk.Label(self, text='class').grid(row=0, column=2)
        self.pClass = tk.Entry(self)
        self.pClass.grid(row=0, column=3)
        
        tk.Label(self, text='level').grid(row=0, column=4)
        self.level = tk.Entry(self)
        self.level.grid(row=0, column=5)
        
        tk.Label(self, text='background').grid(row=0, column=6)
        self.background = tk.Entry(self)
        self.background.grid(row=0, column=7)
        
        tk.Label(self,text='playerName').grid(row=1, column=2)
        self.playerName = tk.Entry(self)
        self.playerName.grid(row=1, column=3)
        
        tk.Label(self, text='faction').grid(row=1, column=4)
        self.faction = tk.Entry(self)
        self.faction.grid(row=1, column=5)
        
        tk.Label(self, text='race').grid(row=1, column=6)
        self.race = tk.Entry(self)
        self.race.grid(row=1, column=7)
        
        tk.Label(self, text='alignment').grid(row=2, column=2)
        self.alignment=tk.Entry(self)
        self.alignment.grid(row=2, column=3)
        
        tk.Label(self, text='experience points').grid(row=2, column=4)
        self.experiencePoints = tk.Entry(self)
        self.experiencePoints.grid(row=2, column=5)
        
        tk.Label(self, text='DCI Number').grid(row=2, column=6)
        self.dciNumber = tk.Entry(self)
        self.dciNumber.grid(row=2, column=7)
        
        self.LoadCharacter()
        
    def CharacterUpdates(self): 
        characterUpdate = {}
        
        characterUpdate['characterName'] = self.characterName.get()
        characterUpdate['class']=self.pClass.get()
        characterUpdate['level']=self.level.get()
        characterUpdate['background']=self.background.get()
        characterUpdate['playerName']=self.playerName.get()
        characterUpdate['faction']=self.faction.get()
        characterUpdate['race']=self.race.get()
        characterUpdate['alignment']=self.alignment.get()
        characterUpdate['experiencePoints']=self.experiencePoints.getint()
        characterUpdate['dciNumber']=self.dciNumber.getint()
        return characterUpdate

    def LoadCharacter(self):
        self.characterName.delete(0, tk.END)
        self.characterName.insert(0, self.characterSheet['characterName'])
        
        self.pClass.delete(0, tk.END)
        self.pClass.insert(0, self.characterSheet['class'])
        
        self.level.delete(0,tk.END)
        self.level.insert(0, self.characterSheet['level'])
        
        self.background.delete(0, tk.END)
        self.background.insert(0, self.characterSheet['background'])
        
        self.playerName.delete(0,tk.END)
        self.playerName.insert(0, self.characterSheet['playerName'])
        
        self.faction.delete(0, tk.END)
        self.faction.insert(0, self.characterSheet['faction'])
        
        self.race.delete(0,tk.END)
        self.race.insert(0, self.characterSheet['race'])


class Character:
    def __init__(self, frame, characterSheet):
        self.frame = frame
        self.characterSheet = characterSheet
        
        self.BuildCharacter()
        self.LoadCharacter()
        
        tk.Button(self.frame, text='Save',command=self.SaveCharacter).pack()
        
    def BuildCharacter(self):
        char = CharacterDetails(self.frame, self.characterSheet)
        
        vitals = tk.Frame(self.frame)
        skills = tk.Frame(self.frame)
                
        tk.Label(vitals, text='Strength').grid(row=0, column=0)
        self.strength = tk.Entry(vitals)
        self.strength.grid(row=0, column=1)
        
        tk.Label(vitals, text='Dexterity').grid(row=1, column=0)
        self.dexterity = tk.Entry(vitals)
        self.dexterity.grid(row=1,column=1)
        
        tk.Label(vitals, text='Constitution').grid(row=2, column=0)
        self.constitution = tk.Entry(vitals)
        self.constitution.grid(row=2, column=1)
        
        tk.Label(vitals, text='Intelligence').grid(row=3, column=0)
        self.intelligence = tk.Entry(vitals)
        self.intelligence.grid(row=3, column=1)
        
        tk.Label(vitals, text='Wisdom').grid(row=4, column=0)
        self.wisdom=tk.Entry(vitals)
        self.wisdom.grid(row=4, column=1)
        
        tk.Label(vitals, text='Charisma').grid(row=5, column=0)
        self.charisma = tk.Entry(vitals)
        self.charisma.grid(row=5, column=1)
        
        
        ttk.Separator(vitals, orient=tk.HORIZONTAL).grid(row=6, columnspan=2, sticky='ew')
        
        tk.Label(vitals, text='Passive Wisdom (Perception)').grid(row=7, column=0)
        self.passiveWisdom = tk.Entry(vitals)
        self.passiveWisdom.grid(row=7, column=1)
        
        ttk.Separator(vitals, orient=tk.HORIZONTAL).grid(row=8, columnspan=2, sticky='ew')
        
        tk.Label(vitals, text='Other Proficiencies and Languages').grid(row=9, columnspan=2)
        self.otherProficiencies = tk.Text(vitals, width='15')
        self.otherProficiencies.grid(row=10, columnspan=2, sticky='ew')
        
        tk.Label(skills, text='Inspiration').grid(row=0, column=1)
        self.inspiration = tk.Entry(skills, width=3)
        self.inspiration.grid(row=0, column=0)
        
        tk.Label(skills, text='Proficiency Bonus').grid(row=1,column=1)
        self.proficiencyBonus = tk.Entry(skills, width=3)
        self.proficiencyBonus.grid(row=1,column=0)
        
        
        
        
        char.pack(fill=tk.X)
        vitals.pack(side=tk.LEFT, fill=tk.X)
        
        skills.pack(side=tk.LEFT, fill=tk.X)
        
    def LoadCharacter(self):
                
        self.strength.delete(0, tk.END)
        self.strength.insert(0, self.characterSheet['vitals']['strength'])
        
        self.dexterity.delete(0, tk.END)
        self.dexterity.insert(0,self.characterSheet['vitals']['dexterity'])
        
        self.constitution.delete(0,tk.END)
        self.constitution.insert(0,self.characterSheet['vitals']['dexterity'])
        
        self.intelligence.delete(0, tk.END)
        self.intelligence.insert(0, self.characterSheet['vitals']['intelligence'])
        
        self.wisdom.delete(0,tk.END)
        self.wisdom.insert(0, self.characterSheet['vitals']['intelligence'])
        
        self.charisma.delete(0,tk.END)
        self.charisma.insert(0, self.characterSheet['vitals']['charisma'])
        
        self.otherProficiencies.delete(1.0, tk.END)
        self.otherProficiencies.insert(1.0, self.characterSheet['otherProficiencies'])

    def SaveCharacter(self):
        self.characterSheet['characterName'] = self.characterName.get()
        self.characterSheet['class'] = self.pClass.get()
        self.characterSheet['level'] = self.level.getint(0)
        self.characterSheet['background'] = self.background.get()
        self.characterSheet['playerName'] = self.playerName.get()
        self.characterSheet['faction'] = self.faction.get()
        self.characterSheet['race'] =self.race.get()
        self.characterSheet['alignment']=self.alignment.get()
        self.characterSheet['experiencePoints']=self.experiencePoints.get()
        self.characterSheet['dciNumber']=self.dciNumber.get()

        
        self.characterSheet['vitals']['strength']=self.strength.get()
        self.characterSheet['vitals']['dexterity']=self.dexterity.get()
        self.characterSheet['vitals']['constiturion']=self.constitution.get()
        self.characterSheet['vitals']['intelligence']=self.intelligence.get()
        self.characterSheet['vitals']['wisdom']=self.wisdom.get()
        self.characterSheet['vitals']['charisma']=self.charisma.get()
        self.characterSheet['passiveWisdom']=self.passiveWisdom.get()
        self.characterSheet['otherProficiencies']=self.otherProficiencies.get(1.0, tk.END)
        
        print(self.characterSheet)
        
class Dice:
    def __init__(self, frame):
        self.frame = frame
        self.BuildDice()
    
    def BuildDice(self):
        tk.Button(self.frame, text='D20', command=self.rollD20).grid(row=0, column=0)
        tk.Button(self.frame, text='D10', command=self.rollD10).grid(row=1, column=0)
        tk.Button(self.frame, text='D8', command=self.rollD8).grid(row=2,column=0)
        tk.Button(self.frame, text='D6', command=self.rollD6).grid(row=3, column=0)
        tk.Button(self.frame, text='D4', command=self.rollD4).grid(row=4, column=0)
        tk.Button(self.frame, text='Percentage', command=self.rollPercentage).grid(row=5, column=0)
        self.result = tk.Entry(self.frame)
        self.result.grid(row=6,column=0)
        
    def rollD20(self):
        self.result.delete(0, tk.END)
        self.result.insert(0, str(random.randint(1,20)))
    
    def rollD10(self):
        self.result.delete(0, tk.END)
        self.result.insert(0, str(random.randint(1,10)))
        
    def rollD8(self):
        self.result.delete(0, tk.END)
        self.result.insert(0, random.randint(1,8))
    
    def rollD6(self):
        self.result.delete(0, tk.END)
        self.result.insert(0, random.randint(1,6))
        
    def rollD4(self):
        self.result.delete(0, tk.END)
        self.result.insert(0, random.randint(1,4))    
    
    def rollPercentage(self):
        self.result.delete(0, tk.END)
        self.result.insert(0, random.randint(1,100))

class launcher:
    def __init__(self, master):
        self.master = master
        self.master.attributes('-fullscreen',True)
        
        
        '''
        tk.Label(self.master, text='test window').pack()
        tk.Button(self.master, text='Test', command=self.buttonClickTest).pack()
        '''
        nb = ttk.Notebook(self.master)
        characters = ttk.Frame(nb)
        dice = ttk.Frame(nb)
        mapPane = ttk.Frame(nb) 
        
        characterScroll = tk.Scrollbar(characters)
        characterScroll.config(orient=tk.VERTICAL)
        characterScroll.pack(side=tk.RIGHT, fill=tk.Y)
        
        charScrollHor = tk.Scrollbar(characters)
        charScrollHor.config(orient=tk.HORIZONTAL)
        charScrollHor.pack(side=tk.BOTTOM, fill=tk.Y)
        
        characterSheet = {'characterId':123, 'characterName': 'dave', 'class': '', 'level': 0, 'background': '', 'playerName': '', 'faction': '', 'race': 'race', 'alignment': '', 'experiencePoints': '', 'dciNumber': '', 'vitals': {'strength': 0, 'dexterity': 0, 'constitution': 0, 'intelligence': 0, 'wisdom': 0, 'charisma': 0}, 'passiveWisdom': 0, 'otherProficiencies': 'jasodijasio\nauishduihasuhaiuhsdiuhas\n', 'armourClass': 0, 'initiative': 0, 'speed': 0, 'hitPoints': {'hitpointMax': 0, 'currentHitPoints': 0, 'temporaryHitPoints': 0}, 'savingThrows': {'strength': 0, 'dexterity': 0, 'constitution': 0, 'intelligence': 0, 'wisdom': 0, 'charisma': 0}, 'skills': {'acrobatics': {'value': 0, 'enabled': False}, 'animalHandling': {'value': 0, 'enabled': False}, 'arcana': {'value': 0, 'enabled': False}, 'athletics': {'value': 0, 'enabled': False}, 'deception': {'value': 0, 'enabled': False}, 'history': {'value': 0, 'enabled': False}, 'insight': {'value': 0, 'enabled': False}, 'intimidation': {'value': 0, 'enabled': False}, 'investigation': {'value': 0, 'enabled': False}, 'medicine': {'value': 0, 'enabled': False}, 'nature': {'value': 0, 'enabled': False}, 'perception': {'value': 0, 'enabled': False}, 'performance': {'value': 0, 'enabled': False}, 'persuation': {'value': 0, 'enabled': False}, 'religion': {'value': 0, 'enabled': False}, 'slightOfHand': {'value': 0, 'enabled': False}, 'stealth': {'value': 0, 'enabled': False}, 'survival': {'value': 0, 'enabled': False}}, 'attacksSpellcasting': {'notes': '', 'attacks': [{'name': '', 'atkBonus': '', 'damageType': ''}]}, 'personalityTraits': '', 'ideals': '', 'bonds': '', 'flaws': '', 'featuresTraits': '', 'age': 0, 'height': '', 'weight': '', 'eyes': '', 'skin': '', 'hair': '', 'factionRank': '', 'additionalFeaturesTraits': '', 'Treasure': [], 'characterBackstory': ''}
        character = Character(characters, characterSheet)
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
    
    root = tk.Tk()
    
    l = launcher(root)