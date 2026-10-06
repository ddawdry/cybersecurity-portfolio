# Alert Triage Methodology
 
## Overview
This project explains how I triage security alerts as a Level 1 (L1) SOC analyst. I learned the triage process while working through the TryHackMe SOC Level 1 learning path. To show how I apply it, I wrote four example alerts of my own and investigated each one, deciding whether it was a True Positive or a False Positive.
 
## Disclaimer
All alerts, users, hosts, and companies in this project are fictional and were created by me. None of the examples come from TryHackMe rooms.
 
## Project Objectives
The objectives of this project were to:
- Document a clear and repeatable alert triage process
- Apply the process to different types of security alerts
- Separate malicious activity from normal business activity
- Use context such as hosts, users, and change tickets to support a verdict
- Explain my reasoning in a way another analyst can follow

## Triage Process
I follow the same steps for every alert:
 
1. Assign the alert to myself and move it to In Progress
2. Review the alert name, description, and key details
3. Identify who or what is affected and check what happened before and after the alert
4. Decide if the alert is a True Positive (malicious) or a False Positive (not malicious)
5. Write a comment with my evidence and verdict, then close or escalate the alert

## Questions I Ask
- Who or what is affected?
- Is there a normal reason for this activity?
- Where did it come from or go to?
- What process started it?
- Does it match a known IT change?

## Example Investigations
The examples are set at a fictional company called Northfield Logistics.
 
| Example | Severity | Verdict | Main Clue |
|---|---|---|---|
| Multiple Failed Logins | Medium | False Positive | Matches a backup task after a password change |
| Suspicious PowerShell Started by Email Client | High | True Positive | Outlook started hidden, encoded PowerShell |
| Payroll Email with Login Link | Medium | True Positive | Lookalike domain with a login link |
| User Added to Domain Admins | High | False Positive | Matches an approved change ticket |
 
### 1. Multiple Failed Logins
A service account had 42 failed logins in 2 minutes from the backup server. The password had been changed the day before, so the backup task was most likely still using the old one. There were no successful logins and no attempts from other hosts.
 
### 2. Suspicious PowerShell Started by Email Client
Outlook started PowerShell on a finance laptop using the `-nop`, `-w hidden`, and `-enc` options. These hide the window and the command. This points to a malicious attachment and needs urgent escalation.
 
### 3. Payroll Email with Login Link
An email asked staff to confirm their bank details through a link. The sender used a lookalike domain. SPF and DKIM passed, but that only proved the email came from the attacker's own domain.
 
### 4. User Added to Domain Admins
An IT admin added a temporary account to Domain Admins during working hours. The change matched an approved change ticket, so it was expected. I noted that the account should be removed after the work ends.
 
## What I Learned
While practising, I trusted a phishing email because the sender address looked like a well known company. I learned that a sender address can be faked and proves nothing on its own. Example 3 builds on this. Even when SPF and DKIM pass, the domain itself can belong to an attacker.
 
Other lessons:
- An alert is something to check, not proof of an attack
- Context like host names, networks, and change tickets often explains an alert
- The process tree shows how activity started
- A good comment covers who was affected, what happened, the evidence, and the next step

## Skills Demonstrated
- Alert triage
- True Positive and False Positive analysis
- Phishing email analysis
- Process tree analysis
- Active Directory security awareness
- Email authentication checks (SPF and DKIM)
- Security documentation

## Files Included
- `Alert-Triage-Methodology.pdf`

## Outcome
This project shows the triage process I use and how I apply it to different types of alerts. Two of the examples were real attacks and two were normal activity. It shows that getting a verdict right depends on checking the context, not just the alert name.
