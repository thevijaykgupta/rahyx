nodes = {
    "A": {"trust": 0.9},
    "B": {"trust": 0.6},
    "C": {"trust": 0.8},
    "D": {"trust": 0.4},
    "E": {"trust": 0.95}
}

connections = {
    "A": ["B", "C"],
    "B": ["D"],
    "C": ["D", "E"],
    "D": ["E"],
    "E": []
}