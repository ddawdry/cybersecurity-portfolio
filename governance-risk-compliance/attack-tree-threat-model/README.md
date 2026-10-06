# Threat Modelling with an Attack Tree

## Overview
This project is based on work I did for a university module on Cyber Security and Networks. The task was to build an attack tree showing how an attacker could expose patient data in a new shared health record system. An attack tree puts the attacker's goal at the top and shows each route they could take to reach it.

## Disclaimer
For this portfolio version I changed the system to a fictional one called CareLink. The branches and attack steps are the ones I came up with in my original work.

## Scenario Summary
CareLink is a digital health record that patients use to book appointments, order prescriptions, and view test results. GPs, hospitals, pharmacies, and care services can all see the same record. One record holds a lot of sensitive data and many people can reach it, which makes it a big target.

## Project Objectives
The objectives of this project were to:
- Identify the ways an attacker could expose patient data
- Build an attack tree with at least 10 leaf nodes
- Explain how each attack route could reach the goal
- Consider technical, human, physical, and supplier risks

## Attack Tree Summary
The root goal is the disclosure of patient data. My tree has 10 branches and 20 leaf nodes. All branches are OR nodes, so any one of them could reach the goal on its own.

| Branch | Leaf Nodes |
|---|---|
| Exploit the app | Phishing for logins, zero-day in the app, intercepting traffic (MITM) |
| Social engineering | Pretending to be staff, pretexting to get into a building |
| Abuse of legit access | Selling data online |
| Denial of service | Flooding the system with traffic |
| Breach internal network | Weak passwords or no MFA, malware, unpatched software |
| Insider threats | Malicious leak, accidental leak |
| Third-party suppliers | Flaw in supplier software, attacking the supplier |
| Data storage weaknesses | Weak encryption, misconfigured cloud storage |
| Physical security | Stealing laptops or USBs, breaking into the server room |
| Weak access control | Too much access, default passwords |

## What I Would Change Now
Looking back, I would add AND nodes for attacks that need more than one step, move the denial of service branch since it does not expose data by itself, merge the two insider branches, rate each leaf by likelihood, and link each branch to a defence. These changes are explained in the PDF and were not part of my original work.

## Skills Demonstrated
- Threat modelling
- Attack tree analysis
- Risk identification
- Social engineering awareness
- Insider threat awareness
- Third-party risk awareness
- Security documentation

## Files Included
- `Attack-Tree-Threat-Model.pdf`

## Outcome
This project shows that patient data can be exposed in many ways, not just through hacking. People, suppliers, and physical security matter as much as technology. Building the tree helped me think like an attacker, which helps me work out where defences are needed.
