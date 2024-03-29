

def binary_tree_right_side_view(root):
    rightmost_value_at_depth = dict()  # depth -> node.val
    max_depth = -1

    stack = [(root, 0)]
    while stack:
        node, depth = stack.pop()

        if node is not None:
            # maintain knowledge of the number of levels in the tree.
            max_depth = max(max_depth, depth)

            # only insert into dict if depth is not already present.
            rightmost_value_at_depth.setdefault(depth, node.val)

            stack.append((node.left, depth + 1))
            stack.append((node.right, depth + 1))

    return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]

