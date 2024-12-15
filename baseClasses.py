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

    @staticmethod
    def cooperate():
        return "cooperate"

    @staticmethod
    def defect():
        return "defect"


class Round:
    def __init__(self, noisy, participant1, participant2, payoffMatrix, participant1PreReaction, participant2PreReaction):
        self.noisy = noisy
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
    def __init__(self, noisy, participant1, participant2, rounds, payoffMatrix):
        self.noisy = noisy
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
        for _ in range(self.rounds):
            round_obj = Round(
                noisy=self.noisy,
                participant1=self.participant1,
                participant2=self.participant2,
                payoffMatrix=self.payoffMatrix,
                participant1PreReaction=participant1PreReaction,
                participant2PreReaction=participant2PreReaction,
            )
            resultList = round_obj.main()
            self.pointsUpdation("participant1", resultList[2])
            self.pointsUpdation("participant2", resultList[3])
            participant1PreReaction = resultList[0]
            participant2PreReaction = resultList[1]

    def decideWinner(self):
        """Determine the winner based on points."""
        if self.participant1Points > self.participant2Points:
            self.winner = "participant1"
        elif self.participant1Points == self.participant2Points:
            self.winner = "draw"
        else:
            self.winner = "participant2"

    def returnResult(self):
        """Return the match results as a list."""
        return [self.participant1Points, self.participant2Points, self.winner]


class Tournament:
    def __init__(self, noisy, participants, roundPerMatch, payoffMatrix):
        self.roundPerMatch = roundPerMatch
        self.noisy = noisy
        self.participants = participants
        self.payoffMatrix = payoffMatrix
        self.winner = None
        self.score = None
