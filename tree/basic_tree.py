class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    def __str__(self, level = 0):
        result = "  " * level + str(self.data) + "\n"
        for child in self.children:
            result += child.__str__(level + 1)
        return result
    
    def addChild(self, tree_node):
        self.children.append(tree_node)

tree = TreeNode("Drinks", [])
hot = TreeNode("Hot", [])
cold = TreeNode("Cold", [])
tree.addChild(cold)
tree.addChild(hot)

tea = TreeNode("Tea", [])
coffee = TreeNode("Coffee", [])
cola = TreeNode("Cola", [])
fanta = TreeNode("Fanta", [])
hot.addChild(tea)
hot.addChild(coffee)
cold.addChild(cola)
cold.addChild(fanta)

print(tree)
