from baseClasses import Strategy
import random

# A strategy that would cooperate fir the first round and then repeats the opponents last move

class TitForTat(Strategy):
    def __init__(self):
        super().__init__()
        self.strategyName = "Tit For Tat"

    def reset(self):
        pass
    
    def cooperationReaction(self):
        return self.cooperate()

    def defectionReaction(self):
        return self.defect()

    def startingReaction(self):
        self.reset()
        return self.cooperate()

# A strategy that would always cooperate

class AlwaysCooperate(Strategy):
    def __init__(self):
        super().__init__()
        self.strategyName="Always Cooperate"

    def reset(self):
        pass

    def cooperationReaction(self):
        return self.cooperate()

    def defectionReaction(self):
        return self.cooperate()

    def startingReaction(self):
        self.reset()
        return self.cooperate()

# A strategy that would always defect

class AlwaysDefect(Strategy):
    def __init__(self):
        super().__init__()
        self.strategyName="Always Defect"

    def reset(self):
        pass

    def cooperationReaction(self):
        return self.defect()

    def defectionReaction(self):
        return self.defect()

    def startingReaction(self):
        self.reset()
        return self.defect()

# A strategy that would move randomly

class RandomStrategy(Strategy):
    def __init__(self):
        super().__init__()
        self.strategyName="Random Strategy"

    def reset(self):
        pass

    def cooperationReaction(self):
        return random.choice([self.defect, self.cooperate])()

    def defectionReaction(self):
        return self.cooperationReaction()

    def startingReaction(self):
        self.reset()
        return self.cooperationReaction()

# A strategy that would cooperate first and then defect for 2 continuous rounds and then repreat itelf. Like: C, D, D, C, D, D, C

class DoubleD(Strategy):
    def __init__(self):
        super().__init__()
        self.strategyName="Double D"
        self.tracker=0

    def reset(self):
        self.tracker=0

    def cooperate(self):
        self.tracker+=2
        return "cooperate"

    def defect(self):
        self.tracker-=1
        return "defect"

    def startingReaction(self):
        self.reset()
        return self.cooperate()

    def cooperationReaction(self):
        if(self.tracker!=0):
            return self.defect()
            print("defected")
        else:
            return self.cooperate()
    
    def defectionReaction(self):
        return self.cooperationReaction()

# A strategy that would cooperate first but defects if opponent defects once

class GrimTrigger(Strategy):
    def __init__(self):
        super().__init__()
        self.strategyName="Grim Trigger"
        self.defected=False

    def reset(self):
        self.defected=False
       
    def startingReaction(self):
        self.reset()
        return self.cooperate()

    def cooperationReaction(self):
        if(self.defected):
            return self.defect()
        else:
            return self.cooperate()

    def defectionReaction(self):
        self.defected=True
        return self.defect()

# A strategy that shifts its move if it loses 

class Pavlov(Strategy):
    def __init__(self):
        super().__init__()
        self.strategyName="Pavlov"
        self.lastMove="cooperate"
        self.currentMove=self.cooperate

    def reset(self):
        self.lastMove="cooperate"
        self.currentMove=self.cooperate

    def cooperate(self):
        self.lastMove="cooperate"
        return "cooperate"
    def defect(self):
        self.lastMove="defect"
        return "defect"
    def startingReaction(self):
         self.reset()
         return self.currentMove()
    def shiftMove(self):
        if self.currentMove==self.cooperate:
           self.currentMove=self.defect
        else:
            self.currentMove=self.cooperate
    def cooperationReaction(self):
        return self.currentMove()
    def defectionReaction(self):
        if(self.lastMove=="cooperate"):
            self.shiftMove()
            
        return self.currentMove()
            


# A strategy that cooperates initially and then copies the opponents last move but occasioanlly cooperate even after they defect

class GenerousTitForTat(Strategy):
    def __init__(self):
        super().__init__()
        self.strategyName="Generous Tit for Tat"

    def reset(self):
        pass

    def cooperationReaction(self):
        return self.cooperate()

    def startingReaction(self):
        self.reset()
        return self.cooperate()

    def defectionReaction(self):
        # Implement a percentage thing for 10% chance of cooperate
        if random.random()>0.1:
            return self.defect()
        else:
            return self.cooperate()


