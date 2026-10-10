# Database Design for a Profile Service

## Overview
This project is based on a database module I took at university. The task was to design and build the database behind a profile service for a community app. I started with the raw profile data, normalised it to Third Normal Form, drew the entity relationship diagram, then built the tables, a view, CRUD stored procedures, and a trigger in Microsoft SQL Server.

The project covers:
- Normalisation from UNF to 3NF
- An entity relationship diagram
- A field definition grid (data dictionary)
- SQL tables with keys and constraints
- A view that joins the tables into a full profile
- CRUD stored procedures
- A trigger that logs new users

## Disclaimer
For this portfolio version I changed the app name, the entity names, the sample data and the server details. Margins is a fictional app. The database design, the normalisation steps and the SQL are the ones I wrote for my coursework.

## Scenario
Margins is a reading community app. The profile service stores each user's profile, their favourite genres, and the city they are based in. A user can pick many genres, and each genre can be picked by many users.

## Database Structure
| Table | Purpose |
|---|---|
| USERS | Stores profile data (name, username, email, bio, city) |
| CITY | Stores each city once, linked from USERS |
| GENRE | Stores the list of genres |
| USERGENRE | Linking table for the many to many link between users and genres |
| USERLOG | Stores a log record each time a new user is added |

## Security Note
This profile database does not store passwords. In the full system, authentication is handled by a separate service, so the profile data holds no credentials. If a credential ever had to be stored here, it would be kept as a secure hash, never as plaintext.

## What I Would Improve Now
- Add indexes on Email and Username
- Add ON DELETE rules so removing a user clears their USERGENRE rows
- Return the new UserID from AddUser
- Expand the log to record updates and deletes

## Skills Demonstrated
- Database normalisation to 3NF
- Entity relationship modelling
- SQL table design with keys and constraints
- Views, stored procedures and triggers
- Microsoft SQL Server
- Security aware data design

## Files Included
- `Database-Design-Profile-Service.pdf`

## Outcome
This project shows how I design a database from raw data to a working build. It covers normalising the data, modelling it, then building the tables, a view, CRUD procedures and a logging trigger in SQL Server.
