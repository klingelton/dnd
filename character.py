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
        
    def BuildFrame(self):
        pass
    
    def LoadCharacter(self):
        pass
    
    def SaveCharacter(self):
        pass
    
    def getCharacterUpdates(self):
        return self.updates
    
class skills(Frame):
    def __init__(self, characterSheet):
        super(skills, self).__init__()
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