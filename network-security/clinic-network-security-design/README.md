# Clinic Network and Security Design

## Overview
This project is based on a report I wrote for a university module on Cyber Security and Networks. The task was to design the network and cyber security setup for a new branch of a private healthcare clinic. The project covers subnetting, network devices, security measures, and how the design protects patient data.

The project includes:
- Network architecture and subnetting
- An IP addressing table
- Security architecture
- Open issues and challenges
- Improvements I would make now

## Disclaimer
For this portfolio version I changed the clinic name, location, host numbers, and IP ranges. Northbrook Health is a fictional company. The design approach and security choices are the ones I made in my original report.

## Scenario Summary
Northbrook Health is a private clinic opening a new branch in Exeter. The branch stores patient records, medical images, and staff information. It also hosts a web app where patients can book appointments and view prescriptions. The clinic wanted a network that is secure, reliable, low cost, and able to grow, as it plans to hire more GPs in the next two years.

## Objectives
The objectives of this project were to:
- Design a network that meets the clinic's needs and allows for growth
- Split the private address range into subnets for each department and the servers
- Choose the devices needed to build the network
- Choose security measures to protect patient and staff data
- Consider UK data protection law

## Network Design
I split the private range `172.16.8.0/22` into one subnet per area, starting with the largest.

| Network | Network Address | Mask | Usable Range | Broadcast |
|---|---|---|---|---|
| GP Team | 172.16.8.0 | /25 | 172.16.8.1 to 172.16.8.126 | 172.16.8.127 |
| Urgent Care | 172.16.8.128 | /26 | 172.16.8.129 to 172.16.8.190 | 172.16.8.191 |
| Physiotherapy | 172.16.8.192 | /27 | 172.16.8.193 to 172.16.8.222 | 172.16.8.223 |
| Admin Staff | 172.16.8.224 | /28 | 172.16.8.225 to 172.16.8.238 | 172.16.8.239 |
| Servers | 172.16.8.240 | /29 | 172.16.8.241 to 172.16.8.246 | 172.16.8.247 |
| ISP Link | 203.0.113.0 | /30 | 203.0.113.1 to 203.0.113.2 | 203.0.113.3 |

The network uses a router, firewall, switches, and wireless access points. These are standard, low cost devices.

## Security Measures
- Firewall to control traffic in and out of the network
- VPN for staff working remotely
- Antivirus on every device
- Role-based access control so staff only see what their job needs
- Daily backups kept on site and off site
- Network monitoring to spot suspicious activity

## Frameworks and Standards Used
- UK Data Protection Act 2018
- UK GDPR

## What I Would Change Now
Looking back, I would put the web server in a DMZ, use VLANs, give patients a separate Wi-Fi network, add firewall rules between subnets, add multi-factor authentication, encrypt stored data, and send logs to a SIEM. These changes are explained in the PDF and were not part of my original report.

## Skills Demonstrated
- Network design
- Subnetting and IP addressing
- Security architecture
- Access control
- Backup and recovery planning
- Data protection awareness
- Technical writing

## Files Included
- `Clinic-Network-Security-Design.pdf`

## Outcome
This project shows how I planned a network for a healthcare clinic, from subnetting the address range to choosing security measures that protect patient data. Reviewing it again also shows how my understanding has grown, especially around keeping internet-facing systems away from sensitive data.
