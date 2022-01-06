# ✨ SupportBot repository ✨

## 👉 Introduction

<div align="center">
    <img src="./.github/img/SB_ICON.png" alt="SupportBot Logo" width="250px" height="250px">
</div>

### What is SupportBot?

SupportBot is a Discord bot specially developed to help you start using Discord as an environment for work or school teams organization. It creates a healthy and safe space for teamworking by letting different groups of people coexist in a single server, but, with private and independent categories managed by roles (only obtainable with an invitation poll made by the team members or by manually adding the role to a user).

SupportBot also provides some interesting features, like the possibility of creating a _school profile_ and filling it as you need. That information can be later requested by you or any of your teammates that share a _team category_ whenever you want. This is pretty useful for assignment front pages, don't you think so?

If you are a teacher, or someone in charge, and you need to be sure that everything is going OK, there is the possibility of generating a _Supervisor_ role. This role has the particularity of make possible the access to all the _team categories_, but not interacting with them.

### Why SupportBot?

This is a completely free tool with some cool features, like:

- Having a registration procedure to save the student’s information.
- Having the possibility of requesting the registered information of the team members.
- Creating private categories managed by roles for teammate organization.
- Saving important URLs and notes.
- Deleting a specified amount of previous messages.
- A tutorial command.
- Helping commands.

## 👉 Invite

Click [here](https://discord.com/api/oauth2/authorize?client_id=877189956752248832&permissions=8&scope=bot) to add the bot into your server.

## 👉 Commands

### Protected actions

Some commands are protected by a special role, because they can be dangerous in different ways without supervision. To use them, you need to have assigned a role called _Bot Manager_, which can be generated with a command provided by the bot.

### Syntaxis

| Symbol  | Meaning                        |
| :-----: | :----------------------------- |
|   `!`   | Command prefix                 |
|  `foo`  | Command body                   |
| `[...]` | Required input                 |
| `(...)` | Optional input                 |
| `@USER` | Discord user mention (_input_) |
|  `NUM`  | An Integer number (_input_)    |
|  `TXT`  | Text (_input_)                 |

### List

|    Command     | Protected | What does it do?                                                                                                 |
| :------------: | :-------: | :--------------------------------------------------------------------------------------------------------------- |
|    `!help`     |    NO     | Provides an overview of the avialable commands.                                                                  |
|    `!intro`    |    YES    | Sends an introduccion message to resume what is and how to use the bot.                                          |
|   `!bmrole`    |    NO     | Creates the _Bot Manager_ role. If a role with the same name currently exists, the bot won't generate a new one. |
| `!clean (NUM)` |    YES    | Removes given number of newest messages, or 10 by default.                                                       |

[📚 Start reading the documentation.](./.github/md/DOCS.md)
