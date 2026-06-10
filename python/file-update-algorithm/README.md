# Update a File Through a Python Algorithm

## Overview
This project was completed as part of the Google Cybersecurity Professional Certificate. The activity focused on developing a Python algorithm to automate the management of an allow list used to control access to restricted resources. The algorithm reads a file containing authorised IP addresses, compares those addresses against a remove list, removes unauthorised entries, and updates the file with the updated allow list.

## Disclaimer
This scenario is fictional and was created for educational purposes as part of the Google Cybersecurity Professional Certificate.

## Project Objectives
The objectives of this project were to:

- Open and read data from a file using Python
- Convert file contents into a workable data structure
- Use iteration and conditional logic to process data
- Remove unauthorised IP addresses from an allow list
- Update a file with new access control information
- Demonstrate automation of a common security administration task

## Python Concepts Used
This project uses multiple main Python concepts, including:

```python
open()
with
.read()
.write()
.split()
.join()
for
if
.remove()
```

These concepts were combined to create an automated workflow for updating access control records.

## Algorithm Workflow
The algorithm performs the following steps:

1. Open the allow list file
2. Read the file contents into a string
3. Convert the string into a list
4. Iterate through a remove list
5. Identify unauthorised IP addresses
6. Remove matching IP addresses from the allow list
7. Convert the updated list back into a string
8. Write the revised data back to the file

## Skills Demonstrated
- Python programming
- File handling
- Data processing
- Access control management
- Automation
- Conditional logic
- Iteration using loops
- Security administration
- Problem solving

## Files Included
- `Algorithm-for-file-updates-in-Python.pdf`

## Outcome
This project demonstrates the ability to develop and explain a Python algorithm that automates access control maintenance. By combining file operations, list manipulation, iteration, and conditional logic, the solution efficiently removes unauthorised IP addresses and updates the allow list. The project highlights how programming can be applied to practical cybersecurity tasks and operational security workflows.
