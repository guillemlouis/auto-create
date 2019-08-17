# Auto create
This project automatically creates everything you need to start your project : 
* navigates to you chosen directory
* creates a new folder named after your project
* creates and initiates a github repo with the github API

**this script has only been tested on MacOS, should work on all UNIX based OS**

# Set up

  ## Clone this repo
  ```
  git clone https://github.com/guillemlouis/auto_create
  ```
  ## Install the dependencies for the script
  ```
  pip install -r dependencies.txt

  ```

  ## Change the paths/logins on the scripts
    Go inside the script and change the location in which you want your projects to be created and the logins to use. 
    ### Create a git token. 
    * Go to https://github.com/settings/tokens
    * Create a token and check "repo" for the scope
    * Generate the token
    * Copy/paste it to the script
  ## Add the script to your aliases
  This is for MacOS especially because it does not load .bashrc by default.
  ```
  echo "alias create='python ~/Dev/auto_create/create.py'" >> ~/.bash_profile
  ```
