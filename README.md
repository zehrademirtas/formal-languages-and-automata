# formal-languages-and-automata
Implementation of DFA minimization using Hopcroft's algorithm. The project visualizes and optimizes deterministic finite automata (DFA) for efficiency.
# **Formal Languages and Automata - DFA Minimization**

## **Project Overview**
This project focuses on **minimizing Deterministic Finite Automata (DFA)** using **Hopcroft's Algorithm**. The system takes user-defined DFA components and reduces the number of states while maintaining the same functionality. Additionally, the project provides **visualization** of the original and minimized DFA and generates its corresponding formal grammar.

## **Technologies Used**
- **Python** (for DFA processing)
- **Graph Algorithms**: Hopcroft’s Algorithm for DFA minimization
- **Data Structures**: defaultdict for transition management
- **Visualization**: Graphviz (to generate DFA diagrams)

## **How It Works**
1. **User Input**: The user provides DFA components, including states, alphabet, transitions, start state, and accept states.
2. **Initial DFA Construction**: The system generates and visualizes the given DFA.
3. **DFA Minimization**: Hopcroft’s Algorithm is applied to merge equivalent states.
4. **Grammar Generation**: The minimized DFA’s transitions are converted into a formal grammar representation.
5. **Visualization Output**: The minimized DFA is displayed as a `.png` image.

## **Installation & Setup**
### **Requirements**
Ensure you have Python installed along with the necessary dependencies. You can install them using:
```bash
pip install -r requirements.txt

### **Running the Project** 
To execute the project, run:

```bash
python dfa_minimization.py
This will generate the minimized DFA visualization and formal grammar representation.

## **Project Outputs**
- **Original DFA Visualization**:Displays the user-defined DFA structure.
- **Minimized DFA Representation**: Shows the optimized DFA after applying Hopcroft's Algorithm.
- **State Transition Table:**:  Lists the new minimized transitions.
- **Generated Formal Grammar**: Displays the grammar corresponding to the minimized DFA.
