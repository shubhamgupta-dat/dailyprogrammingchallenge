import random
from operator import xor

dict_pointer = {}

def get_pointer():
    """
    Get pointer from random
    :return:
    """
    random_memory = random.randrange(2,1000)
    while random_memory in dict_pointer.keys():
        random_memory = random.randrange(2, 1000)
    return random_memory

def dereference_pointer(key):
    """
    Dereferences pointer if a value is removed from XORDLL
    :return:
    """
    dict_pointer.pop(key)
    pass

class Node():

    def __init__(self,node_value,node_address):
        self.next_address:int = node_address
        self.node_value:int = node_value

    def __str__(self):
        return f"Node value: {self.node_value} and address : {self.next_address}"


class XORDLL():

    def __init__(self,value,address = None):
        if address is None:
            self.start_address:int = get_pointer()
        else:
            self.start_address:int = address
        self.previous_address = 0
        self.start_node:Node = Node(value,-1)
        dict_pointer[self.start_address] = self.start_node
        self.current_node:Node = self.start_node
        self.movement_pointer:int = self.start_address
        self.movement_previous = 0
        self.end_address = self.start_address

    def add(self,value,address = None):
        """
        Add new node to the point
        :param value: int
        :param address: int
        :return:
        """
        if address is None:
            new_address = hash(get_pointer())
        else:
            new_address = hash(address)
        self.current_node.next_address = xor(self.previous_address,
                                             new_address
                                             )
        self.current_node = Node(value,-1)
        dict_pointer[new_address] = self.current_node
        self.previous_address = self.end_address
        self.end_address = new_address

    def get_next(self):
        """
        Get next Node from a particular address
        :return:
        """
        if self.movement_pointer == self.end_address:
            #print("Returning last value, Cannot Go Forward")
            return dict_pointer.get(self.movement_pointer)
        next_node:Node = dict_pointer.get(self.movement_pointer)
        temp_pointer = self.movement_pointer
        self.movement_pointer = xor(self.movement_previous,next_node.next_address)
        self.movement_previous = temp_pointer
        return next_node

    def get_previous(self):
        if self.previous_address == self.start_address:
            print("Returning first value, Cannot Go Backward")
            return dict_pointer.get(self.previous_address)
        previous_node:Node = dict_pointer.get(self.previous_address)
        temp_pointer = self.movement_previous
        self.movement_previous = xor(self.movement_pointer,previous_node.next_address)
        self.movement_pointer = temp_pointer
        return previous_node

    def show_nodes(self):
        self.movement_pointer= self.start_address
        self.movement_previous = 0
        current_node:Node = self.get_next()
        i = 0
        while current_node.next_address != -1:
            print("Current Node Value", current_node.node_value)
            current_node: Node = self.get_next()
        print("Current Node Value", current_node.node_value)
        print("Returned last value, Cannot Go Forward")


    def get(self,index):
        self.movement_pointer = self.start_address
        self.movement_previous = 0
        out_of_bound_flag = False
        for i in range(0,index+1):
            if out_of_bound_flag:
                raise Exception("Index Bound Exception")
            current_node:Node = self.get_next()
            if current_node.next_address == -1:
                out_of_bound_flag = True
        return current_node

#
if __name__ == '__main__':
    xor_dll:XORDLL = XORDLL(1,2)
    xor_dll.add(3,4)
    xor_dll.add(5,7)
    xor_dll.show_nodes()
    print("Get the value for index 1: {}".format(xor_dll.get(1)))
    print(xor_dll.get(2))