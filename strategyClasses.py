from baseClasses import Strategy
import random

# A strategy that would cooperate fir the first round and then repeats the opponents last move

class TitForTat(Strategy):
    def __init__(self):
        super().__init__()
        self.strategyName = "Tit For Tat"
    
    def cooperationReaction(self):
        self.cooperate()

    def defectionReaction(self):
        self.defect()

    def startingReaction(self):
        self.cooperate()

# A strategy that would always cooperate

class AlwaysCooperate(Strategy):
    def __init__(self):
        super().__init__()
        self.strategyName="Always Cooperate"

    def cooperationReaction(self):
        self.cooperate()

    def defectionReaction(self):
        self.cooperate()

    def startingReaction(self):
        self.cooperate()

# A strategy that would always defect

class AlwaysDefect(Strategy):
    def __init__(self):
        super().__init__()
        self.strategyName="Always Defect"

    def cooperationReaction(self):
        self.defect()

    def defectionReaction(self):
        self.defect()

    def startingReaction(self):
        self.defect()

# A strategy that would move randomly

class RandomStrategy(Strategy):
    def __init__(self):
        super().__init__()
        self.strategyNamae="Random Strategy"

    def cooperationReaction(self):
        exec(random.choice(["self.defect()", "self.cooperate()"]))

    def defectionReaction(self):
        self.cooperationReaction()

    def startingReaction(self):
        self.cooperationReaction()

# A strategy that would cooperate first and then defect for 2 continuous rounds and then repreat itelf. Like: C, D, D, C, D, D, C

class DoubleD(Strategy):
    def __init__(self):
        super().__init__()
        self.strategyName="Double D"
        self.tracker=0

    def cooperate(self):
        self.tracker+=2
        return "cooperate"

    def defect(self):
        self.tracker-=1
        return "defect"

    def startingReaction(self):
        
        self.cooperate()

    def cooperationReaction(self):
        if(self.tracker!=0):
            
            self.defect()
        else:
            self.cooperate
    
    def defectionReaction(self):
        self.cooperationReaction()

# A strategy that would cooperate first but defects if opponent defects once

class GrimTrigger(Strategy):
    def __init__(self):
        super().__init__()
        self.strategyName="Grim Trigger"
        self.defected=False
       
    def startingReaction(self):
        self.cooperate()

    def cooperationReaction(self):
        if(self.defected):
            self.defect()
        else:
            self.cooperate()

    def defectionReaction(self):
        self.defected=True
        self.defect()

