# MakeAIWork

## Projects

This repository contains sources to be used by python students. Directory <i>projects</i> contains the (re)sources:
<ul>
<li>p1, p2 and p3</i> containing
<i>cursus_materiaal</i> with a project description
</ul>

Directory <i>notebooks</i> contains Jupyter notebooks that can be used in Jupyter Lab. Directory <i>scripts</i> contains some example Python scripts. 

---

## Python AI Workspace Installation
Watch [instruction videos at YouTube](https://youtube.com/playlist?list=PLf5zREwsIjUNQ2y4TGi9F0uXQZ1B08d_v) 


### Clone this Git repository
To be able to use this repository and handover your code, you need to have remote access to Github.

<ol>

<li>

**Create an account at [Github](https://github.com)**

</li>

<li>

**Install Git**

Make sure you select "Checkout as-is, commit Unix-style line endings" during the installation process. 

<ul>

<li>

[Git for Windows](https://gitforwindows.org/)

</li>

<li>

[Git for Mac](https://git-scm.com/download/mac)

</li>

</ul>

<li>

**Install [Homebrew](https://brew.sh/) (MacOS only)**

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

</li>

<li>

**Install [iterm2](https://iterm2.com/) (MacOS)**

```bash
brew install iterm2
```

</li>

<li>

**Install zsh (MacOS and Ubuntu)**

<ul>

<li>

Install [zsh](https://www.howtogeek.com/362409/what-is-zsh-and-why-should-you-use-it-instead-of-bash/) on MacOS using

```bash
brew install zsh
```

In Ubuntu
```bash
sudo apt install zsh 
```

</li>

<li>

Add iTerm2 path to zsh profile
 
 ```bash
echo "eval \"\$(homebrew/bin/brew shellenv)\"" >> ~/.zshrc
```

</li>
 
 <li>
 
**(Optional) Install oh-my-zsh (MacOS and Ubuntu)**
  
```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

</li>

</ul>

</li>

<li>

**Install [GitHub CLI](https://cli.github.com/) (MacOS and Ubuntu)**

```bash
brew install gh
```
 
[Installation instructions on Ubuntu](https://www.techiediaries.com/install-github-cli-ubuntu-20/)

</li>

<li>

**Create a ssh key-pair token**

Start a (git) bash shell *and generate a secret key pair with your student email adress

```sh
ssh-keygen -t Ed25519 -C {your@student.email.com}
```

</li>

<li>

**Transfer your <b>public</b> key to Github**

If you installed the GitHub client, you can authenticate with the following command in the terminal and select ssh for authentication

```sh
gh auth login
```

otherwise enter the following in (git) bash shell to view the contents of your public key

```sh
cat ~/.ssh/id_ed25519.pub
```
and paste this in the text area when adding a [new ssh key in GitHub](https://github.com/settings/ssh/new)

</li>

<li>

**Create a fork of this repository** 

Create a fork of MitwRdam/MakeAIWork in [GitHub](https://github.com/MitwRdam/MakeAIWork) or 
use the GitHub Client by entering the following commands in your terminal

```bash
gh repo fork https://github.com/MitwRdam/MakeAIWork
```
</li>

<li>

**Clone your <b>fork</b>**
If you installed the GitHub client, you can authenticate with the following command in the terminal

```sh
gh repo clone git@github.com:{your_github_username}/MakeAIWork.git
```

otherwise enter the following command in your (git)bash shell after replacing {your_github_username} with your GitHub username.
```sh
git clone git@github.com:{your_github_username}/MakeAIWork.git
```

</li>

<li>

**Configure git**

In order to commit and push your changes, you need identitify yourself. 

Open a (git)bash, enter directory MakeAIWork and run:
```bash
sh/git_config.sh {your_github_username} {your@student.email.com}
```
This script will also set the [pull policy](https://www.git-scm.com/docs/git-pull) to rebase.

</li>

<li>

**Add upstream to original remote repository**

To be able To be able to fetch and merge changes from this repository using (bash) commands, you need to have a (second) upstream.  
If you used the GitHub client to create the fork you can <strong>skip</strong> this step, otherwise enter the following commands

```bash
git remote add mitwrdam https://github.com/MitwRdam/MakeAIWork
```

</li>

<li>

Keep your fork repository up-todate by regularly pulling changes from the original remote repository into your local fork..

```bash
 git pull mitwrdam main
```

and push the changes to you remote fork 

```bash
git push
```

</li>

</ol>

### Enable [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/about) (Windows only)
<ol>

<li>

**Check If Your Processor Supports [Virtualization](https://www.technorms.com/8208/check-if-processor-supports-virtualization)**

</li>

<li>

**Enable Windows Subsystem for Linux**

Enter the following command in Windows Powershell:
```pwsh
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

</li>

<li>

**Enable the Virtual Machine Platform feature (Windows only)**
Enter the following command in Windows Powershell:
```pwsh
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

</li>

<li>

**Make WSL 2 Default (Windows only)**
Enter the following command in Windows Powershell:
```pwsh
wsl –set-default-version 2
```

</li>

</ol>

### Install Docker Desktop (Windows and MacOS)
To facilitate you with a managed portable [isolated](https://learndocker.online/introduction/the-whats-and-whys/what-are-containers/) [Development Environment]((https://learndocker.online/introduction/the-whats-and-whys/why-docker-for-devs)), we provide a Docker image in which all dependencies are preinstalled. We prefer Docker for isolation since it is a much lighter solution than [Virtual Machine](https://learndocker.online/introduction/the-whats-and-whys/containers-vs-vms/). 

<ol>

<li>

**Download and install [Docker Desktop](https://www.docker.com/get-started)**

[Download for Mac with Apple M* chip](https://docs.docker.com/desktop/mac/apple-silicon/)

<li>

**Configure Docker Desktop**

Open Docker Desktop, go to settings and select <i>Start when you login</i>

In Windows you can a script to enable Docker Desktop to start directly after you start Git Bash:

```bash
sh/git_bash_profile.sh
```

this script will also navigate automatically to the MakeAIWork directory.

</li>

<li>

**Test your Docker installation**
Check if you are able to use Docker by running an example container in <b>(git) bash</b>
```sh
docker run hello-world
```

If that works, you can run the scripts to start the Docker container as described in section <u>Python AI Workspace Usage</u>.

</li>

<li>

**Install python to enable the webbrowser to open automatically after starting a webservice**

<ol>

<li>

Install [python](https://www.python.org/downloads/release/python-3105/)

</li>

<li>

Install venv (Ubuntu)

```sh
sudo apt install python3.10-venv
```

</li>

<li>

Create virtual Python environment

```sh
python3 -m venv .
```

</li>

<li>

Activate venv
```sh
source bin/activate
```
</li>

</ol>

***NOTE***
We only run Python directly on the host to sue the webbrowser module. For ad Docker Workaround on Windows, you need to install the Ubuntu in Windows sub-system.

</li>

</li>

</ol>

### Edit with Visual Studio Code
<ol>

<li>

Install [Visual Studio Code](https://code.visualstudio.com)

</li>

<li>

**Enable VSCode to be opened from the command line (macOS only)**

In VSCode, open the Command Palette and type 'shell command' in order to select the Shell command: Install ‘code’ command in PATH

</li>

<li>

**Start vscode with command from current directory**

Start a (git) bash shell and enter directory MakeAIWork, from there use the command <i>code</i> to start vscode.
```sh
cd MakeAIWork
code .
```

</li>

<li>

**Install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)**

</li>

<li>

**Install Live Share**

Follow the instructions at [Collaborate with Live Share](https://code.visualstudio.com/learn/collaboration/live-share)

</li>

</ol>

## Run Python scripts with Graphical UI in Docker (MacOS only)

<ol>

<li>

**Install XQuartz X.Org Window System**
On the MacOS host, we use xquartz to provide us with a MacOS X Window System.<br>
Download and install [xquartz](https://www.xquartz.org/)<br>
Log out and Log in to activate the changes the terminal

</li>

<li>

**Configure XQuartz to allow network connections from host**

<ol>

<li>

Get your IP address

Run the following command in the terminal to see your IP address

```bash
ifconfig en0 | grep 'inet ' | awk '{print $2}'
```

<li>

Start XQuartz

```bash
open -a XQuartz
```

which will open a XQuartz terminal in which you enter

```sh
xhost {Your IP}
```

Click on the word 'XQuartz' on the top left of your screen (next to the Apple logo) and select <i>Preference</i>. Open the tab 
<i>Security</i> and check 'Allow connections from network clients' 

</li>

</ol>

</li>

<li>

**Install Socat**
The graphical Python script runs with a Linux X Window System in a Docker container. To connect this to the MacOS X Window System on the host we use the [command line utility socat](https://linux.die.net/man/1/socat). 

```bash
brew install socat
```

</li>

<li>

**Test by running a Python script with GUI**

</li>

</ol>

### Ubuntu in Windows sub-system (alternative for Windows users)
Instead of Git bash and Docker, you can install a complete Ubuntu terminal environment with Windows Subsystem for Linux (WSL). Although Ubuntu can be installed in minutes, you lack the benefit of all preinstalled Python modules in an isolated container. 

<ol>

<li>

Download and install [Ubuntu LTS on WSL2](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-11-with-gui-support#3-download-ubuntu)

</li>

<li>

Install Miniconda

</li>

<li>

Install dependencies

</li>

<li>

Install Jupyterlab

</li>

</ol>

---

## Python AI Workspace Usage
Students use a containerised Python environment running a [Docker](https://www.docker.com/) image. 

### Files available to the container
The project files are accessible in the containerised runtime environment by means of a bind mount between the directories from the current path ($PWD) on your laptop (host) and the directories in the HOME directory at the container instance:
<ul>
<li>${PWD}/notebooks -> $HOME/notebooks</li>
<li>${PWD}/pics      -> $HOME/pics</li>
<li>${PWD}/projects  -> $HOME/projects</li>
<li>${PWD}/scripts   -> $HOME/scripts</li>
</ul>
<br>

***CAUTION***
<br>
You can remove both container and image without data loss but be aware that files removed from the container directory /project will also be removed from you host directory project.
<br>

### Scripts to use Python
Docker scripts can be found in <i>docker</i>. Each of the scripts below will call <i>docker/run/miw_container.sh</i> to facilitate the following runtimes:

<ul>

<li>

<b>REPL</b> (Read Evaluate Print Loop) modus to experimentally learn Python commands. Exit by pressing [Control+D].

```bash 
sh/python.sh
```

</li>

<li>

Start python with a <b>script</b> from directory <i>project</i>

```bash 
sh/python.sh scripts/lists/sum.py
```

</li>

<li>

Start <b>Jupyter Lab</b> to learn from the <i>notebooks</i> available at <i>project/notebooks</i>

```bash 
sh/jupyter.sh
```

</li>

<li>

Start container with an interactive <b>bash</b> (expert mode) to perform system operations

```sh
sh/bash.sh
```  

</li>

</ul>

***NOTE***
<br>
If you do not have Docker, the scripts will fall back to python and bash on your host.

### Docker artifacts
Each of the above scripts will call run/miw_container.sh which will spin up a container based on the latest version of 'jaboo/miw' which is either stored locally or will be fetched from available at [Dockerhub](https://hub.docker.com/repository/docker/jaboo/miw). 

Inspect locally stored images with
```sh
docker images
```

The containers will be removed automatically after being terminated. For overview of both running and terminated containers enter  
```sh
docker container ls -a
```

Removing images and/containers will not cause data loss. After removing the image, Docker will pull a new instance when you start a container. 
Docker images and containers can be removed (if not done automatically) by running
```sh
docker/clean_docker_artifacts.sh
```

---

### References
[How to Use Linux Terminal in Windows 10](https://allthings.how/how-to-use-linux-terminal-in-windows-10/)<br>
[Jupyter](https://jupyter.org/)<br>
[Running GUI's with Docker on OS X](https://www.youtube.com/watch?v=PKyj8sbZNYw&list=LL&index=4&t=6s)
