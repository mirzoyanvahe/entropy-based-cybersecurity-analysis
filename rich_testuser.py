from load_data import load_logs

logon, device, http = load_logs()

users_logon = set(logon["user"])
users_http = set(http["user"])
users_device = set(device["user"])

active_users = users_logon & users_http & users_device

print("Number of users with logon + http + device:", len(active_users))

# pick one
test_user = list(active_users)[0]
print("Chosen active user:", test_user)

#Number of users with logon + http + device: 228
#Chosen active user: DTAA/RVS0852

#DTAA/FDP0500