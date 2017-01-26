from tkinter import *

class characterDetails(Frame):
    def __init__(self, characterSheet):
        super(characterDetails, self).__init__()
        self.characterSheet = characterSheet
        self.updates={}
        self.entry = {}
    
    def BuildFrame(self):
        Label(self,text='Character Name').grid(row=0, column=0, rowspan=3)
        
        self.entry['characterName'] = Entry(self)
        self.entry['characterName'].grid(row=0, column=1, rowspan=3)
        
        Label(self,text='Class').grid(row=0, column=2)
        self.entry['class'] = Entry(self)
        self.entry['class'].grid(row=0, column=3)
        
        
        Label(self,text='Level').grid(row=0, column=4)
        self.entry['level']=Entry(self)
        self.entry['level'].grid(row=0, column=5)
        
        Label(self, text='Background').grid(row=0, column=6)
        self.entry['background']=Entry(self)
        self.entry['background'].grid(row=0,column=7)
        
        Label(self, text='Player Name').grid(row=1, column=2)
        self.entry['playerName']=Entry(self)
        self.entry['playerName'].grid(row=1, column=3)
        
        
        Label(self, text='Faction').grid(row=1, column=4)
        self.entry['faction']=Entry(self)
        self.entry['faction'].grid(row=1, column=5)
        
        Label(self, text='Race').grid(row=1, column=6)
        self.entry['race']=Entry(self)
        self.entry['race'].grid(row=1, column=7)
        
        Label(self, text='alignment').grid(row=3, column=2)
        self.entry['alignment']=Entry(self)
        self.entry['alignment'].grid(row=3, column=3)
        
        Label(self, text='Experience Points').grid(row=3, column=4)
        self.entry['experiencePoints']=Entry(self)
        self.entry['experiencePoints'].grid(row=3, column=5)
        
        Label(self, text='DCI Number').grid(row=3, column=6)
        self.entry['dciNumber']=Entry(self)
        self.entry['dciNumber'].grid(row=3, column=7)
    
    def LoadCharacter(self):
        for e in self.entry:
            self.entry[e].delete(0, END)
            self.entry[e].insert(0, self.characterSheet[e])    
    
    def SaveCharacter(self):
        for e in self.entry:
            self.updates[e] = self.entry[e].get()
    
    def getCharacterUpdates(self):
        return self.updates
    
class characterAttributes(Frame):
    def __init__(self, characterSheet):
        super(characterAttributes).__init__()
        self.characterSheet = characterSheet
        self.updates
        self.entry={}
    def BuildFrame(self):
        Label(self, text='Strength').grid(row=0, column=0)
        self.entry['strength']['value']=Entry(self)
        self.entry['strength']['value'].grid(row=1, column=0)
        self.entry['strength']['modifier']=Entry(self)
        self.entry['strength']['modifier'].grid(row=2,column=0)
        
        Label(self, text='Dexterity').grid(row=3, column=0)
        self.entry['dexterity']['value']=Entry(self)
        self.entry['dexterity']['value'].grid(row=4, column=0)
        self.entry['dexterity']['modifier']=Entry(self)
        self.entry['dexterity']['modifier'].grid(row=5,column=0)
        
        Label(self, text='Constitution').grid(row=6, column=0)
        self.entry['constitution']['value']=Entry(self)
        self.entry['constitution']['value'].grid(row=7, column=0)
        self.entry['constitution']['modifier']=Entry(self)
        self.entry['constitution']['modifier'].grid(row=8,column=0)
        
        Label(self, text='Intelligence').grid(row=9, column=0)
        self.entry['intelligence']['value']=Entry(self)
        self.entry['intelligence']['value'].grid(row=10, column=0)
        self.entry['intelligence']['modifier']=Entry(self)
        self.entry['intelligence']['modifier'].grid(row=11,column=0)
        
        Label(self, text='Wisdom').grid(row=12, column=0)
        self.entry['wisdom']['value']=Entry(self)
        self.entry['wisdom']['value'].grid(row=13, column=0)
        self.entry['wisdom']['modifier']=Entry(self)
        self.entry['wisdom']['modifier'].grid(row=14,column=0)
        
        Label(self, text='Charisma').grid(row=15, column=0)
        self.entry['charisma']['value']=Entry(self)
        self.entry['charisma']['value'].grid(row=16, column=0)
        self.entry['charisma']['modifier']=Entry(self)
        self.entry['charisma']['modifier'].grid(row=17,column=0) 
    
    def LoadCharacter(self):
        for e in self.entry:
            self.entry[e]['value'].delete(0,END)
            self.entry[e]['modifier'].delete(0,END)
            
            self.entry[e]['value'].insert(0, self.characterSheet['vitals'][e]['value'])
            self.entry[e]['modifier'].insert(0, self.characterSheet['vitals'][e]['modifier'])
    
    def SaveCharacter(self):
        for e in self.entry:
            self.updates[e]['value'] = self.entry[e]['value'].get()
            self.updates[e]['modifier'] = self.entry[e]['modifer'].get()
    
    def getCharacterUpdates(self):
        return self.updates
    
