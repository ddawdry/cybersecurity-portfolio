# SOC Alert Triage Practice
 
## Overview
This project was completed as part of the TryHackMe SOC Level 1 learning path. The activity focused on triaging security alerts in a simulated SOC dashboard as a Level 1 (L1) analyst. I reviewed five alerts, investigated the evidence in each one, decided whether each alert was a True Positive or a False Positive, and wrote a comment explaining my reasoning.
 
## Disclaimer
The alerts, users, and systems in this project are fictional and were created for educational purposes as part of the TryHackMe SOC Level 1 learning path.
 
## Project Objectives
The objectives of this project were to:
- Follow a structured alert triage process
- Investigate alert details such as users, hosts, networks, and processes
- Separate malicious activity from normal business activity
- Classify alerts as True Positive or False Positive
- Write clear comments that explain my analysis and verdict
## Triage Process
Each alert was handled using the following steps:
 
1. Assign the alert to myself and move it to In Progress
2. Review the alert name, description, and key indicators
3. Identify who or what is affected, such as the user, host, or network
4. Review the action in the alert and the context around it
5. Decide if the alert is a True Positive (malicious) or a False Positive (not malicious)
6. Write a comment explaining the evidence and verdict
7. Move the alert to Closed
## Alerts Investigated
 
| Alert | Severity | Verdict |
|---|---|---|
| Potential Data Exfiltration | Critical | False Positive |
| Double-Extension File Creation | High | True Positive |
| Download from GitHub Repository | Low | False Positive |
| Email Marked as Phishing after Delivery | Medium | True Positive |
| Spike of Domain Discovery Commands | Medium | True Positive |
 
### 1. Potential Data Exfiltration
The alert triggered because a device sent more than 5 GB of data to one destination in a day.
 
Evidence:
- Destination was `*.zoom.us`, a trusted video call service
- Source network was `UK04/MEETINGROOM`
- Sent data was 5.8 GB and received data was 5.2 GB
Reasoning: Video calls send and receive similar amounts of data. A meeting room device using Zoom all day matches this traffic. There were no signs of data theft.
 
### 2. Double-Extension File Creation
The alert triggered because a file with two extensions was created.
 
Evidence:
- File name was `cats2025.mp4.exe`, an executable disguised as a video
- The Mark of the Web showed it was downloaded from `freecatvideoshd.monster`, an untrusted site
- The file was downloaded through Chrome by user `S.Conway` on HR laptop `LPT-HR-009`
Reasoning: Windows can hide the last file extension, so the user would only see `cats2025.mp4`. This is a common phishing trick. The file MD5 hash should be checked against threat intelligence and the host should be checked to see if the file was run.
 
### 3. Download from GitHub Repository
The alert triggered because a user downloaded from GitHub.
 
Evidence:
- Accessed URL was `github.com/facebook/react`
- User `G.Chandler` was on IT laptop `LPT-IT-063`
- Source network was `VPN/DEVELOPERS`
Reasoning: React is a widely used JavaScript library maintained by Meta. An IT user on the developer network downloading development tools is expected activity.
 
### 4. Email Marked as Phishing after Delivery
The alert triggered because an email was classified as phishing after it reached the user.
 
Evidence:
- Sender showed as `support@microsoft.com`
- SPF and DKIM checks both failed, so the sender was spoofed
- The email used urgent language about a 600% price increase
- The email pushed the user to download an attached file, `REPORT.rar`
- The recipient was the IT Manager, a high value target
Reasoning: The sender address was faked. Microsoft does not send pricing updates as RAR attachments. Archive files can hide malware and avoid some email filters. The email should be removed, the sender blocked, and the user checked to see if the attachment was opened.
 
### 5. Spike of Domain Discovery Commands
The alert triggered because several Active Directory discovery commands were run in a short time.
 
Evidence:
- Commands included `whoami /priv`, `net group "Domain Admins" /domain`, and `nltest /dclist`
- Host was `DMZ-MSEXCHANGE-2013`, an internet facing Exchange 2013 server on Windows Server 2012 R2
- Commands ran as `NT AUTHORITY\SYSTEM`, the highest privilege account on Windows
- Process tree: `w3wp.exe` (IIS web server) started `C:\Users\Public\revshell.exe`, which started `cmd.exe`
Reasoning: A web server should never start an unknown executable from a public folder. This suggests the server was exploited and a reverse shell was installed. The attacker was looking for admin accounts and domain controllers. This needs urgent escalation and the host should be isolated.
 
## What I Got Wrong
I first marked the phishing email as a False Positive. The sender address showed `support@microsoft.com`, so I assumed it was genuine. I also thought a RAR file was lower risk than an executable.
 
After reviewing the alert again, I learned that:
- A sender address can be faked and proves nothing on its own
- SPF and DKIM checks show whether a sender is genuine, and both had failed
- Archive files like RAR can hide malware inside them
I then corrected the verdict to True Positive.
 
## Lessons Learned
- An alert is a question to investigate, not a confirmed attack
- Context such as device names, networks, and destinations often explains an alert
- Check SPF and DKIM before trusting an email sender
- Review the process tree and check whether each parent process should start its child
- A good comment covers who was affected, what happened, the evidence, and the next step
## Skills Demonstrated
- Alert triage
- True Positive and False Positive analysis
- Phishing email analysis
- Endpoint and process tree analysis
- Email authentication checks (SPF and DKIM)
- Security documentation
- Investigation note-taking
## Outcome
This project shows how a Level 1 SOC analyst triages alerts using evidence and context. Out of five alerts, three were confirmed as malicious and two were normal business activity. The project also shows how I learned from a wrong verdict and improved my process for checking phishing emails.
