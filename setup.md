# Setup
## python system
### pyenv
   1. Installing zsh
      - for window users, first install git for windows (see the git section), git for window comes with bash, then install zsh, see https://dominikrys.com/posts/zsh-in-git-bash-on-windows/
   2. Installing pyenv
       - https://www.newline.co/courses/create-a-serverless-slackbot-with-aws-lambda-and-python/installing-python-3-and-pyenv-on-macos-windows-and-linux
   3. Setting up pyenv location
      - put the following lines into ~/.zshrc
        ```console
        export PYENV_ROOT=/Volumes/m2.wd.black.sn850.1/dev/pyenv/
        export PATH="$(pyenv root)/shims:$PATH"
        eval "$(pyenv virtualenv-init -)"
        ```
       here /Volumes/m2.wd.black.sn850.1/ is the location for the external storage device under macos, for other system or device, replace this with repect to the correct address.
       - under zsh, execute the following commands:
            ```console
            % pip3 install virtualenv
            % pip3 install virtualenvwrapper
            % brew install pyenv-virtualenv
            ```
        for the last command, this is for mac, not sure how to do it under windows. The corresponding command for linux will be added later.
   4. Installing python with a given version: to install version 3.10, here is the command
      ```console
      % pyenv install 3.10
      ```
      To use this version globally, one can do the following:
      ```console
      % pyenv global 3.10
      ```
   5. Setting up project environment
      - To assign a python version to a environment name, the syntax is as follows
         ```console
         % pyenv virtualenv [python version] [environment name]
         ```
         As an example, to assign python 3.7 (you need to install version 3.7 first by using "pyenv install 3.7") to an environment name python3.7:
         ```console
         % pyenv virtualenv 3.7 python3.7
         ```
      - %o assign a project with a given environment:
         ```console
         % cd [project dir]
         % pyenv local [environment name]
         ```
         Following the example above, assign the python3.7 environment to project projects/ts/wavelet/tf:
         ```console
         % cd projects/ts/wavelet/tf:wq
         
         % python local python3.7
         ```
         In this way, different projects can use different python versions.

### Setting up project environment
   1. Installing jupyter notebook
   2. Installing required packages
      ```bash
      pip install -r requirements.txt
      ```

### Running jupyter notebook
```bash
./runjnb.sh
```

## vscode
### Terminal
How to set up terminal using zsh: bring up command pallete, find "Terminal Default Profile", choose zsh.

### devcontainer

## Git
### Window 11
   - https://www.windows11.pro/5639.html
   - https://git-scm.com/download/win
### MacOS
   - https://git-scm.com/download/mac
### Linux
   - https://git-scm.com/download/linux
## Docker
