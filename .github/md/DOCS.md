# 📚 Documentation 📚

## 👉 Analysis

### Objective

Provide a free tool that help students to organize their school teams in Discord, by providing the facilities of creating private categories for team roles, saving notes, important URLs, and team member's information.

### Target

Students that want to start organizing their teams in Discord, due to the advantages of having text and voice channels that makes easier sharing ideas and scheduling meetings and also the possibility of using some of the thousands of bots available for this platform.

### Functional requirements

1. When the bot joins a server, it registers it, saving its server ID.
2. When the bot leaves a server, it unregisters it, removing all the information saved from that server (profiles are an exception to this rule).
3. The user can register themself to have a "school profile".
4. The user can either edit or remove the entries they have created in their profile.
5. The user can request see their saved school profile information so far.
6. The user can unregister themself (this action removes permanently all their personal information).
7. The school profile data that can be saved are the name, an email, a school ID, the Discord ID, a phone number, and relevant pages (e.g., social media).
8. The first time the registration command is executed, the bot will ask every profile entry to the user. If the user tries to register again, the bot will say that they actually have a profile and then will send it.
9. During the registration process, the user can skip introducing entries that they don't need or want to fill.
10. The user can request the creation of the security role, called "Bot Manager".
11. The user can request instructions of how to use the bot.
12. The user can request removal of the last given number of messages.
13. The user can request create a new _work team_ category, protected by a role with the same name.
14. The user can request removal of a _work team_. This action is permanent and also removes all the information associated with this team (profiles are an exception to this rule).
15. When a user requests the creation of a _work team_, the bot will create a category and a role with the given name,

(SUPERVISOR ROLE, it can be generated, and he can only read messages of every team, no interactions are allowed)
(POLL NEW MEMBER REQ)

### Non-functional requirements

1. The bot is always working.
2. The database is always working.
3. All commands can be executed properly if the user has the security role.
4. There is no command with permissions problems.
5. The information of every user is strictly encrypted in the database, except for their Discord ID.
6. The name and Discord ID of a profile cannot be null (both are required).
7. The maximum number of personal links allowed per user is 3.
8. The server unregistering process will not remove user registries, because they can be on another server that is simultaneously using the bot as well.
9. _Work team_ categories are only visible by their respective roles.
10. The maximum amount of _work teams_ per server is 15.

## 👉 Design

### Deployment diagram

...

### Bot class diagram

...

### Entity-Relationship diagram

...

[👈 Return to the main page.](../../README.md)
