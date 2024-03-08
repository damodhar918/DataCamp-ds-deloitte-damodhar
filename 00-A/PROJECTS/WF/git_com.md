| Command | Explanation |
| --- | --- |
| `user.name=Damodhar Jangam` | Sets the username for the Git configuration to "Damodhar Jangam". |
| `user.email=Damodhar.Jangam@ccc.com` | Sets the user email for the Git configuration to "Damodhar.Jangam@ccc.com". |
| `git config --global user.email "Damodhar.Jangam@ccc.com"` | Sets the user email for the global Git configuration to "Damodhar.Jangam@ccc.com". |
| `git config --global user.name "Damodhar Jangam"` | Sets the username for the global Git configuration to "Damodhar Jangam". |
| `git config --list` | Lists all the Git configurations. |
| `git config --local user.email ""` | Sets the user email for the local Git configuration to an empty string "". |
| `git config --local user.name ""` | Sets the username for the local Git configuration to an empty string "". |
| `git add .` | Stages all the changes made in the project. |
| `git reset --hard <SHA> && git push -f` | Hard resets the Git repository to the specific commit hash and forcefully pushes the changes to the remote repository. |
| `git revert [hash] && git push` | Reverts the specific commit and pushes the changes to the remote repository. |
| `git status` | Displays the current working status of the Git repository. |
| `git pull` | Fetches and merges the changes from the remote repository to the local repository. |
| `git commit -m` | Commits the staged changes with a message. |
| `git push` | Pushes the committed changes to the remote repository. |
| `git log` | Displays the Git commit history logs. |
| `git checkout develop` | Switches the Git branch to "develop". |
| `git pull develop` | Fetches and merges the changes from the "develop" branch of the remote repository to the local repository. |
| `git checkout FB` | Switches the Git branch to "FB". |
| `git rebase develop` | Rebases the "FB" branch onto the "develop" branch. |
| `git push` | Pushes the rebased changes to the remote repository. |