# playground
Everything but the actual analysis pipelines


# Git cheat sheet
Create 3 directories on your local machine: /data /analysis /playground
The latter two will be synced with our two github repos

Step-by-step instructions:

Go to your local folder /playground and open the Git bash.
```
git init
git remote add pg https://github.com/ANDA-DownStates/playground.git
```

pg will now be the name of the remote link, check this with:
```
git remote -v
```

Now its time to get the actual content of the remote repository:
```
git pull pg HEAD
```

Let's create a dummy file and push it to the remote repo. 

First, create a dummy txt file in the folder /playground, then add it to our git stage (= stuff that will be part of our next commit) and commit it to our local repo.
git add dummy.txt
git commit -m 'My dummy commit'
git push -u origin master

The last part of the last line (-u origin master) is just needed the first time to tell git to which remote branch to push.
