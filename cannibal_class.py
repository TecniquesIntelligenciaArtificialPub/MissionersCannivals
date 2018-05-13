import search

class MissionareCannibalProblem(search.Problem):

    """Cannibal problem
    """
    possible_actions = [[0,1], [1,0], [2,0], [1,1], [0,2]]

    def __init__(self):
        self.initial = (3,3,-1)
        search.Problem.__init__(self, self.initial, (0,0,1))

    def actions(self, state):
        """returns people in the boat"""
        return [action for action in self.possible_actions if self.legal(state, action)]

    def result(self, state, action):
        """people travel"""
        new_state = [state[i] + action[i] * state[2] for i in range(2)]
        new_state.append(state[2] * -1)

        return tuple(new_state)

    def legal(self, state, action):
        new_state = self.result(state,action)
        return (new_state[0] == 0 or new_state[0] == 3 or new_state[0] == new_state[1]) and (all(p in range(4) for p in new_state[:2]))

    def h(self, node):
        """number of trips"""

        return (node.state[0]+node.state[1])/2


sol = search.depth_first_graph_search(MissionareCannibalProblem())
print('DFS: ', sol.solution())
print('Final state (DFS): ', sol)
print('')


sol = search.breadth_first_graph_search(MissionareCannibalProblem())
print('BFS: ', sol.solution())
print('Final state (BFS): ', sol)



sol = search.astar_search(MissionareCannibalProblem())
print('A*: ', sol.solution())

search.compare_searchers([MissionareCannibalProblem()], "Cannibal",
                         [search.depth_first_graph_search, search.breadth_first_graph_search,
                          search.iterative_deepening_search, search.astar_search])

