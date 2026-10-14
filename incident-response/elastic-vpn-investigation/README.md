# VPN Log Investigation in Elastic

## Overview
In this project I loaded a month of VPN logs into Elasticsearch and investigated them in Kibana. I used Discover, the time histogram and the fields pane to spot problems, KQL to dig into them, and Lens to build visualisations. I finished by putting everything on one dashboard.

## Scenario
Northvale Logistics is a fictional UK company. Staff connect through a VPN, and every connection, failed login and disconnect is logged. HR told the security team that p.lloyd left on 15 September. I reviewed all VPN activity for September 2026.

I used AI to help write a Python script, `generate_vpn_month.py`, to create the month of logs to learn on. It makes 910 events of normal staff activity with a few problems hidden inside.

## Lab Setup
- Elasticsearch and Kibana running on my own machine
- Logs loaded with Kibana's Upload a file tool into the `northvale_vpn` index
- A data view using `@timestamp` as the time field
- The time filter set to 1 September to 1 October 2026

## What I Did
1. Spotted a spike on Sunday 20 September in the Discover histogram.
2. Used the fields pane and KQL to trace it to one IP making 160 failed logins against e.price, with none successful.
3. Searched for p.lloyd after their leaving date and found 3 late night connections from a new IP.
4. Checked connections from outside the UK and Ireland and confirmed one user's logins from the Netherlands were a work trip.
5. Built Lens visualisations for failed logins and connections by country.
6. Put everything on a Northvale VPN Overview dashboard, with an events over time chart that shows the spike straight away.

## Key Searches
```
Source_ip : "203.0.113.77" and not action : "failed"
UserName : "p.lloyd"
action : "connect" and not Source_Country : ("United Kingdom" or "Ireland")
```

## Findings
| Finding | Verdict | MITRE ATT&CK |
|---|---|---|
| 160 failed logins against e.price from one IP | True Positive (failed attack) | T1110.001 |
| Leaver account p.lloyd used after leaving | True Positive | T1078 |
| m.devries logging in from the Netherlands | False Positive (work trip) | None |

## What I Learned
- The time filter matters. If it does not cover the right dates, the data looks like it is missing.
- The histogram is a quick way to spot spikes before writing any query.
- NOT is just as useful as AND, for example to prove an attack never succeeded.
- Context changes the verdict. A login from abroad was fine, but a login from a leaver was not.
- Filtering before visualising matters, or one attack can skew the whole chart.

## Skills Demonstrated
- Loading data into Elasticsearch and creating data views
- Kibana Discover, time filter and fields pane
- KQL searching with field, AND, OR and NOT queries
- Lens visualisations and dashboards
- Detecting brute force and leaver account misuse
- Separating true positives from false positives
- Using AI tools to create practice data
- MITRE ATT&CK mapping

## How to Recreate It
1. Run `python3 generate_vpn_month.py` to create `northvale_vpn_sept.json`.
2. In Kibana, use Upload a file to import it into an index called `northvale_vpn`.
3. Set the time filter to 1 September to 1 October 2026.
4. Run the searches in the PDF.

## Files Included
- `Elastic-VPN-Log-Investigation.pdf`
- `generate_vpn_month.py`

## Outcome
This project shows how I use Kibana to investigate VPN logs, from spotting a spike to proving an attack failed and catching a leaver's account still in use. It also compares the same work in Splunk and Elastic.
