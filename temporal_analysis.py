"""
Task 5: Temporal and Comparative Analysis

This module evaluates how the entropy rate of security event behavior
changes over time. The goal is to assess system stability and identify
potential anomalies by comparing entropy values across different
time windows.
"""

# Imports

from load_data import load_logs
from transitions import build_event_timeline, extract_transitions
from markov import normalize_transitions, stationary_distribution
from entropy import entropy_rate


# Step 1
# Split the event timeline into two temporal segments

def split_timeline(timeline):
    """
    Split a timeline into two equal-sized temporal segments.

    Parameters:
        timeline (list): Ordered list of (timestamp, event) tuples

    Returns:
        first_half (list): First half of the timeline
        second_half (list): Second half of the timeline
    """
    midpoint = len(timeline) // 2
    first_half = timeline[:midpoint]
    second_half = timeline[midpoint:]
    return first_half, second_half


# ===================== Step 2 =====================
# Compute entropy rate for a single timeline segment

def entropy_for_timeline(timeline):
    """
    Compute the entropy rate for a given timeline segment.

    Steps:
    1. Extract transition frequencies
    2. Normalize transitions into probabilities
    3. Compute stationary distribution
    4. Compute entropy rate

    Parameters:
        timeline (list): Ordered list of (timestamp, event) tuples

    Returns:
        float: Entropy rate value
    """

    # Extract transition counts
    transitions = extract_transitions(timeline)

    # Normalize counts into transition probabilities
    probs = normalize_transitions(transitions)

    # Compute stationary distribution
    stationary = stationary_distribution(probs)

    # Compute entropy rate
    H = entropy_rate(probs, stationary)

    return H


# ===================== Step 3 =====================
# Main execution: temporal comparison

if __name__ == "__main__":

    # -------- Load dataset --------
    logon, device, http = load_logs()

    # -------- Choose a rich user --------
    user_id = "DTAA/FDP0500"
    print("Analyzed user:", user_id)

    # -------- Build full event timeline --------
    timeline = build_event_timeline(logon, device, http, user_id)
    print("Total events:", len(timeline))

    # -------- Split timeline into two time windows --------
    first_half, second_half = split_timeline(timeline)

    print("First half events :", len(first_half))
    print("Second half events:", len(second_half))

    # -------- Compute entropy for each window --------
    H_first = entropy_for_timeline(first_half)
    H_second = entropy_for_timeline(second_half)

    # -------- Print results --------
    print("\nTemporal Entropy Analysis Results")
    print("--------------------------------")
    print("Entropy (first half) : ", round(H_first, 4))
    print("Entropy (second half): ", round(H_second, 4))
    print("Entropy change       : ", round(H_second - H_first, 4))

    # -------- Interpretation hint --------
    if H_second > H_first:
        print("\nInterpretation: Increased entropy suggests more unpredictable behavior.")
    else:
        print("\nInterpretation: Decreased entropy suggests more structured behavior.")