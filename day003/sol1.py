class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    list_output = [node.val]

    if node.left is not None:
        list_output.append(serialize(node.left))
    else:
        list_output.append([])

    if node.right is not None:
        list_output.append(serialize(node.right))
    else:
        list_output.append([])

    return list_output

def deserialize(serialized):
    if len(serialized[1])==0:
        left_node = None
    else:
        left_node = deserialize(serialized[1])

    if len(serialized[2])==0:
        right_node = None
    else:
        right_node = deserialize(serialized[2])
    return Node(serialized[0],
                    left=left_node,
                    right=right_node)

if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'