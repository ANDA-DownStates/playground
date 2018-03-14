# playground
Everything but the actual analysis pipelines


# Git cheat sheet
Create 3 directories on your local machine: /data /analysis /playground
The latter two will be synced with our two github repos

Step-by-step instructions:

Go to your local folder /analysis and open the Git bash.
git init
git remote add pg https://github.com/ANDA-DownStates/analysis.git

pg will now be the name of the remote link, check this with:
git remote -v

Now its time to get the actual content of the remote repository:
git pull pg HEAD



