"""
Generates a week of VPN logs for the fictional company Northvale Logistics.
Writes one JSON event per line to vpn_logs.json, ready to upload to Splunk.

Hidden in the data:
- One IP in Brazil tries 9 different usernames (password spraying)
- One of those accounts, j.harper, gets in 12 minutes after logging in from the UK
"""
import json
import random
from datetime import datetime, timedelta

random.seed(42)

ATTACKER_IP = "203.0.113.45"
START = datetime(2026, 9, 14)

uk_users = [
    "j.harper", "a.patel", "m.clarke", "s.okafor", "r.hughes", "l.bennett",
    "d.walsh", "k.morgan", "t.ahmed", "e.price", "c.fletcher", "n.ward",
    "b.carter", "h.ellis", "f.reid", "g.shaw", "p.lloyd", "w.ford",
    "y.khan", "o.grant",
]
ie_users = ["s.byrne", "c.doyle"]
nl_user = "m.devries"

def home_ip(i):
    return f"198.51.100.{20 + i}"

events = []

def add(t, user, ip, country, action):
    events.append({
        "EventTime": t.strftime("%Y-%m-%dT%H:%M:%S"),
        "Company": "Northvale",
        "UserName": user,
        "Source_ip": ip,
        "Source_Country": country,
        "action": action,
        "port": 443,
        "protocol": "tcp",
    })

def session(day, user, ip, country, start_hour_range=(7, 10), skip=None):
    s = day + timedelta(hours=random.randint(*start_hour_range), minutes=random.randint(0, 59), seconds=random.randint(0, 59))
    e = s + timedelta(hours=random.randint(2, 8), minutes=random.randint(0, 59))
    add(s, user, ip, country, "login")
    add(e, user, ip, country, "teardown")

# j.harper on Monday 14th: fixed sessions so the timeline is clear
add(datetime(2026, 9, 14, 8, 2, 11), "j.harper", home_ip(3), "United Kingdom", "login")
add(datetime(2026, 9, 14, 12, 1, 44), "j.harper", home_ip(3), "United Kingdom", "teardown")
add(datetime(2026, 9, 14, 13, 30, 5), "j.harper", home_ip(3), "United Kingdom", "login")
add(datetime(2026, 9, 14, 17, 22, 10), "j.harper", home_ip(3), "United Kingdom", "teardown")

# Password spraying from Brazil on Monday morning
targets = ["a.patel", "m.clarke", "s.okafor", "r.hughes", "l.bennett", "d.walsh", "k.morgan", "t.ahmed"]
t = datetime(2026, 9, 14, 8, 10, 3)
for user in targets:
    for _ in range(3):
        add(t, user, ATTACKER_IP, "Brazil", "login_failed")
        t += timedelta(seconds=random.randint(6, 12))
add(datetime(2026, 9, 14, 8, 14, 1), "j.harper", ATTACKER_IP, "Brazil", "login_failed")
add(datetime(2026, 9, 14, 8, 14, 20), "j.harper", ATTACKER_IP, "Brazil", "login_failed")
add(datetime(2026, 9, 14, 8, 14, 37), "j.harper", ATTACKER_IP, "Brazil", "login")
add(datetime(2026, 9, 14, 9, 1, 10), "j.harper", ATTACKER_IP, "Brazil", "teardown")

# Netherlands: one user on a work trip, 4 sessions
for d in range(1, 5):
    session(START + timedelta(days=d), nl_user, "192.0.2.80", "Netherlands")

# Ireland: two users, 26 sessions in total
for i in range(26):
    user = ie_users[i % 2]
    ip = "192.0.2.10" if user == "s.byrne" else "192.0.2.11"
    session(START + timedelta(days=i % 7), user, ip, "Ireland")

# UK: normal sessions until we reach 1,500 events in total
while len(events) < 1500:
    idx = random.randrange(len(uk_users))
    user = uk_users[idx]
    day = START + timedelta(days=random.randint(0, 6))
    if user == "j.harper" and day.date() == START.date():
        continue  # keep j.harper's Monday timeline clean
    session(day, user, home_ip(idx), "United Kingdom")

events.sort(key=lambda e: e["EventTime"])

with open("vpn_logs.json", "w") as f:
    for e in events:
        f.write(json.dumps(e) + "\n")

print(f"Wrote {len(events)} events to vpn_logs.json")