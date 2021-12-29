# ✨ SupportBot repository ✨

## 👉 Introduction

<div align="center">
    <img src="./.github/img/SB_ICON.png" alt="SupportBot Logo" width="250px" height="250px">
</div>

### What is SupportBot?

SupportBot is a bot specially developed to help you with creating a safe space in where you and your school teammates can work and organize in different private channels with the help of subject roles.

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

|  Symbol   | Meaning              |
| :-------: | :------------------- |
|    `!`    | Command prefix       |
|   `foo`   | Command body         |
|   `...`   | Input description    |
|  `[...]`  | Required input       |
|  `(...)`  | Optional input       |
|  `@user`  | Discord user mention |
| `...:num` | A number input type  |
| `...:txt` | A text input type    |

### List

|        Command        | Protected | What does it do?                                                                                                 |
| :-------------------: | :-------: | :--------------------------------------------------------------------------------------------------------------- |
|        `!help`        |    NO     | Provides an overview of the avialable commands.                                                                  |
|       `!intro`        |    YES    | Sends an introduccion message to resume what is and how to use the bot.                                          |
|       `!bmrole`       |    NO     | Creates the _Bot Manager_ role. If a role with the same name currently exists, the bot won't generate a new one. |
| `!clean (amount:num)` |    YES    | Removes the last given number of messages, or 10 by default                                                      |

[📚 Start reading the documentation.](./.github/md/DOCS.md)
