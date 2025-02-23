### MacOS

___

#### Install Homebrew + XCode

1. Install homebrew: via `https://www.youtube.com/watch?v=UBdiA0SJqLE`
2. Go to the Homebrew landing page to get an installation command
3. Copy some output of that command to make sure your ~/.zprofile, ~/.zshrc , or ~/.bash_profile correctly initializes
   the brew command whenever you start a new terminal session.
4. Run xcode-select --install to make sure certain Xcode dependencies are installed. Without this step, there are many
   things you will not be able to successfully install with Homebrew.

#### Install iTerm2 Terminal

1. Download it from the iTerm2 homepage or by running brew install --cask iterm2.
2. Open the iTerm2 application to validate that you installed it correctly.
3. Familiarize yourself with the benefits of iTerm two by watching this: `https://www.youtube.com/watch?v=P-Etw6aa2cY`

### Multiple Python versions

1. Navigate `https://github.com/pyenv/pyenv?tab=readme-ov-file#macos`
2. Add commands: `https://github.com/pyenv/pyenv#set-up-your-shell-environment-for-pyenv`
3. Run: `brew install openssl readline sqlite3 xz zlib tcl-tk`
4. Navigate and Install for MacOS: `https://github.com/pyenv/pyenv/wiki#suggested-build-environment`
   `

* `pyenv version` - Show the current Python version(s) and its origin
* `pyenv versions` - List all Python versions available to pyenv
* `pyenv install --list` - Show the versions we can install
* `pyenv install --list | wc -l` - Count the total versions we can install
* `pyenv install [someversion]` - Install the Python's version on pyenv
* `pyenv shell [someversion]` - Switch between versions local terminal-shell
* `pyenv global [someversion]` - Switch between version globally all terminals
* `python --version` - See the current python version that run