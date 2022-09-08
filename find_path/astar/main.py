W = 9999  # wall

# step direction and length in each move
movements = ((1, 0), (0, 1), (-1, 0), (0, -1))


class Node:
    def __init__(self, parent, pos, cost):
        self.parent = parent
        self.pos = pos
        self._cost = cost
        self._f = 0
        self._g = 0

    def __eq__(self, other):
        return self.parent == other.parent and self.pos == other.pos and self.cost == other.cost

    @property
    def cost(self):
        return self._cost

    @property
    def g(self) -> int:
        return self._g

    def h(self, end: tuple[int, int]) -> int:
        return abs(self.pos[0] - end[0]) + abs(self.pos[1] - end[1])

    @property
    def f(self) -> int:
        return self._f

    def calculate_f(self, parent_node, end: tuple[int, int]):
        """
        to calculate new cost(g and f) after moving from parent node;
        must be cumulated, or it will underestimate cost and direct to wrong path
        :param parent_node: parent node
        :param end: END node position
        :return:
        """
        self._g = self._cost + parent_node.g
        self._f = self.g + self.h(end)  # F(x) = G(x) + H(x)


def astar(graph: tuple[tuple[int, ...], ...], start: tuple[int, int], end: tuple[int, int]):
    """
    :param graph: [[1,2,3], [4,5,6], [7,8,9]], max_height: len(graph), max_width: len(graph[0]),
     each element represents the cost
    :param start: (h, w)
    :param end: (h, w)
    :return: path from start to end
    """
    height = len(graph)
    width = len(graph[0])

    open_list = []
    close_set: set[tuple[int, int]] = set()

    start_node = Node(None, start, graph[start[0]][start[1]])
    open_list.append(start_node)

    while len(open_list) > 0:
        current_idx = 0
        current_node = open_list[current_idx]

        # if we shuffle open_list,
        # it will be able to find out another way (if exists) to the end with the same total cost.
        for idx, node in enumerate(open_list):
            # to choose the lowest cumulated cost node for next try
            if node.f < current_node.f:
                current_idx = idx
                current_node = node

        open_list.pop(current_idx)
        close_set.add(current_node.pos)

        if current_node.pos == end:
            path = []
            scan = current_node
            while scan is not None:
                path.append(scan.pos)
                scan = scan.parent
            return path[::-1]

        next_available_step = []
        for move in movements:
            # check if node in next step is valid
            new_pos = (current_node.pos[0] + move[0], current_node.pos[1] + move[1])
            if new_pos[0] < 0 or new_pos[0] >= height:
                continue
            if new_pos[1] < 0 or new_pos[1] >= width:
                continue
            new_cost = graph[new_pos[0]][new_pos[1]]
            if new_cost == W:  # wall, can not pass through
                continue
            next_available_step.append(Node(current_node, new_pos, new_cost))

        for next_step in next_available_step:
            if next_step.pos in close_set:  # already in close set
                continue

            # calculate F(x) = G(x) + H(x)
            # calculate before comparing to node in open_list
            next_step.calculate_f(current_node, end)

            for open_node in open_list:
                if next_step.pos == open_node.pos and next_step.g > open_node.g:  # already in open list
                    continue
            open_list.append(next_step)
    else:
        return None
    # end


def build_graph() -> tuple[tuple[int, ...], ...]:
    """
    :return: 2-d graph, each value represents the cost to move to that node
    """
    return (
        (0, 5, 6, 25, W, 25, 20, 15, W),  # 1
        (15, 6, W, 10, 25, 10, 15, 6, 20),  # 2
        (20, 5, 6, 20, 15, 15, 6, 5, 15),  # 3
        (15, 20, 25, 6, 15, 10, 20, 15, 25),  # 4
        (15, 10, 5, 25, W, 25, 10, W, 15),  # 5
        (20, 15, 10, 15, 5, 15, 15, 20, 15),  # 6
        (15, 25, 6, 15, 15, 15, 6, 25, 20),  # 7
        (15, 15, 10, W, 25, 15, 15, 15, 15),  # 8
        (25, 20, 5, 15, 15, 10, 5, 25, 20),  # 9
        (20, 15, 15, 6, 25, 5, 15, 20, 15),  # 10
        (15, 5, 20, 15, 15, 6, 15, 5, 15),  # 11
        (15, 20, 15, 6, 6, 15, 25, 15, 20),  # 12
        (15, 20, W, W, 0, W, W, 25, 15),  # 13
    )


def print_graph(graph):
    print('\n'.join(
        [''.join([f'{i:<4}' for i in row]) for row in graph]
    ))


def convert_graph(graph: tuple[tuple[any, ...], ...], start, end, path=None):
    def convert(i, h, w):
        if (h, w) == start:
            return 'S'  # start
        if (h, w) == end:
            return 'E'  # end
        if i == W:
            return 'W'  # wall
        if path is not None and (h, w) in path:
            return '*'  # result path
        return str(i)

    return ((f'{convert(i, h, w):<4}' for w, i in enumerate(row)) for h, row in enumerate(graph))


if __name__ == '__main__':
    graph = build_graph()
    start = (12, 4)
    end = (0, 0)
    paths = astar(graph, start, end)
    print(paths)

    print('original:')
    print_graph(convert_graph(graph, start, end))

    print('result:')
    m = convert_graph(graph, start, end, paths)
    print_graph(m)
