import baseClasses
import strategyClasses
import argparse

payOffMatrix={
    "CC":(3,3),
    "CD":(0,5),
    "DC":(5,0),
    "DD":(1,1),
    }
def parse_args():
    parser=argparse.ArgumentParser(
       prog="PrisonerSim",
       description="Run a PrsionerSim Tournament",
      )

    parser.add_argument('--strategies', required=True, help="Comma-separated list of strategy names (e.g., TitForTat,AlwaysCooperate")
    parser.add_argument('--rounds', default=100, type=int, help="Number of rounds to run")
    return parser.parse_args()

def main():
    args=parse_args()  

    availableStrategies={
        "TitForTat":strategyClasses.TitForTat(),
        "AlwaysCooperate":strategyClasses.AlwaysCooperate(),
        "AlwaysDefect":strategyClasses.AlwaysDefect(),
        "RandomStrategy":strategyClasses.RandomStrategy(),
        "DoubleD":strategyClasses.DoubleD(),
        "GrimTrigger":strategyClasses.GrimTrigger(),
        "Pavlov":strategyClasses.Pavlov(),
        "GenerousTitForTat":strategyClasses.GenerousTitForTat(),
        }

    strategies=args.strategies.split(",")

    strategyObj=[availableStrategies[strategy] for strategy in strategies]

    tournament=baseClasses.Tournament(strategyObj,args.rounds,payOffMatrix)
    tournament.runTournament()
    tournamentWinner=tournament.getWinner()
    print("...")
    print(f"The winner of the tournament is {tournamentWinner}")

if __name__=="__main__":
    main()


