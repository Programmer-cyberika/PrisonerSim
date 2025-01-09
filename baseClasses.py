import itertools
import colorama
colorama.init()

class Strategy:
    def __init__(self):
        self.strategyName = None

    def getStrategyName(self):
        return self.strategyName

    def cooperationReaction(self):
        pass

    def defectionReaction(self):
        pass

    def startingReaction(self):
        pass

    def reset(self):
        pass
    
    def cooperate(self):
        return "cooperate"

    
    def defect(self):
        return "defect"


class Round:
    def __init__(self, participant1, participant2, payoffMatrix, participant1PreReaction, participant2PreReaction):
        self.participant1 = participant1
        self.participant2 = participant2
        self.participant1Score = 0
        self.participant2Score = 0
        self.participant1PreReaction = participant1PreReaction
        self.participant2PreReaction = participant2PreReaction
        self.pointsCC_1 = payoffMatrix["CC"][0]
        self.pointsCC_2 = payoffMatrix["CC"][1]
        self.pointsCD_1 = payoffMatrix["CD"][0]
        self.pointsCD_2 = payoffMatrix["CD"][1]
        self.pointsDC_1 = payoffMatrix["DC"][0]
        self.pointsDC_2 = payoffMatrix["DC"][1]
        self.pointsDD_1 = payoffMatrix["DD"][0]
        self.pointsDD_2 = payoffMatrix["DD"][1]

        self.participant1Reaction = None
        self.participant2Reaction = None

    def phase(self):
        if self.participant1PreReaction == "defect":
            self.participant2Reaction = self.participant2.defectionReaction()

        elif self.participant1PreReaction == "cooperate":
            self.participant2Reaction = self.participant2.cooperationReaction()

        if self.participant2PreReaction == "defect":
            self.participant1Reaction = self.participant1.defectionReaction()

        elif self.participant2PreReaction == "cooperate":
            self.participant1Reaction = self.participant1.cooperationReaction()

        if self.participant1PreReaction is None:
            self.participant2Reaction = self.participant2.startingReaction()
            self.participant1Reaction = self.participant1.startingReaction()

    def scoreCalculation(self):
        if self.participant1Reaction == "cooperate" and self.participant2Reaction == "cooperate":
            self.participant1Score = self.pointsCC_1
            self.participant2Score = self.pointsCC_2

        elif self.participant1Reaction == "cooperate" and self.participant2Reaction == "defect":
            self.participant1Score = self.pointsCD_1
            self.participant2Score = self.pointsCD_2

        elif self.participant1Reaction == "defect" and self.participant2Reaction == "defect":
            self.participant1Score = self.pointsDD_1
            self.participant2Score = self.pointsDD_2

        elif self.participant1Reaction == "defect" and self.participant2Reaction == "cooperate":
            self.participant1Score = self.pointsDC_1
            self.participant2Score = self.pointsDC_2

    def returnValue(self):
        return [self.participant1Reaction, self.participant2Reaction, self.participant1Score, self.participant2Score]

    def main(self):
        self.phase()
        self.scoreCalculation()
        return self.returnValue()


class Match:
    def __init__(self, participant1, participant2, rounds, payoffMatrix):

        self.participant1 = participant1
        self.participant2 = participant2
        self.rounds = rounds
        self.payoffMatrix = payoffMatrix
        self.participant1Points = 0
        self.participant2Points = 0
        self.winner = None

    def pointsUpdation(self, participant, points):
        """Update points for a participant."""
        if participant == "participant1":
            self.participant1Points += points
        elif participant == "participant2":
            self.participant2Points += points

    def runRounds(self):
        """Run all rounds and update points."""
        participant1PreReaction = None
        participant2PreReaction = None
        print("...")
        print("...")

        print(f"{colorama.Fore.LIGHTBLUE_EX}Starting match between {self.participant1.getStrategyName()} and {self.participant2.getStrategyName()}")
        for _ in range(self.rounds):
            round_obj = Round(

                participant1=self.participant1,
                participant2=self.participant2,
                payoffMatrix=self.payoffMatrix,
                participant1PreReaction=participant1PreReaction,
                participant2PreReaction=participant2PreReaction,
            )
            resultList = round_obj.main()
            self.pointsUpdation("participant1", resultList[2])
            self.pointsUpdation("participant2", resultList[3])
            print(f"{colorama.Fore.LIGHTRED_EX}Round Result: {resultList[0]} vs {resultList[1]}")
            participant1PreReaction = resultList[0]
            participant2PreReaction = resultList[1]

    def decideWinner(self):
        """Determine the winner based on points."""
        if self.participant1Points > self.participant2Points:
            self.winner = self.participant1.getStrategyName()
        elif self.participant1Points == self.participant2Points:
            self.winner = "draw"
        else:
            self.winner = self.participant2.getStrategyName()

    def returnResult(self):
        """Return the match results as a list."""
        self.displayResult()
        return [self.participant1Points, self.participant2Points, self.winner]

    def displayResult(self):
        print("...")
        print(f"{colorama.Fore.LIGHTGREEN_EX}Match result between {self.participant1.getStrategyName()} and {self.participant2.getStrategyName()}:-")
        print(f"{colorama.Fore.LIGHTRED_EX}{self.participant1.getStrategyName()} scored {self.participant1Points}")
        print(f"{colorama.Fore.LIGHTYELLOW_EX}{self.participant2.getStrategyName()} scored {self.participant2Points}")
        print(f"{colorama.Fore.LIGHTMAGENTA_EX}Match Winner: {self.winner}")


class Tournament:
    def __init__(self, participants, roundsPerMatch, payoffMatrix):

        self.participants = participants
        self.rounds = roundsPerMatch
        self.payoffMatrix = payoffMatrix
        self.results = {}
        self.winner=None
        self.score=dict()

    def getWinner(self):
        winnersList=list()
        max_value=max(self.score.values())
        
        for key,values in self.score.items():
                 if values==max_value:
                     winnersList.append(key)
        if len(winnersList)==1:
            return winnersList[0]
        else:
            return winnersList

    
    def keepScore(self, participant, score):
        if participant in self.score:
              self.score[participant] += score
        else:
            self.score[participant] = score

    def runMatch(self, participant1, participant2):
        match_obj = Match(
            participant1=participant1,
            participant2=participant2,
            rounds=self.rounds,
            payoffMatrix=self.payoffMatrix,
        )
        match_obj.runRounds()
        match_obj.decideWinner()
        result = match_obj.returnResult()
        self.keepScore(participant1.getStrategyName(), result[0])
        self.keepScore(participant2.getStrategyName(), result[1])
        

    def runTournament(self):

        print(colorama.Fore.LIGHTCYAN_EX + "--- PrisonerSim Tournament Results ---")

        print(colorama.Fore.CYAN+"Strategies", end=":  ")
        print(f"{colorama.Fore.GREEN}{len(self.participants)}", end="\n")

        print(colorama.Fore.CYAN+"Rounds per match", end=":  ")
        print(f"{colorama.Fore.GREEN}{(self.rounds)}", end="\n")

        print(colorama.Fore.CYAN+"Payoff Matrix", end=":  ")
        print(f"{colorama.Fore.GREEN}{self.payoffMatrix}", end="\n")

        print(colorama.Fore.WHITE+"...")

        for participant1, participant2 in list(itertools.combinations(self.participants,2)):
            self.runMatch(participant1, participant2)
            