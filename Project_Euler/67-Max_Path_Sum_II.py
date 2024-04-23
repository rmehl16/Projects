
class Node:
    def __init__(self, value, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left
        self.max_path_sum = None
    
    def printNode(self):
        print(f"Value: {self.value}, left: {self.left}, right: {self.right}")

    def getMaxPathSum(self):
        if self.max_path_sum is not None:
            return self.max_path_sum

        l_sum = 0
        r_sum= 0
        if self.left is not None:
            l_sum = self.left.getMaxPathSum()
        if self.right is not None:
            r_sum = self.right.getMaxPathSum()
        self.max_path_sum = max(l_sum, r_sum) + self.value
        return self.max_path_sum


if __name__ == '__main__':
    # print('hi')
    # x = Node(5)
    # y = Node(1)
    # z = Node(10, x, y)
    # z.printNode()
    # print(z.getMaxPathSum())

    arr = []
    with open("input/0067_triangle.txt") as graph_file:
        for line in graph_file:
            # print(line.strip().split(' '))
            values = line.strip().split(' ')
            nodes = []
            for val in values:
                nodes.append(Node(int(val)))
            arr.append(nodes)
    
    # Create edges using index of nodes in the array
    for i in range(len(arr)-1):
        for j in range(len(arr[i])):
            n = arr[i][j]
            n.left = arr[i+1][j]
            n.right = arr[i+1][j+1]

    head =  arr[0][0]
    res = head.getMaxPathSum()
    print(res)

    # for i in range(3):
    #     for x in arr[i]:
    #         x.printNode()
