import math

def entropy_rate(probs, stationary):
    H = 0.0
    for (src, dst), p in probs.items():
        if p > 0:
            H += stationary[src] * (-p * math.log2(p))
    return H

def per_state_entropy(probs):
    entropy = {}
    for (src, dst), p in probs.items():
        entropy[src] = entropy.get(src, 0.0)
        if p > 0:
            entropy[src] -= p * math.log2(p)
    return entropy

#test
if __name__ == "__main__":
    from load_data import load_logs
    from transitions import build_event_timeline, extract_transitions
    from markov import normalize_transitions, stationary_distribution

    logon, device, http = load_logs()
    user = "DTAA/FDP0500"

    timeline = build_event_timeline(logon, device, http, user)
    transitions = extract_transitions(timeline)

    probs = normalize_transitions(transitions)
    pi = stationary_distribution(probs)

    H = entropy_rate(probs, pi)
    per_state = per_state_entropy(probs)

    print("Entropy rate:", round(H, 4))
    print("\nPer-state entropy:")
    for state, val in per_state.items():
        print(f"{state}: {val:.4f}")