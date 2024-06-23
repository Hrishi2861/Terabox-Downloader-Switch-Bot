This is a Switch Bot written in Python for Downloading Videos From Terabox.

Terabox API/Base Code [**HERE**](https://t.me/Privates_Bots/7212).

---

<b>Fill this Values in [config.env](config.env)</b>
- `BOT_TOKEN`: The Switch Bot Token that you got from Bot Apps. `Str`

---
### For farther assistance visit my support group: [**@JetMirror**](https://t.me/jetmirrorchats).

---
## Deploy on VPS

## Prerequisites

### 1. Installing requirements

- Clone this repo:

```
git clone https://github.com/Hrishi2861/Terabox-Downloader-Switch-Bot/ && cd Terabox-Downloader-Switch-Bot
```

- For Debian based distros

```
sudo apt install python3 python3-pip
```

Install Docker by following the [Official docker docs](https://docs.docker.com/engine/install/#server).
Or you can use the convenience script: `curl -fsSL https://get.docker.com |  bash`


- For Arch and it's derivatives:

```
sudo pacman -S docker python
```

------

### 2. Build And Run the Docker Image

Make sure you still mount the app folder and installed the docker from official documentation.

- There are two methods to build and run the docker:
  1. Using official docker commands.
  2. Using docker-compose.

------

#### Build And Run The Docker Image Using Official Docker Commands

- Start Docker daemon (SKIP if already running, mostly you don't need to do this):

```
sudo dockerd
```

- Build Docker image:

```
sudo docker build . -t terabox
```

- Run the image:

```
sudo docker run -p 80:80 -p 8080:8080 terabox
```

- To stop the running image:

```
sudo docker ps
```

```
sudo docker stop id
```

----

#### Build And Run The Docker Image Using docker-compose

**NOTE**: If you want to use ports other than 80 and 8080 change it in [docker-compose.yml](docker-compose.yml).

- Install docker compose

```
sudo apt install docker-compose
```

- Build and run Docker image:

```
sudo docker-compose up --build
```

- To stop the running image:

```
sudo docker-compose stop
```

- To run the image:

```
sudo docker-compose start
```

- To get latest log from already running image (after mounting the folder):

```
sudo docker-compose up
```

---
## If anyone want requirements.txt to run without Docker, access it <a href='https://gist.github.com/Hrishi2861/3da4f269a95329d9e244e2e2567d9641'>Here</a>.

Cmd to start the Bot: bash start.sh
