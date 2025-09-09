import heapq
import collections
import random

# The state is a tuple of 9 integers, with 0 representing the blank tile.
GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)

class Node:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost  # g(n)
        self.heuristic_cost = heuristic_cost  # h(n)
        self.total_cost = self.cost + self.heuristic_cost  # f(n)

    def __lt__(self, other):
        return self.total_cost < other.total_cost

def get_inversions(state):
    inversions = 0
    flat_list = [tile for tile in state if tile != 0]
    for i in range(len(flat_list)):
        for j in range(i + 1, len(flat_list)):
            if flat_list[i] > flat_list[j]:
                inversions += 1
    return inversions

def is_solvable(initial_state):
    inversions = get_inversions(initial_state)
    return inversions % 2 == 0

def generate_solvable_puzzles(num_puzzles, num_moves):
    puzzles = []
    while len(puzzles) < num_puzzles:
        current_state = list(GOAL_STATE)
        for _ in range(num_moves):
            blank_idx = current_state.index(0)
            row, col = blank_idx // 3, blank_idx % 3
            possible_moves = []
            if row > 0: possible_moves.append('UP')
            if row < 2: possible_moves.append('DOWN')
            if col > 0: possible_moves.append('LEFT')
            if col < 2: possible_moves.append('RIGHT')
            
            action = random.choice(possible_moves)
            new_state = list(current_state)
            
            if action == 'UP':
                new_blank_idx = blank_idx - 3
            elif action == 'DOWN':
                new_blank_idx = blank_idx + 3
            elif action == 'LEFT':
                new_blank_idx = blank_idx - 1
            elif action == 'RIGHT':
                new_blank_idx = blank_idx + 1
            
            new_state[blank_idx], new_state[new_blank_idx] = new_state[new_blank_idx], new_state[blank_idx]
            current_state = new_state

        initial_state = tuple(current_state)
        if is_solvable(initial_state) and initial_state != GOAL_STATE and initial_state not in puzzles:
            puzzles.append(initial_state)
    return puzzles


def Actions(state):
    blank_idx = state.index(0)
    row, col = blank_idx // 3, blank_idx % 3
    actions = []
    if row > 0: actions.append('UP')
    if row < 2: actions.append('DOWN')
    if col > 0: actions.append('LEFT')
    if col < 2: actions.append('RIGHT')
    return actions

def Transition(state, action):
    blank_idx = state.index(0)
    new_state = list(state)
    if action == 'UP':
        new_blank_idx = blank_idx - 3
    elif action == 'DOWN':
        new_blank_idx = blank_idx + 3
    elif action == 'LEFT':
        new_blank_idx = blank_idx - 1
    elif action == 'RIGHT':
        new_blank_idx = blank_idx + 1
    
    new_state[blank_idx], new_state[new_blank_idx] = new_state[new_blank_idx], new_state[blank_idx]
    return tuple(new_state)

def GoalTest(state):
    return state == GOAL_STATE

def StepCost(state, action, next_state):
    return 1


def h0(state):
    #The heuristic is always 0
    return 0

def h1(state):
    #misplaced tiles
    misplaced_count = 0
    for i in range(9):
        if state[i] != GOAL_STATE[i] and state[i] != 0:
            misplaced_count += 1
    return misplaced_count

def h2(state):
#Manhattan distance
    distance = 0
    for i in range(9):
        tile = state[i]
        if tile != 0:
            current_row, current_col = i // 3, i % 3
            goal_idx = GOAL_STATE.index(tile)
            goal_row, goal_col = goal_idx // 3, goal_idx % 3
            distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance


