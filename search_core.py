import heapq
from eight_puzzle import Node, Actions, Transition, GoalTest, StepCost

def A_star_search(initial_state, heuristic):
    # Priority queue for the frontier, stores tuples of (f(n), node)
    start_node = Node(initial_state, heuristic_cost=heuristic(initial_state))
    frontier = [(start_node.total_cost, start_node)]
    heapq.heapify(frontier)

    # Map of state -> best known g(n)
    best_cost_by_state = {initial_state: 0}

    nodes_expanded = 0
    nodes_generated = 1
    max_frontier_size = 1

    while frontier:
        if len(frontier) > max_frontier_size:
            max_frontier_size = len(frontier)

        _, current_node = heapq.heappop(frontier)

        if GoalTest(current_node.state):
            goal_node = current_node
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            path.reverse()

            metrics = {
                'nodes_expanded': nodes_expanded,
                'nodes_generated': nodes_generated,
                'max_frontier_size': max_frontier_size,
                'solution_depth': len(path) - 1,
                'solution_cost': goal_node.cost,
            }
            return metrics, path

        nodes_expanded += 1

        # Generate children of the current node
        for action in Actions(current_node.state):
            next_state = Transition(current_node.state, action)
            new_cost = current_node.cost + StepCost(current_node.state, action, next_state)

            # Skip if we've already found an equal or cheaper path to this state
            if next_state in best_cost_by_state and best_cost_by_state[next_state] <= new_cost:
                continue

            nodes_generated += 1

            # Create a new node and add to frontier
            new_node = Node(
                state=next_state,
                parent=current_node,
                action=action,
                cost=new_cost,
                heuristic_cost=heuristic(next_state)
            )
            heapq.heappush(frontier, (new_node.total_cost, new_node))
            best_cost_by_state[next_state] = new_cost

    return None, None  # No solution found