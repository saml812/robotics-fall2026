"""Mission 1 starter, created in student_submission/mission_1/planners.py.

Open that submission file in your editor and implement the four functions.
The guide creates it automatically and never overwrites an existing file.

Each function receives ctx with start, goal, grid, heuristic(cell) and
expand(cell, frontier_size). Return a list of (row, column) cells including
start and goal, or [] after exhausting the search. Call ctx.expand once per
expanded node. Record the actual frontier size, not the number of visited cells.
The runner enforces an expansion budget and a separate process time limit.
Use only the Python standard library. Do not import planning.reference_path.
When a free start is already the goal, return the single starting cell with
zero moves. No expansion is required for that case. Use the six small checks
on the Mission 1 page before running the full canonical-map evaluation.
"""
from collections import deque
from heapq import heappush, heappop
from planning.core import reconstruct, free


def bfs(ctx):
    """FIFO queue. Mark discovered cells when enqueuing and store parents.
    Use ctx.expand(current, len(frontier)+1) to obtain neighbours.
    BFS minimizes number of unit-cost edges, not execution time on a robot.
    """
    # raise NotImplementedError('Implement BFS with a deque and parent dictionary')
    # edge case: an endpoint is a wall or off the grid, so no route exists
    if not free(ctx.grid, ctx.start) or not free(ctx.grid, ctx.goal):
        return []
    # edge case: start is already the goal
    if ctx.start == ctx.goal:
        return [ctx.start]

    queue = deque([ctx.start])
    parent = {ctx.start: None}

    while len(queue) != 0:
        current = queue.popleft()

        for nxt in ctx.expand(current, len(queue) + 1):
            # check if cell is already discovered 
            if nxt in parent:
                continue
            # mark nxt as discovered and remember how we got there
            parent[nxt] = current

            # check if nxt is goal
            if nxt == ctx.goal:
                return reconstruct(parent, ctx.goal)

            # add nxt to the queue
            queue.append(nxt)

    # return empty queue if cannot reach goal
    return []


def dfs(ctx):
    """LIFO stack. Track discovered cells and parents to avoid cycles.
    A valid DFS path need not be shortest. Keep the supplied neighbour order.
    """
    # raise NotImplementedError('Implement DFS with a stack')
    # edge case: an endpoint is a wall or off the grid, so no route exists
    if not free(ctx.grid, ctx.start) or not free(ctx.grid, ctx.goal):
        return []
    if ctx.start == ctx.goal:
        return [ctx.start]

    stack = [ctx.start]
    parent = {ctx.start: None}

    while len(stack) != 0:
        current = stack.pop()

        # reverse so the first neighbour (right) is added to the top of the
        # stack and is explored first
        for nxt in reversed(ctx.expand(current, len(stack) + 1)):
            # check if cell is already discovered
            if nxt in parent:
                continue
            # mark nxt as discovered and remember how we got there
            parent[nxt] = current

            # check if nxt is goal
            if nxt == ctx.goal:
                return reconstruct(parent, ctx.goal)

            # add nxt to the stack
            stack.append(nxt)

    return []


def iddfs(ctx):
    """Run depth-limited DFS with bounds 0, 1, 2, ... .
    Prevent cycles on the current path. Do not keep a global visited set across
    depth limits. Count expansions again on every iteration. Return [] only
    after exhaustive failure. Catch no budget exceptions. The runner records
    resource_limit honestly if this expensive method reaches its budget.
    """
    # raise NotImplementedError('Implement iterative deepening with depth-limited DFS')
    # edge case: an endpoint is a wall or off the grid, so no route exists
    if not free(ctx.grid, ctx.start) or not free(ctx.grid, ctx.goal):
        return []
    # edge case: start is already the goal, no expansion needed
    if ctx.start == ctx.goal:
        return [ctx.start]

    depth_limit = 0
    while True:
        stack = [(ctx.start, [ctx.start], depth_limit)]
        cutoff = False 

        while len(stack) != 0:
            current, path, moves_left = stack.pop()

            # goal is checked when a cell is removed from the stack
            if current == ctx.goal:
                return path

            # expansion is counted again on every depth limit
            # skip cells already on the current path
            successors = []
            for nxt in ctx.expand(current, len(stack) + 1):
                if nxt not in path:
                  successors.append(nxt)
            if moves_left > 0:
                for nxt in reversed(successors):
                    stack.append((nxt, path + [nxt], moves_left - 1))
            elif successors:
                cutoff = True

        if not cutoff:
            return []

        depth_limit += 1


def astar(ctx):
    """Use a heap ordered by g + ctx.heuristic(cell).
    Keep best g costs and parents. Ignore outdated heap entries. Each edge
    costs 1. Stop when the goal is removed from the priority queue.
    """
    # raise NotImplementedError('Implement A* with Manhattan distance')
    # edge case: an endpoint is a wall or off the grid, so no route exists
    if not free(ctx.grid, ctx.start) or not free(ctx.grid, ctx.goal):
        return []
    # edge case: start is already the goal
    if ctx.start == ctx.goal:
        return [ctx.start]

    heap = []
    best_g = {ctx.start: 0}      # cheapest known cost from start to each cell
    parent = {ctx.start: None}
    closed = set()               # cells already expanded
    waiting = {ctx.start}        # distinct cells with a live heap entry

    # heap entries are (priority f = g + h, g, cell)
    heappush(heap, (ctx.heuristic(ctx.start), 0, ctx.start))

    while len(heap) != 0:
        f, g, current = heappop(heap)

        # ignore old entries
        # or the cell has already been expanded
        if current in closed or g != best_g[current]:
            continue
        waiting.discard(current)

        # stop when the goal is removed from the priority queue
        if current == ctx.goal:
            return reconstruct(parent, ctx.goal)

        closed.add(current)

        # frontier size counts distinct waiting cells plus the current cell removed
        for nxt in ctx.expand(current, len(waiting) + 1):
            new_g = g + 1  # each edge costs 1
            # only keep this route if it is cheaper than any known route
            if nxt not in best_g or new_g < best_g[nxt]:
                best_g[nxt] = new_g
                parent[nxt] = current
                heappush(heap, (new_g + ctx.heuristic(nxt), new_g, nxt))
                waiting.add(nxt)

    return []
