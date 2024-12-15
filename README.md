# **PrisonerSim**  
A simulation of the **Prisoner's Dilemma** game inspired by Robert Axelrod's research, designed to explore and test strategies against classical approaches like **Tit-for-Tat**.

---

## **Overview**  
The Prisoner's Dilemma is a classic problem in **game theory** that explores cooperation and betrayal between two players. This project replicates the traditional game mechanics of the Prisoner's Dilemma, but with a **modified payoff matrix** designed to explore strategies against the classical **Tit-for-Tat**.

---

## **Features**  
- Simulates rounds of the **Prisoner's Dilemma** game.  
- Implements strategies, including **Tit-for-Tat**.  
- Allows for testing and exploration of custom strategies.  
- Results and comparisons are provided for analysis.

---

## **Modified Payoff Matrix**  
The game uses the following modified payoff matrix:

|             | **Player 2: C2** | **Player 2: D2** |
|-------------|------------------|------------------|
| **Player 1: C1** | 3, 3              | 0, 5              |
| **Player 1: D1** | 5, 0              | 1, 1              |

- **C1, C2**: Both players cooperate, earning 3 points each.
- **C1, D2**: Player 1 cooperates, Player 2 defects (Player 1 gets 0 points, Player 2 gets 5 points).
- **D1, C2**: Player 1 defects, Player 2 cooperates (Player 1 gets 5 points, Player 2 gets 0 points).
- **D1, D2**: Both players defect, earning 1 point each.

### Objective  
This simulation aims to test and explore strategies that can **outscore Tit-for-Tat** under this new payoff system. The goal is to identify strategies that have the potential to outperform Tit-for-Tat in real-world dilemmas, where cooperation and defection play a significant role.

---

## **Getting Started**  

### **1. Prerequisites**  
Make sure you have the following installed:  
- **Python 3.x**  

---

### **2. Repository Status**  
This project is in its early development phase. The core mechanics are being worked on, but feel free to explore and contribute ideas or improvements.

To get started, clone the repository:  
```bash
git clone https://github.com/Programmer-cyberika/PrisonerSim.git
cd PrisonerSim
```

---

## **Planned Strategies**  
- **Tit-for-Tat**  
- **Random Strategy**  
- **Always Cooperate**  
- **Always Defect**  
- Custom strategies for testing and optimization.

---

## **Goals**  
The primary goal of this project is to:  
1. Replicate the game environment.  
2. Explore and develop strategies that can **outperform Tit-for-Tat**.  
3. Analyze results to gain insights into game theory and strategy optimization.  
4. Implement and test various strategies, such as **Tit-for-Tat with forgiveness**, **Generous Tit-for-Tat**, **Grim Trigger**, and others.  
5. Analyze and compare the effectiveness of each strategy against Tit-for-Tat.

---

## **Contributions**  
Contributions are welcome! Feel free to open an **issue** or submit a **pull request** with new strategies or improvements. To contribute, fork the repository and create a pull request.

---

## **License**  
This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## **Acknowledgments**  
- Inspired by Robert Axelrod's research on the Prisoner's Dilemma.  
- Game theory concepts developed by John Nash and others.

---

## **Contact**  
For questions, ideas, or feedback, feel free to reach out via GitHub.
