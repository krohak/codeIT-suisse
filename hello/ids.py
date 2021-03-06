l={

"destination": "DhobyGhaut",
"stations": [{
        "name": "Punggol",
        "passengers": 80,
        "connections": [{
                "station": "Sengkang",
                "line": "purple"
            }
        ]

    }, {

        "name": "Sengkang",
        "passengers": 40,
        "connections": [{
                "station": "Punggol",
                "line": "purple"
            }, {
                "station": "Serangoon",
                "line": "purple"
            }
        ]

    }, {

        "name": "Serangoon",
        "passengers": 40,
        "connections": [{
                "station": "LittleIndia",
                "line": "purple"
            }, {
                "station": "Sengkang",
                "line": "purple"
            }, {
                "station": "PayaLebar",
                "line": "orange"
            }, {
                "station": "Bishan",
                "line": "orange"
            }
        ]
    }, {

        "name": "LittleIndia",
        "passengers": 40,
        "connections": [{
                "station": "Serangoon",
                "line": "purple"
            }, {
                "station": "DhobyGhaut",
                "line": "purple"
            },
        ]
    }, {

        "name": "DhobyGhaut",
        "passengers": 20,
        "connections": [{
                "station": "LittleIndia",
                "line": "purple"
            }, {
                "station": "HarbourFront",
                "line": "purple"
            }, {
                "station": "Somerset",
                "line": "red"
            }, {
                "station": "MarinaBay",
                "line": "red"
            }, {
                "station": "Esplanade",
                "line": "orange"
            }
        ]

    }, {

        "name": "HarbourFront",
        "passengers": 90,
        "connections": [{
                "station": "DhobyGhaut",
                "line": "purple"
            }
        ]

    }, {
        "name": "Somerset",
        "passengers": 0,
        "connections": [{
                "station": "DhobyGhaut",
                "line": "red"
            }, {
                "station": "Orchard",
                "line": "red"
            }
        ]

    }, {
        "name": "Orchard",
        "passengers": 30,
        "connections": [{
                "station": "Somerset",
                "line": "red"
            }, {
                "station": "Novena",
                "line": "red"
            }
        ]

    }, {
        "name": "Novena",
        "passengers": 10,
        "connections": [{
                "station": "Orchard",
                "line": "red"
            }, {
                "station": "Bishan",
                "line": "red"
            }
        ]

    }, {
        "name": "Bishan",
        "passengers": 20,
        "connections": [{
                "station": "Novena",
                "line": "red"
            }, {
                "station": "Woodlands",
                "line": "red"
            }, {
                "station": "Serangoon",
                "line": "orange"
            }
        ]

    }, {
        "name": "Woodlands",
        "passengers": 40,
        "connections": [{
                "station": "Bishan",
                "line": "red"
            }
        ]

    }, {
        "name": "MarinaBay",
        "passengers": 100,
        "connections": [{
                "station": "DhobyGhaut",
                "line": "red"
            }
        ]
    }, {
        "name": "Esplanade",
        "passengers": 0,
        "connections": [{
                "station": "DhobyGhaut",
                "line": "orange"
            }, {
                "station": "PayaLebar",
                "line": "orange"
            }
        ]
    }, {
        "name": "PayaLebar",
        "passengers": 75,
        "connections": [{
                "station": "Esplanade",
                "line": "orange"
            }, {
                "station": "Serangoon",
                "line": "orange"
            }
        ]
    }
]
}



nodes=[]
destination=[]
destination.append(l["destination"])


for node in l["stations"]:
              nodes.append(node)
print(nodes)






class Problem(object):

    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal.  Your subclass's constructor can add
        other arguments."""
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        raise NotImplementedError

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        raise NotImplementedError

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal or checks for state in self.goal if it is a
        list, as specified in the constructor. Override this method if
        checking against a single self.goal is not enough."""
        if isinstance(self.goal, list):
            return is_in(state, self.goal)
        else:
            return state == self.goal

    def path_cost(self, c, state1, action, state2):
        """Return the cost of a solution path that arrives at state2 from
        state1 via action, assuming cost c to get up to state1. If the problem
        is such that the path doesn't matter, this function will only look at
        state2.  If the path does matter, it will consider c and maybe state1
        and action. The default method costs 1 for every step in the path."""
        return c + 1

    def value(self, state):
        """For optimization problems, each state has a value.  Hill-climbing
        and related algorithms try to maximize this value."""
        raise NotImplementedError
# ______________________________________________________________________________


class Node:

    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state.  Also includes the action that got us to this state, and
    the total path_cost (also known as g) to reach the node.  Other functions
    may add an f and h value; see best_first_graph_search and astar_search for
    an explanation of how the f and h values are handled. You will not need to
    subclass this class."""

    def __init__(self, state, parent=None, action=None, path_cost=0):
        """Create a search tree Node, derived from a parent by an action."""
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

    def __repr__(self):
        return "<Node {}>".format(self.state)

    def __lt__(self, node):
        return self.state < node.state

    def expand(self, problem):
        """List the nodes reachable in one step from this node."""
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """[Figure 3.10]"""
        next = problem.result(self.state, action)
        return Node(next, self, action,
                    problem.path_cost(self.path_cost, self.state,
                                      action, next))

    def solution(self):
        """Return the sequence of actions to go from the root to this node."""
        return [node.action for node in self.path()[1:]]

    def path(self):
        """Return a list of nodes forming the path from the root to this node."""
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    # We want for a queue of nodes in breadth_first_search or
    # astar_search to have no duplicated states, so we treat nodes
    # with the same state as equal. [Problem: this may not be what you
    # want in other contexts.]

    def __eq__(self, other):
        return isinstance(other, Node) and self.state == other.state

    def __hash__(self):
        return hash(self.state)

# ______________________________________________________________________________







def depth_limited_search(problem, limit=50):
    """[Figure 3.17]"""
    def recursive_dls(node, problem, limit):
        if problem.goal_test(node.state):
            return node
        elif limit == 0:
            return 'cutoff'
        else:
            cutoff_occurred = False
            for child in node.expand(problem):
                result = recursive_dls(child, problem, limit - 1)
                if result == 'cutoff':
                    cutoff_occurred = True
                elif result is not None:
                    return result
            return 'cutoff' if cutoff_occurred else None

    # Body of depth_limited_search:
    return recursive_dls(Node(problem.initial), problem, limit)


def iterative_deepening_search(problem):
    for depth in range(sys.maxsize):
        result = depth_limited_search(problem, depth)
        if result != 'cutoff':
            return result
