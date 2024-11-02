# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #initializare nodul sursa de tipul (pozitie, [pasi efectuati])
    cale_nod_sursa = []
    pozitie_nod_sursa = problem.getStartState()
    nod_sursa = (pozitie_nod_sursa, cale_nod_sursa)

    #initializare lista noduri care au fost expandate
    expandate = []

    #BFS => marginea dintre nodurile expandate si cele nedescoperite este o coada
    bariera = util.Queue()
    bariera.push(nod_sursa)

    while bariera:
        nod_curent = bariera.pop()
        pozitie = nod_curent[0]
        cale_curenta = nod_curent[1]
        
        if problem.isGoalState(pozitie):
            return cale_curenta
        
        if pozitie not in expandate:  
            expandate.append(pozitie)
             
            succesori = problem.getSuccessors(pozitie)
            for succesor in succesori:
                cale_noua = cale_curenta[:]
                cale_noua.append(succesor[1])
                nod_nou = (succesor[0], cale_noua)
                bariera.push(nod_nou)
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    cale_nod_sursa = []
    pozitie_nod_sursa = problem.getStartState()
    #ucs => adaugam cost la nodul_sursa
    nod_sursa = (pozitie_nod_sursa, cale_nod_sursa, 0)

    expandate = []

    bariera = util.PriorityQueue()
    #priorityqueue cere ca al doilea argument sa fie prioritatea
    bariera.push(nod_sursa, 0)

    while bariera:
        nod_curent = bariera.pop()
        pozitie = nod_curent[0]
        cale_curenta = nod_curent[1]
        cost_curent = nod_curent[2]

        if problem.isGoalState(pozitie):
            return cale_curenta
        
        if pozitie not in expandate:  
            expandate.append(pozitie)

            succesori = problem.getSuccessors(pozitie)
            for succesor in succesori:
                cale_noua = cale_curenta[:]
                cale_noua.append(succesor[1])
                cost_nou = cost_curent + succesor[2]
                nod_nou = (succesor[0], cale_noua, cost_nou)
                #adaugam costul nou ca si prioritate
                bariera.push(nod_nou, cost_nou)
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
