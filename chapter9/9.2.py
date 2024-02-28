class ContextMemory():
    def __init__(self):
        self.currentContext = "None"
        self.currentHuman = None # pointer to the data file for the human we are currentl talking to
        self.humanFile = []
        self.emotion = "happy"
        self.humanEmotion = "happy"
        self.contextDict={}
        self.contextDict['currentHuman'] = self.currentHuman
        self.contextDict['robotEmotion'] = self.emotion
        self.contextDict['humanEmotion'] = self.humanEmotion
        
    def inContext(self, datum):
        if datum in self.contextDict:
            return self.contextDict[datum]
        else:
            return 0
            
    def setHuman(self,human):
        self.currentHuman = human
        self.humanFile.append(human)  # add this person to the database of people we know
        
    def addHuman(self,human):
        self.humanFile.append(human)