class savingThrows(Frame):
    def __init__(self, characterSheet):
        super(savingThrows, self).__init__()
        self.characterSheet = characterSheet
        self.updates
        self.entry
        
    def BuildFrame(self):
        self.entry['strength']['enabled'] = IntVar()
        self.entry['strength']['Checkbutton'] = Checkbutton(self, text='strength', Variable=self.entry['strength']['enabled']).grid(row=0, column=0)
        self.entry['strength']['value'] = Entry(self)
        self.entry['strength']['value'].grid(row=0,column=1)
        
        self.entry['dexterity']['enabled'] = IntVar()
        self.entry['dexterity']['Checkbutton'] = Checkbutton(self, text='dexterity', Variable=self.entry['dexterity']['enabled']).grid(row=1, column=0)
        self.entry['dexterity']['value'] = Entry(self)
        self.entry['dexterity']['value'].grid(row=1,column=1)
        
        self.entry['constitution']['enabled'] = IntVar()
        self.entry['constitution']['Checkbutton'] = Checkbutton(self, text='Constitution', Variable=self.entry['constitution']['enabled']).grid(row=2, column=0)
        self.entry['constitution']['value'] = Entry(self)
        self.entry['constitution']['value'].grid(row=2,column=1)
        
        self.entry['intelligence']['enabled'] = IntVar()
        self.entry['intelligence']['Checkbutton'] = Checkbutton(self, text='Intelligence', Variable=self.entry['intelligence']['enabled']).grid(row=3, column=0)
        self.entry['intelligence']['value'] = Entry(self)
        self.entry['intelligence']['value'].grid(row=3,column=1)
        
        self.entry['wisdom']['enabled'] = IntVar()
        self.entry['wisdom']['Checkbutton'] = Checkbutton(self, text='Wisdom', Variable=self.entry['wisdom']['enabled']).grid(row=4, column=0)
        self.entry['wisdom']['value'] = Entry(self)
        self.entry['wisdom']['value'].grid(row=4,column=1)
        
        self.entry['charisma']['enabled'] = IntVar()
        self.entry['charisma']['Checkbutton'] = Checkbutton(self, text='Charisma', Variable=self.entry['charisma']['enabled']).grid(row=4, column=0)
        self.entry['charisma']['value'] = Entry(self)
        self.entry['charisma']['value'].grid(row=4,column=1)
    
    def LoadCharacter(self):
        for e in self.entry:
            self.entry[e]['Checkbutton'].deselect()
            self.entry[e]['value'].delete(0,END)
            
            if self.characterSheet['savingThrows'][e]['enabled']:
                self.entry[e]['Checkbutton'].select()
                
            self.entry[e]['value'] = self.characterSheet['savingThrows'][e]['value']
    
    def SaveCharacter(self):
        for e in self.entry:
            self.updates['savingThrows'][e]['enabled'] = self.entry[e]['enabled'].get()
            self.updates['savingThrows'][e]['value'] = self.entry[e]['value'].get()
    
    def getCharacterUpdates(self):
        return self.updates
    
