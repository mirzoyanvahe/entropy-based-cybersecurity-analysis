import networkx as nx
from load_data import load_logs
from transitions import build_event_timeline, extract_transitions

def build_graph(transitions):
    G = nx.DiGraph()
    for (src, dst), weight in transitions.items():
        G.add_edge(src, dst, weight=weight)
    return G


if __name__ == "__main__":
    logon, device, http = load_logs()

    #use the SAME rich user
    test_user = "DTAA/FDP0500"

    timeline = build_event_timeline(logon, device, http, test_user)
    transitions = extract_transitions(timeline)

    G = build_graph(transitions)

    print("Nodes:", list(G.nodes()))
    print("Edges with weights:")
    for u, v, d in G.edges(data=True):
        print(f"{u} -> {v} {d}")