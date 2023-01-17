import sys

class SimpleGraphNode:
    def __init__(self, val):
        self.val = val
        self.nodes = []
        self.max_path_sum = None

def printGraph(node):
    if node is None:
        print('Null')

    res = []

    visited = {}
    visited[node] = True

    q = [node]
    while len(q) > 0:
        cur = q[0]
        res.append((cur.val, cur.max_path_sum))
        
        if len(q) > 1:
            q = q[1:]
        else:
            q = []
        
        for child in cur.nodes:
            if not visited.get(child, False):
                q.append(child)
                visited[child] = True

    i = 1
    lines = 0
    s = ''
    for pair in res:
        s += '(' + str(pair[0]) + ',' + str(pair[1]) + ')  '
        lines += 1
        if i == lines:
            print(s + '\n')
            i += 1
            lines = 0
            s = ''


def getMaxPathSum(node):
    if node.max_path_sum is not None:
        return node.max_path_sum + node.val
    
    if len(node.nodes) == 0:
        node.max_path_sum = 0
        return node.val

    child_sums = []
    for child in node.nodes:
        child_sums.append(getMaxPathSum(child))

    node.max_path_sum = max(child_sums)

    #print(node.val, node.max_path_sum)
    return node.max_path_sum + node.val

if __name__ == '__main__':
    pyramid_root = None
    with open('18-Maximum-path-sum-pyramid.txt', 'r') as file:
        lines = file.readlines()
        prev_line = None
        for line in lines:
            #pyramid.append(tuple([int(x) for x in line.strip().split(' ')]))
            #max_path_sums.append([None for x in line.strip().split(' ')])
            nums = [SimpleGraphNode(int(x)) for x in line.strip().split(' ')]
            if prev_line is None:
                pyramid_root = nums[0]
            else:
                for i in range(len(prev_line)):
                    prev_line[i].nodes.append(nums[i])
                    prev_line[i].nodes.append(nums[i+1])

            prev_line = nums

    print(getMaxPathSum(pyramid_root))
    printGraph(pyramid_root)




'''
Use python 18-Maximum-path-sum-pyramid.txt to change input
'''