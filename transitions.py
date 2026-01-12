import pandas as pd
from collections import Counter

def map_logon_event(row):
    return "LOGON" if row["activity"] == "Logon" else "LOGOFF"


def map_device_event(row):
    return "USB_CONNECT" if row["activity"] == "Connect" else "USB_DISCONNECT"


def map_http_event(row):
    return "HTTP_ACCESS"

def build_event_timeline(logon, device, http, user_id):
    events = []

    for _, row in logon[logon["user"] == user_id].iterrows():
        events.append((pd.to_datetime(row["date"]), map_logon_event(row)))

    for _, row in device[device["user"] == user_id].iterrows():
        events.append((pd.to_datetime(row["date"]), map_device_event(row)))

    for _, row in http[http["user"] == user_id].iterrows():
        events.append((pd.to_datetime(row["date"]), map_http_event(row)))

    events.sort(key=lambda x: x[0])
    return events

def extract_transitions(timeline):
    transitions = Counter()

    for i in range(len(timeline) - 1):
        src = timeline[i][1]
        dst = timeline[i + 1][1]
        transitions[(src, dst)] += 1

    return transitions

#test
if __name__ == "__main__":
    from load_data import load_logs

    logon, device, http = load_logs()

    #rich user
    #test_user = "DTAA/RVS0852"
    test_user = "DTAA/FDP0500"

    print("Test user:", test_user)

    timeline = build_event_timeline(logon, device, http, test_user)
    print("Total events:", len(timeline))

    transitions = extract_transitions(timeline)

    print("\nTop 15 transitions:")
    for (src, dst), count in transitions.most_common(15):
        print(f"{src} -> {dst} : {count}")