def normalize_transitions(transitions):
    probs = {}
    outgoing = {}

    # sum outgoing transitions per state
    for (src, dst), count in transitions.items():
        outgoing[src] = outgoing.get(src, 0) + count

    # normalize
    for (src, dst), count in transitions.items():
        probs[(src, dst)] = count / outgoing[src]

    return probs

def stationary_distribution(probs, tol=1e-8, max_iter=1000):
    states = sorted({src for src, _ in probs.keys()})
    index = {state: i for i, state in enumerate(states)}
    n = len(states)

    # build transition matrix
    P = [[0.0] * n for _ in range(n)]
    for (src, dst), p in probs.items():
        P[index[src]][index[dst]] = p

    # initial uniform distribution
    pi = [1.0 / n] * n

    for _ in range(max_iter):
        new_pi = [0.0] * n
        for i in range(n):
            for j in range(n):
                new_pi[j] += pi[i] * P[i][j]

        if max(abs(new_pi[i] - pi[i]) for i in range(n)) < tol:
            break
        pi = new_pi

    return {states[i]: pi[i] for i in range(n)}


#test
if __name__ == "__main__":
    from load_data import load_logs
    from transitions import build_event_timeline, extract_transitions

    logon, device, http = load_logs()
    user = "DTAA/FDP0500"

    timeline = build_event_timeline(logon, device, http, user)
    transitions = extract_transitions(timeline)

    probs = normalize_transitions(transitions)

    print("Sample transition probabilities:")
    for (src, dst), p in list(probs.items())[:10]:
        print(f"{src} -> {dst} : {p:.4f}")

#test
if __name__ == "__main__":
    from load_data import load_logs
    from transitions import build_event_timeline, extract_transitions

    logon, device, http = load_logs()
    user = "DTAA/FDP0500"

    timeline = build_event_timeline(logon, device, http, user)
    transitions = extract_transitions(timeline)

    probs = normalize_transitions(transitions)
    pi = stationary_distribution(probs)

    print("\nStationary distribution:")
    for state, val in pi.items():
        print(f"{state}: {val:.4f}")

    print("\nSum:", sum(pi.values()))