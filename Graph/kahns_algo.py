def kahns_algo(self, graph):
        # Find number of incoming edges for each vertex
        in_degree = {}
        for x, neighbors in graph.items():
            in_degree.setdefault(x, 0)
            for n in neighbors:
                in_degree[n] = in_degree.get(n, 0) + 1

        # Iterate over edges to find vertices with no incoming edges
        empty = {v for v, count in in_degree.items() if count == 0}

        result = []
        while empty:
            # Take random vertex from empty set
            v = empty.pop()
            result.append(v)

            # Remove edges originating from it, if vertex not present
            # in adjacency list use empty list as neighbors
            for neighbor in graph.get(v, []):
                in_degree[neighbor] -= 1

                # If neighbor has no more incoming edges add it to empty set
                if in_degree[neighbor] == 0:
                    empty.add(neighbor)

        if len(result) != len(in_degree):
            return None # Not DAG
        else:
            return result