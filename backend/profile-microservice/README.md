# Profile Service Microservice

## Overview
This project is based on a university report where I designed, built and tested a profile microservice. The service manages user profile data for a community app. It is written in Python, follows RESTful API design, stores data in Microsoft SQL Server, and runs in a Docker container. Authentication is handled by a separate service, and the API is documented with Swagger.

The project covers:
- A use case diagram and an entity relationship diagram
- Token based authentication and role based access control
- Secure handling of secrets and personal data
- RESTful API endpoints documented with Swagger
- Docker deployment
- Functional and security testing

## Disclaimer
For this portfolio version I changed the app name, the entity names, the sample data and the server details. Margins is a fictional app. The design, the code and the testing approach are the ones I used in my coursework.

## What the Service Does
A normal user can create, view, update and delete their own profile. An admin can view, update or delete any user's profile, for example to deal with a support ticket or remove a spam account. Every action is checked against an external authenticator before it runs.

## Security Highlights
- Authentication is delegated to a separate service, so no passwords are stored in the profile database
- Each request is checked for a valid token before any protected action runs
- Role based access control keeps admin actions separate from normal user actions
- Database credentials are read from environment variables, not written into the code
- Data models validate incoming data

## Tech Used
- Python
- Flask and Connexion
- SQLAlchemy
- Microsoft SQL Server
- JWT for tokens
- Swagger (OpenAPI)
- Docker

## Testing
I used Swagger to confirm every endpoint worked, then Postman to send real requests with and without tokens. Tests confirmed that protected endpoints rejected requests with no token, that users could not open another user's profile, and that admin endpoints were blocked for normal users.

## What I Would Improve Now
- Add automated tests instead of only manual testing in Postman
- Expand error handling while still hiding personal details
- Add filtering to the admin endpoints so they scale with more users

## Skills Demonstrated
- RESTful API design in Python
- Token based authentication and role based access control
- Secure handling of secrets and personal data
- SQLAlchemy and Microsoft SQL Server
- API documentation with Swagger
- Docker containerisation
- Functional and security testing

## Files Included
- `Profile-Service-Microservice.pdf`

## Outcome
This project shows how I build a secure, documented microservice from design through to testing. It brings together database design, a REST API, token based authentication, role based access control and containerised deployment, with security and privacy considered at each step.
