
import math

# Alpha-Beta Pruning Functions
def alpha_beta_search(state):
    """ Alpha-Beta Search to get the optimal action """
    value = max_value(state, -math.inf, math.inf)
    print("Optimal Value:", value)
    return value

def max_value(state, alpha, beta):
    """ Function to calculate the MAX value node """
    if terminal_test(state):  # If leaf node, return utility value
        return utility(state)
    v = -math.inf
    for child in state["children"]:  # Iterate through child nodes
        v = max(v, min_value(child, alpha, beta))
        if v >= beta:
            return v  # Beta cutoff
        alpha = max(alpha, v)
    return v

def min_value(state, alpha, beta):
    """ Function to calculate the MIN value node """
    if terminal_test(state):  # If leaf node, return utility value
        return utility(state)
    v = math.inf
    for child in state["children"]:  # Iterate through child nodes
        v = min(v, max_value(child, alpha, beta))
        if v <= alpha:
            return v  # Alpha cutoff
        beta = min(beta, v)
    return v

# Utility Functions
def terminal_test(state):
    """ Check if the node is a leaf node """
    return "value" in state  # Leaf node if it contains 'value'

def utility(state):
    """ Return the utility value of a leaf node """
    return state["value"]

# Build the Binary Tree Based on Leaf Nodes
def build_tree(values):
    """ Recursively build a binary tree from a list of leaf node values """
    if len(values) == 1:  # Single value -> Leaf node
        return {"value": values[0]}
    mid = len(values) // 2
    left_subtree = build_tree(values[:mid])
    right_subtree = build_tree(values[mid:])
    return {"children": [left_subtree, right_subtree]}

# Main Program
if __name__ == "__main__":
    leaf_nodes = [10, 9, 14, 18, 5, 4, 50, 3]
    tree = build_tree(leaf_nodes)  # Build the binary tree
    print("Alpha-Beta Pruning Search:")
    alpha_beta_search(tree)
