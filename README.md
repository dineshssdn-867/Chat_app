<div align="center">
  
<img src="https://camo.githubusercontent.com/24cec635191128fc504cfaa08de7eecde66eac9cefeb939e8d6c49a1c592ba36/68747470733a2f2f7265732e636c6f7564696e6172792e636f6d2f64696e65736873636c6f75642f696d6167652f75706c6f61642f76313632323733333135312f35373136353863643265633436356130386532646332636633303235383032335f6f33687234782e706e67">
  
</div>

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->

[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)

<!-- ALL-CONTRIBUTORS-BADGE:END -->

#  D's Chat App Backend ✨

Personal Project - D's Chat App Backend

## Demo💻

[Demo](https://d-s-chat.web.app/login)

## Environment Variables⚙

To run this project, you will need to add the following environment variables to a .env file at the root of the project


- `AWS_KEY` : Your aws key for S3

- `AWS_SECRET_KEY` : Your secret aws key for S3

- `CACHE_USERNAME` : Operator of cache username

- `CACHE_PASSWORD` : Password of cache service password

## Run Locally🚀

Clone the project

```bash
  git clone https://github.com/dineshssdn-867/Chat_app.git
```

Go to the project directory

```bash
  cd Chat_app
```

Create Environement and install dependencies

```bash
python m venv env
env\Scripts\activate
pip install -r requirements.txt
```

Make migrations and start the server

```bash
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
```

## Features🧾

You can register as a user
<details>
  <summary>For User</summary>
  
  - Login and Register.
  - Chat with anyone like direct message to anyone in this app.
  - Update your profile.
</details>


## Tech Stack👨‍💻

**Backend:** Django, AWS S3, Nginx, Caching Services, Certbot, Docker, Docker-compose, Cloudflare, Digitalocean

[emoji key](https://allcontributors.org/docs/en/emoji-key)

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/dineshssdn-867"><img src="https://avatars.githubusercontent.com/u/66898317?v=4" width="100px;" alt=""/><br /><sub><b>Dinesh Nariani</b></sub></a><br /><a href="https://github.com/dineshssdn-867/DIM/commits?author=dineshssdn-867" title="Code">💻</a> <a href="https://github.com/dineshssdn-867/DIM/commits?author=dineshssdn-867" title="Documentation">📖</a> <a href="#design-dineshssdn-867" title="Design">🎨</a> <a href="#maintenance-dineshssdn-867" title="Maintenance">🚧</a> <a href="#projectManagement-dineshssdn-867" title="Project Management">📆</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