class skills(Frame):
    def __init__(self, characterSheet):
        super(skills, self).__init__()
        self.characterSheet = characterSheet
        self.updates = {}
        
    def BuildFrame(self):
        self.entry['acrobatics']['enabled'] = IntVar()
        self.entry['acrobatics']['Checkbutton'] = Checkbutton(self, text='acrobatics', Variable=self.entry['acrobatics']['enabled']).grid(row=0, column=0)
        self.entry['acrobatics']['value'] = Entry(self)
        self.entry['acrobatics']['value'].grid(row=0,column=1)
        
        self.entry['animalHandling']['enabled'] = IntVar()
        self.entry['animalHandling']['Checkbutton'] = Checkbutton(self, text='animalHandling', Variable=self.entry['animalHandling']['enabled']).grid(row=1, column=0)
        self.entry['animalHandling']['value'] = Entry(self)
        self.entry['animalHandling']['value'].grid(row=1,column=1)
        
        
        self.entry['arcana']['enabled'] = IntVar()
        self.entry['arcana']['Checkbutton'] = Checkbutton(self, text='arcana', Variable=self.entry['arcana']['enabled']).grid(row=2, column=0)
        self.entry['arcana']['value'] = Entry(self)
        self.entry['arcana']['value'].grid(row=2,column=1)
        
        self.entry['athletics']['enabled'] = IntVar()
        self.entry['athletics']['Checkbutton'] = Checkbutton(self, text='athletics', Variable=self.entry['athletics']['enabled']).grid(row=3, column=0)
        self.entry['athletics']['value'] = Entry(self)
        self.entry['athletics']['value'].grid(row=3,column=1)
        
        self.entry['deception']['enabled'] = IntVar()
        self.entry['deception']['Checkbutton'] = Checkbutton(self, text='deception', Variable=self.entry['deception']['enabled']).grid(row=4, column=0)
        self.entry['deception']['value'] = Entry(self)
        self.entry['deception']['value'].grid(row=4,column=1)
        
        self.entry['history']['enabled'] = IntVar()
        self.entry['history']['Checkbutton'] = Checkbutton(self, text='history', Variable=self.entry['history']['enabled']).grid(row=5, column=0)
        self.entry['history']['value'] = Entry(self)
        self.entry['history']['value'].grid(row=5,column=1)
        
        self.entry['insight']['enabled'] = IntVar()
        self.entry['insight']['Checkbutton'] = Checkbutton(self, text='insight', Variable=self.entry['insight']['enabled']).grid(row=6, column=0)
        self.entry['insight']['value'] = Entry(self)
        self.entry['insight']['value'].grid(row=6,column=1)
        
        self.entry['intimidation']['enabled'] = IntVar()
        self.entry['intimidation']['Checkbutton'] = Checkbutton(self, text='intimidation', Variable=self.entry['intimidation']['enabled']).grid(row=7, column=0)
        self.entry['intimidation']['value'] = Entry(self)
        self.entry['intimidation']['value'].grid(row=7,column=1)
        
        self.entry['investigation']['enabled'] = IntVar()
        self.entry['investigation']['Checkbutton'] = Checkbutton(self, text='investigation', Variable=self.entry['investigation']['enabled']).grid(row=8, column=0)
        self.entry['investigation']['value'] = Entry(self)
        self.entry['investigation']['value'].grid(row=8,column=1)
        
        self.entry['medicine']['enabled'] = IntVar()
        self.entry['medicine']['Checkbutton'] = Checkbutton(self, text='medicine', Variable=self.entry['medicine']['enabled']).grid(row=9, column=0)
        self.entry['medicine']['value'] = Entry(self)
        self.entry['medicine']['value'].grid(row=9,column=1)
        
        self.entry['nature']['enabled'] = IntVar()
        self.entry['nature']['Checkbutton'] = Checkbutton(self, text='nature', Variable=self.entry['nature']['enabled']).grid(row=10, column=0)
        self.entry['nature']['value'] = Entry(self)
        self.entry['nature']['value'].grid(row=10,column=1)
        
        self.entry['perception']['enabled'] = IntVar()
        self.entry['perception']['Checkbutton'] = Checkbutton(self, text='perception', Variable=self.entry['perception']['enabled']).grid(row=11, column=0)
        self.entry['perception']['value'] = Entry(self)
        self.entry['perception']['value'].grid(row=11,column=1)
        
        self.entry['performance']['enabled'] = IntVar()
        self.entry['performance']['Checkbutton'] = Checkbutton(self, text='performance', Variable=self.entry['performance']['enabled']).grid(row=12, column=0)
        self.entry['performance']['value'] = Entry(self)
        self.entry['performance']['value'].grid(row=12,column=1)
        
        self.entry['persuasion']['enabled'] = IntVar()
        self.entry['persuasion']['Checkbutton'] = Checkbutton(self, text='persuasion', Variable=self.entry['persuasion']['enabled']).grid(row=13, column=0)
        self.entry['persuasion']['value'] = Entry(self)
        self.entry['persuasion']['value'].grid(row=13,column=1)
        
        self.entry['religion']['enabled'] = IntVar()
        self.entry['religion']['Checkbutton'] = Checkbutton(self, text='religion', Variable=self.entry['religion']['enabled']).grid(row=14, column=0)
        self.entry['religion']['value'] = Entry(self)
        self.entry['religion']['value'].grid(row=14,column=1)
        
        self.entry['sleightOfHand']['enabled'] = IntVar()
        self.entry['sleightOfHand']['Checkbutton'] = Checkbutton(self, text='sleightOfHand', Variable=self.entry['sleightOfHand']['enabled']).grid(row=15, column=0)
        self.entry['sleightOfHand']['value'] = Entry(self)
        self.entry['sleightOfHand']['value'].grid(row=15,column=1)
        
        self.entry['stealth']['enabled'] = IntVar()
        self.entry['stealth']['Checkbutton'] = Checkbutton(self, text='stealth', Variable=self.entry['stealth']['enabled']).grid(row=16, column=0)
        self.entry['stealth']['value'] = Entry(self)
        self.entry['stealth']['value'].grid(row=16,column=1)
        
        self.entry['survival']['enabled'] = IntVar()
        self.entry['survival']['Checkbutton'] = Checkbutton(self, text='survival', Variable=self.entry['survival']['enabled']).grid(row=17, column=0)
        self.entry['survival']['value'] = Entry(self)
        self.entry['survival']['value'].grid(row=17,column=1)
        
    
    def LoadCharacter(self):
        for e in self.entry:
            self.entry[e]['Checkbutton'].deselect()
            self.entry[e]['value'].delete(0,END)
            
            if self.characterSheet['skills'][e]['enabled']:
                self.entry[e]['Checkbutton'].select()
                
            self.entry[e]['value'] = self.characterSheet['skills'][e]['value']
            
    
    def SaveCharacter(self):
        for e in self.entry:
            self.updates[e]['value'] = self.entry[e]['value'].get()
            self.updates[e]['modifier'] = self.entry[e]['modifer'].get()
    
    def getCharacterUpdates(self):
        return self.updates
    
