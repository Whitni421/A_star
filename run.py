from search_core import A_star_search
from eight_puzzle import h0, h1, h2


PUZZLE_INSTANCES = [
        (1, 2, 3, 4, 0, 5, 7, 8, 6), (1, 2, 3, 4, 5, 8, 7, 0, 6), (1, 2, 3, 0, 4, 6, 7, 5, 8), (1, 2, 0, 4, 5, 3, 7, 8, 6), (1, 2, 3, 4, 5, 6, 7, 8, 0),
        (1, 2, 3, 4, 8, 5, 7, 0, 6), (1, 2, 3, 4, 5, 6, 0, 7, 8), (1, 0, 3, 4, 2, 6, 7, 5, 8), (1, 2, 3, 4, 5, 6, 7, 8, 0), (1, 2, 3, 4, 5, 6, 7, 8, 0),

        (1, 4, 2, 7, 0, 5, 8, 3, 6), (4, 1, 3, 7, 2, 5, 8, 0, 6), (7, 4, 5, 6, 8, 2, 3, 1, 0), (7, 5, 4, 8, 6, 2, 1, 0, 3), (2, 5, 3, 6, 1, 4, 8, 7, 0),
        (2, 6, 5, 7, 4, 3, 1, 8, 0), (1, 3, 5, 2, 4, 0, 7, 8, 6), (5, 6, 3, 4, 0, 1, 7, 2, 8), (8, 6, 7, 2, 5, 4, 3, 0, 1), (3, 6, 8, 7, 4, 5, 0, 2, 1),

        (6, 1, 8, 4, 0, 2, 7, 3, 5), (8, 6, 7, 2, 5, 4, 3, 0, 1), (2, 6, 3, 5, 1, 4, 0, 7, 8), (5, 8, 3, 4, 1, 2, 7, 6, 0), (5, 6, 7, 4, 8, 0, 3, 2, 1),
        (7, 3, 5, 4, 2, 1, 6, 0, 8), (1, 6, 8, 4, 7, 0, 2, 5, 3), (8, 5, 3, 4, 2, 1, 7, 6, 0), (6, 5, 8, 2, 7, 4, 3, 1, 0), (8, 7, 6, 5, 4, 3, 2, 1, 0)
    ]


def main():
    heuristics = {
        "h0 (UCS)": h0,
        "h1 (Misplaced Tiles)": h1,
        "h2 (Manhattan Distance)": h2,
    }

    print("Running A* search with different heuristics on 30 puzzle instances...")

    for h_name, h_func in heuristics.items():
        print(f"\n--- Results for Heuristic: {h_name} ---")
        print("Instance | Solution Depth | Nodes Expanded | Max Frontier Size")
        print("------------------------------------------------------------------")

        for i, puzzle in enumerate(PUZZLE_INSTANCES):
            metrics, path = A_star_search(puzzle, h_func)

            if metrics:
                print(f"{i+1:8d} | {metrics['solution_depth']:14d} | {metrics['nodes_expanded']:14d} | {metrics['max_frontier_size']:17d}")
            else:
                print(f"{i+1:8d} | No solution found")



if __name__ == "__main__":
    main()
