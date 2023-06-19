

class Node:

    def __init__(self, parrent, left, right, value):
        self.parrent = parrent
        self.left = left
        self.right = right
        self.value = value



def main():
    N, Q = input().split()
    N, Q = int(N), int(Q)
    list_nodes = (constructing_Tree(N))
    # for node in list_nodes: # Проверка работоспособности создания дерева
    #     print(node.value, end=' ')
    changes_list = list(map(int, input().split()))
    values_dict = {}
    for i in range(len(list_nodes)):
        values_dict[list_nodes[i].value] = list_nodes[i]
    for change in changes_list:
        swap_nodes(values_dict[change])
    # for change in changes_list:
    #     for node in list_nodes:
    #         if node.value == change:
    #             swap_nodes(node)
    # for node in list_nodes: # Проверка работоспособности перестановок
    #     if node.parrent != None:
    #         try:
    #             print(node.value, node.parrent.value, node.left.value, node.right.value)
    #         except:
    #             try:
    #                 print(node.value, node.parrent.value, node.left, node.right.value)
    #             except:
    #                 try:
    #                     print(node.value, node.parrent.value, node.left.value, node.right)
    #                 except:
    #                     print(node.value, node.parrent.value, node.left, node.right)
    #
    #    else:
    #        print(node.value)

    for node in list_nodes:
        if node.parrent == None:
            root = node
    # print(root.value, root.left, root.right.value ) # Проверка перестановки
    answer_list = []
    for node in answer(root, answer_list, N):
        print(node.value, end = ' ')

def constructing_Tree(N : int):
    list_nodes = []
    root = Node(None, None, None, 1)
    list_nodes.append(root)
    spawn_childs(root, N, list_nodes)
    return(list_nodes)

def spawn_childs(parrent : Node, N : int, list_nodes : list):
    if (parrent.value * 2) <= N: # Если
        leftChild = Node(parrent, None, None, parrent.value * 2)
        parrent.left = leftChild
        list_nodes.append(leftChild)
        spawn_childs(leftChild, N, list_nodes)

    if (parrent.value * 2 + 1) <= N:
        rightChild = Node(parrent, None, None, parrent.value * 2 + 1)
        parrent.right = rightChild
        list_nodes.append(rightChild)
        spawn_childs(rightChild, N, list_nodes)

    return(list_nodes)

def swap_nodes(node_to_swap : Node):
    if node_to_swap.parrent != None:
        parrent = node_to_swap.parrent

        if parrent.parrent != None:
            grandparrent = node_to_swap.parrent.parrent

            if grandparrent.left == parrent:
                grandparrent.left = node_to_swap

            if grandparrent.right == parrent:
                grandparrent.right = node_to_swap

        if node_to_swap == parrent.left:
            child = node_to_swap.left
            node_to_swap.left, parrent.left, parrent.parrent, node_to_swap.parrent = parrent, node_to_swap.left, node_to_swap, parrent.parrent

            if child != None:
                child.parrent = parrent

        if node_to_swap == parrent.right:
            child = node_to_swap.right
            node_to_swap.right, parrent.right, parrent.parrent, node_to_swap.parrent = parrent, node_to_swap.right, node_to_swap, parrent.parrent

            if child != None:
                child.parrent = parrent


def answer(root : Node, answer_list : list, N: int):
    if root:
        answer(root.left,answer_list, N)
        answer_list.append(root)
        answer(root.right,answer_list, N)
    return(answer_list)
    # if root.left != None:
    #     answer(root.left, answer_list, N)
    # else:
    #     if root not in answer_list:
    #         answer_list.append(root)
    # if root.left in answer_list and root not in answer_list:
    #     answer_list.append(root)
    # if root.right != None:
    #     answer(root.right, answer_list, N)
    # else:
    #     if root not in answer_list:
    #         answer_list.append(root)
    # if root.right in answer_list and root not in answer_list:
    #     answer_list.append(root)
    # return(answer_list)

if __name__ == '__main__':
    main()