class otherProficiencies(Frame):
    def __init__(self, characterSheet):
        super(otherProficiencies, self).__init__()
        self.characterSheet = characterSheet
        self.updates = {}
        
    def BuildFrame(self):
        pass
    
    def LoadCharacter(self):
        pass
    
    def SaveCharacter(self):
        pass
    
    def getCharacterUpdates(self):
        return self.updates
    
class defence(Frame):
    def __init__(self, characterSheet):
        super(defence, self).__init__()
        self.characterSheet = characterSheet
        self.updates = {}
        
    def BuildFrame(self):
        pass
    
    def LoadCharacter(self):
        pass
    
    def SaveCharacter(self):
        pass
    
    def getCharacterUpdates(self):
        return self.updates
    
class attacksAndSpellcasting(Frame):
    def __init__(self, characterSheet):
        super(attacksAndSpellcasting, self).__init__()
        self.characterSheet = characterSheet
        self.updates = {}
        
    def BuildFrame(self):
        pass
    
    def LoadCharacter(self):
        pass
    
    def SaveCharacter(self):
        pass
    
    def getCharacterUpdates(self):
        return self.updates
    
class equipment(Frame):
    def __init__(self, characterSheet):
        super(equipment, self).__init__()
        self.characterSheet = characterSheet
        self.updates = {}
        
    def BuildFrame(self):
        pass
    
    def LoadCharacter(self):
        pass
    
    def SaveCharacter(self):
        pass
    
    def getCharacterUpdates(self):
        return self.updates
    
class background(Frame):
    def __init__(self, characterSheet):
        super(background, self).__init__()
        self.characterSheet = characterSheet
        self.updates = {}
        
    def BuildFrame(self):
        pass
    
    def LoadCharacter(self):
        pass
    
    def SaveCharacter(self):
        pass
    def getCharacterUpdates(self):
        return self.updates

class featuresAndTraits(Frame):
    def __init__(self, characterSheet):
        super(featuresAndTraits, self).__init__()
        self.characterSheet = characterSheet
        self.updates = {}
        
    def BuildFrame(self):
        pass
    
    def LoadCharacter(self):
        pass
    
    def SaveCharacter(self):
        pass
    
    def getCharacterUpdates(self):
        return self.updates


class character(Frame):
    def __init__(self, characterSheet):
        super(character, self).__init__()
        self.characterSheet = characterSheet
        self.updates={}
        
    def BuildCharacterSheet(self):
        pass
        
    def getCharacterSheet(self):
        return self.characterSheet