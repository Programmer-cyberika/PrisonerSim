# PrisonerSim

[![GitHub Repository](https://img.shields.io/badge/GitHub-PrisonerSim-blue)](https://github.com/Programmer-cyberika/PrisonerSim)

PrisonerSim is a Python project that simulates the Iterated Prisoner's Dilemma. The goal is to experiment with strategies and explore how different approaches perform over multiple rounds of the dilemma.

---

## Features

- Play the Iterated Prisoner's Dilemma with multiple strategies.
- Customizable payoff matrix through JSON files (default payoff matrix is included).
- Default values for the number of rounds and strategies simplify running simulations.
- Simulate tournaments for specified strategies over multiple rounds.
- View detailed outputs in the terminal, including round-wise results and final scores.

---

## Installation

To run this project, ensure you have Python installed along with the required libraries.

### Requirements

Install the required libraries using the following command:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains the following libraries:

- `argparse`
- `colorama`

---

## Usage

Run the script `executeTournament.py` using the following arguments:

### Arguments:

1. **`--payoff`**  
   Path to the JSON file specifying the payoff matrix.  
   Example JSON format:  
   ```json
   {
       "CC": [3, 3],
       "CD": [0, 5],
       "DC": [5, 0],
       "DD": [1, 1]
   }
   ```
   > **Note:** If no JSON file is provided, the default payoff matrix will be used:
   ```json
   {
       "CC": [3, 3],
       "CD": [0, 5],
       "DC": [5, 0],
       "DD": [1, 1]
   }
   ```

2. **`--rounds`**  
   Specify the number of rounds to play in the tournament.  
   > **Default:** 100 rounds.

3. **`--strategies`**  
   List of strategies to include in the tournament. Separate multiple strategies with spaces.  
   > **Default Strategies:** Every built-in strategy: `TitForTat`, `AlwaysCooperate`, `AlwaysDefect`, `RandomStrategy`, `DoubleD`, `GrimTrigger`, `Pavlov`, and `GenerousTitForTat`.

---

## Example Usage

1. Using all defaults:
   ```bash
   python "executeTournament.py"
   ```

2. Specifying custom values:
   ```bash
   python "executeTournament.py" --payoff path/to/payoff.json --rounds 200 --strategies TitForTat,AlwaysCooperate,RandomStrategy
   ```

---

## Adding or Editing Strategies

To add new strategies or modify existing ones, follow these steps:

1. **Locate the Strategy Classes**  
   All strategies are implemented as subclasses of the `Strategy` class in the project in `strategyClasses.py`.

2. **Create a New Strategy**  
   Define a new class that inherits from `Strategy`. Implement the methods as defined in other strategies.  
   Example:
   ```python
   class AlwaysCooperate(Strategy):
       def __init__(self):
           super().__init__()
           self.strategyName = "Always Cooperate"

       def reset(self):
           pass

       def cooperationReaction(self):
           return self.cooperate()

       def defectionReaction(self):
           return self.cooperate()

       def startingReaction(self):
           self.reset()
           return self.cooperate()
   ```

3. **Register the Strategy**  
   The project dynamically maps strategies using the `Strategy.__subclasses__()` method, so your new class will automatically be included in the available strategies.

4. **Test the Strategy**  
   Add your new strategy to the `--strategies` argument when running the script and verify its behavior during the tournament.

   Example:
   ```bash
   python "executeTournament.py" --strategies TitForTat AlwaysCooperate
   ```

---

## Acknowledgments

This project is inspired by the rich field of game theory and the work of brilliant minds who have contributed to it. Special acknowledgment to **Professor Robert Axelrod**, whose seminal work on the Iterated Prisoner's Dilemma and the Tit-for-Tat strategy has paved the way for exploring cooperative and competitive behaviors in decision-making.  

Additionally, a nod to other pioneers like **John Nash**, whose equilibrium theory underpins much of modern game theory, and **John von Neumann**, who co-founded the field of game theory itself. Their contributions have deeply influenced this project and the broader understanding of strategic interactions.

---

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please fork the repository, make your changes, and submit a pull request.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Repository

[PrisonerSim GitHub Repository](https://github.com/Programmer-cyberika/PrisonerSim)
