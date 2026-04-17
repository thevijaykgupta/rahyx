from modules.routing.network import nodes, connections

def find_best_path(start, end, risk_score, path=[]):
    path = path + [start]

    if start == end:
        return path

    best_path = None
    best_score = -999

    for node in connections[start]:
        if node not in path:
            new_path = find_best_path(node, end, risk_score, path)
            if new_path:
                
                # 🔥 NEW LOGIC
                score = sum(nodes[n]["trust"] for n in new_path) - risk_score

                if score > best_score:
                    best_score = score
                    best_path = new_path

    return best_path