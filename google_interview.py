import operator
import functools
import pprint
import json


def product_array(numbers, division=True):
    '''
    Given an array of integers, return a new array such that each element at index i 
    of the new array is the product of all the numbers in the original array except the one at i.
    For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
    If our input was [3, 2, 1], the expected output would be [2, 3, 6].

    Follow-up: what if you can't use division?
    '''
    result = [-1 for i in numbers]
    product = functools.reduce(operator.mul, numbers, 1)

    for i in range(len(numbers)):
        n = numbers[i]
        if division:
            result[i] = product//n
        else:
            result[i] = divide(product, n)
    return result


def divide(a, b):
    count = 0
    while a > 0:
        a -= b
        count += 1
    return count


class Node:
    '''
    This problem was asked by Google.

    Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

    For example, given the following Node class

    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    The following test should pass:

    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
    '''

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    return json.dumps(_serialize(root))


def _serialize(root):
    if root == None:
        return None
    return dict({'Node': {'val': root.val, 'left': _serialize(root.left), 'rigth': _serialize(root.right)}})


def deserialize(tree_str):
    json_tree = json.loads(tree_str)

    return deserialize_dict(json_tree)


def deserialize_dict(json_tree):

    if json_tree is None:
        return None

    json_node = json_tree.get('Node')

    if json_node is None:
        return None
    # print(json_node)
    return Node(json_node['val'], deserialize_dict(json_node['left']), deserialize_dict(json_node['rigth']))


def test_node():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(fn_pair):
    return fn_pair(lambda x,_: x)

def cdr(fn_pair):
    return fn_pair(lambda _,y: y)

def how_many_decoding(decoded_string):
    last_seen = decoded_string[0]
    result = 1
    for i in range(1, len(decoded_string)):
        current = decoded_string[i]

        if 0<= int(last_seen + current) <= 26:
            result += 1
        last_seen = current
    return result

print(how_many_decoding("2721"))