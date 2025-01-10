import baseClasses
import argparse
import os
import json
import colorama
import strategyClasses

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

    parser.add_argument('--strategies', default="TitForTat,AlwaysCooperate,AlwaysDefect,RandomStrategy,DoubleD,GrimTrigger,Pavlov,GenerousTitForTat", help="Comma-separated list of strategy names (e.g., TitForTat,AlwaysCooperate)")
    parser.add_argument('--rounds', default=100, type=int, help="Number of rounds to run")
    parser.add_argument('--payoff',default=" ", help="Path to file containing payoff matrix in JSON format (eg. {CC: [3, 3],CD: [0, 5],DC: [5, 0],DD: [1, 1]}")
    return parser.parse_args()

def main():
    args=parse_args()  
    # Get the name of all available strategies by using list comprehensions
    availableStrategies={cls.__name__:cls() for cls in baseClasses.Strategy.__subclasses__()}
    global payOffMatrix
    if os.path.isfile(args.payoff):
                with open(args.payoff, "r") as f:
                    if f.read():
                        payOffMatrix=json.load(f)
    
    strategies=args.strategies.split(",")
    # Check if the strategies are valid
    invalidStrategies=[strategy for strategy in strategies if strategy not in availableStrategies.keys()]
    if invalidStrategies:
        raise ValueError(f"Invalid strategies: {','.join(invalidStrategies)}")

    strategyObj=[availableStrategies[strategy] for strategy in strategies]

    tournament=baseClasses.Tournament(strategyObj,args.rounds,payOffMatrix)
    tournament.runTournament()
    tournamentWinner=tournament.getWinner()
    print("...")
    for strategy,score in tournament.getScore().items():
        print(f"{colorama.Fore.LIGHTBLUE_EX}{strategy} scored {score}")
    print(f"{colorama.Fore.RED}The winner of the tournament is {tournamentWinner}")

if __name__=="__main__":
    main()