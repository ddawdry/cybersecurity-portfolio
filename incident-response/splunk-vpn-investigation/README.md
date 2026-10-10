# VPN Log Investigation in Splunk

## Overview
In this project I loaded VPN logs into Splunk and searched them for signs of account misuse. I built an index, checked the data, then hunted for two common attack patterns: impossible travel and password spraying. I finished by designing an alert for the spraying pattern.

## Scenario
Northvale Logistics is a fictional UK company. Staff connect through a VPN, and the gateway logs every session in JSON. The security team asked me to review a week of logs and report anything unusual.

I used AI to help write a Python script, `generate_vpn_logs.py`, to create the week of logs to learn on. It makes 1,500 events of normal staff activity with an attack hidden inside, so I had realistic data to hunt through.

## Lab Setup
- Splunk Free running on my own machine
- A new index called `vpn_logs`
- The log file uploaded through Add Data with the `_json` source type

## What I Did
1. Checked all 1,500 events loaded and broke the logins down by country.
2. Followed up the logins from Brazil and found j.harper logging in from the UK and Brazil 12 minutes apart.
3. Counted how many usernames each IP tried and found one IP trying 9 accounts.
4. Broke that IP's events down by user and action, which linked the two findings.
5. Designed an hourly alert for password spraying.

## Key Search
```
index=vpn_logs
| stats dc(UserName) as users count by Source_ip
| where users > 3
| sort - users
```

## Findings
| Finding | Evidence | MITRE ATT&CK |
|---|---|---|
| Password spraying | 203.0.113.45 tried 9 usernames | T1110.003 |
| Account compromise | j.harper logged in from the UK then Brazil 12 minutes apart | T1078 |

## What I Learned
- With the `_json` source type, adding `spath` extracts the fields a second time. That doubled my values and inflated my counts, so I removed it.
- `stats dc()` counts unique values, which makes it easy to spot one IP trying many accounts.
- Two small findings can link up into one bigger story, so it is worth following each lead.
- Splunk Free does not include alerting, so I planned the alert instead of building it.

## Skills Demonstrated
- Splunk index setup and data upload
- SPL searching and statistics
- Threat hunting in VPN logs
- Detecting impossible travel and password spraying
- Designing detection alerts
- Using AI tools to create practice data
- MITRE ATT&CK mapping

## How to Recreate It
1. Run `python3 generate_vpn_logs.py` to create `vpn_logs.json`.
2. Create a `vpn_logs` index in Splunk.
3. Upload the file with the `_json` source type.
4. Set the time picker to All time and run the searches in the PDF.

## Files Included
- `Splunk-VPN-Log-Investigation.pdf`
- `generate_vpn_logs.py`

## Outcome
This project shows how I use Splunk to turn raw VPN logs into findings. It covers loading the data, hunting for attack patterns, linking evidence together, and planning an alert so the same attack would be caught automatically.
