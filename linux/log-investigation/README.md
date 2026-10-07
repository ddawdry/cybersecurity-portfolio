# Linux Log Investigation Lab

## Overview
This lab practises the kind of log checking a Level 1 SOC analyst does on a Linux host. It builds on the basics from the TryHackMe Linux Fundamentals rooms, but in a security setting. I set up two virtual machines in my home lab, created some suspicious activity on purpose, then used Linux commands to find it.

The lab covers three things:
- Finding and counting failed SSH logins, and tracing where they came from
- Finding a cron job an attacker could use to keep access
- Finding a process running from a suspicious location

## Lab Setup
| Machine | Role | Details |
|---|---|---|
| ubuntu-lab | Target | Ubuntu 24.04, runs SSH |
| kali | Attacker | Kali Linux |

Both machines sit on a host-only network, so nothing leaves my own computer.

## What I Did
1. Ran failed SSH logins from the attacker machine, then one successful login.
2. Found the failed logins in `/var/log/auth.log` with `grep`, counted them with `wc`, and traced the source IP with `awk` and `sort`.
3. Added a cron job that runs a hidden script, then found it with `crontab -l`, the cron spool folder, and the system log.
4. Ran a process from `/tmp` under a hidden name, then found it with `ps` and confirmed what it was with `/proc/PID/exe` and a file hash.
5. Cleaned up everything I created.

## Mapping to MITRE ATT&CK
| What I found | Technique | ID |
|---|---|---|
| Repeated SSH login attempts | Brute Force | T1110 |
| Cron job for persistence | Scheduled Task/Job: Cron | T1053.003 |
| Program run from /tmp | Masquerading | T1036 |

## Skills Demonstrated
- Linux log analysis
- SSH brute force detection
- Cron job and persistence checks
- Process investigation
- Command line tools (grep, awk, wc, sort, ps)
- MITRE ATT&CK mapping

## Files Included
- `Log-Investigation-Lab.pdf`

## Outcome
This lab shows how I would check a Linux host for three common signs of attack: brute force logins, cron job persistence, and a process hiding in /tmp. It links the Linux basics to real SOC work and sets up my home lab for sending these logs to a SIEM later.
