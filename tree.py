class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

    def vlr(self) -> list[int]:
        result = [self.val]
        if self.left is not None:
            result.extend(self.left.vlr())
        if self.right is not None:
            result.extend(self.right.vlr())
        return result

    def lvr(self) -> list[int]:
        result = []
        if self.left is not None:
            result.extend(self.left.lvr())
        result.append(self.val)
        if self.right is not None:
            result.extend(self.right.lvr())
        return result

    def lrv(self) -> list[int]:
        result = []
        if self.left is not None:
            result.extend(self.left.lrv())
        if self.right is not None:
            result.extend(self.right.lrv())
        result.append(self.val)
        return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    print(root.vlr())
    print(root.lvr())
    print(root.lrv())
