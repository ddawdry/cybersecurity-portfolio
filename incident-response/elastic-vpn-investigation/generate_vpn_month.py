"""
Generates a month of VPN logs (September 2026) for the fictional company
Northvale Logistics. Writes one JSON event per line to northvale_vpn_sept.json,
ready to upload into Kibana with "Upload a file".

Hidden in the data:
- A spike on Sunday 20 September: one IP makes 160 failed logins against e.price
- p.lloyd left the company on 15 September, but the account still connects after that
- m.devries connects from the Netherlands on a work trip (normal, not an attack)
"""
import json
import random
from datetime import datetime, timedelta

random.seed(7)

TZ = "+01:00"
START = datetime(2026, 9, 1)
DAYS = 30
LEAVE_DATE = datetime(2026, 9, 15)

uk_users = [
    "j.harper", "a.patel", "m.clarke", "s.okafor", "r.hughes", "l.bennett",
    "d.walsh", "k.morgan", "t.ahmed", "e.price", "c.fletcher", "n.ward",
    "b.carter", "h.ellis", "f.reid", "g.shaw", "p.lloyd", "w.ford",
    "y.khan", "o.grant",
]
uk_cities = ["Bath", "Bristol", "Swindon", "Cardiff", "Reading"]
ie_users = ["s.byrne", "c.doyle"]

events = []

def add(t, user, ip, country, city, action):
    events.append({
        "@timestamp": t.strftime("%Y-%m-%dT%H:%M:%S") + TZ,
        "Company": "Northvale",
        "UserName": user,
        "Source_ip": ip,
        "Source_Country": country,
        "Source_City": city,
        "action": action,
    })

def session(day, user, ip, country, city):
    s = day + timedelta(hours=random.randint(7, 10), minutes=random.randint(0, 59), seconds=random.randint(0, 59))
    if random.random() < 0.04:  # the odd typo before a good login
        add(s - timedelta(seconds=random.randint(10, 40)), user, ip, country, city, "failed")
    e = s + timedelta(hours=random.randint(3, 8), minutes=random.randint(0, 59))
    add(s, user, ip, country, city, "connect")
    add(e, user, ip, country, city, "teardown")

# Normal UK staff, weekdays only
for d in range(DAYS):
    day = START + timedelta(days=d)
    if day.weekday() >= 5:
        continue
    for i, user in enumerate(uk_users):
        if user == "p.lloyd" and day >= LEAVE_DATE:
            continue
        if random.random() < 0.75:
            session(day, user, f"198.51.100.{20 + i}", "United Kingdom", uk_cities[i % len(uk_cities)])
    for j, user in enumerate(ie_users):
        if random.random() < 0.7:
            session(day, user, f"192.0.2.{10 + j}", "Ireland", "Dublin")

# m.devries on a work trip to Rotterdam, 7 to 10 September
for d in [7, 8, 9, 10]:
    session(datetime(2026, 9, d), "m.devries", "192.0.2.80", "Netherlands", "Rotterdam")

# p.lloyd's account used after they left on 15 September
for d, h, m in [(17, 21, 14), (22, 22, 41), (26, 23, 5)]:
    s = datetime(2026, 9, d, h, m, random.randint(0, 59))
    add(s, "p.lloyd", "192.0.2.150", "United Kingdom", "London", "connect")
    add(s + timedelta(minutes=random.randint(20, 50)), "p.lloyd", "192.0.2.150", "United Kingdom", "London", "teardown")

# Brute force spike on Sunday 20 September
t = datetime(2026, 9, 20, 3, 2, 0)
for _ in range(160):
    add(t, "e.price", "203.0.113.77", "Netherlands", "Amsterdam", "failed")
    t += timedelta(seconds=random.randint(5, 15))

events.sort(key=lambda e: e["@timestamp"])

with open("northvale_vpn_sept.json", "w") as f:
    for e in events:
        f.write(json.dumps(e) + "\n")

print(f"Wrote {len(events)} events to northvale_vpn_sept.json")
