DEPLOYMENT INSTRUCTIONS
------

Deploy to Dev:
git push heroku <branchname>:master
or
git push heroku master

Deploy to Production:
1.  a. !!IMPORTANT!! Set 
        DEBUG = False
    in config.py
        ANALYTICS = True
    b. delete comments out of code
    c. delete unusable navbar pieces
    d. remove endpt code for unreachable endpts 
2.  Commit and push changes to repo
3.  ssh into rnd at ocf
        ssh rnd@ssh.ocf.berkeley.edu
4.  update website repo
    note that while on master, people can see master.
    
        git checkout master
        git pull
        git checkout --track origin/coming-soon-1.03a-deploy
        git checkout <version name>
        git pull
5.  check rnd.berkeley.edu to see if changes are there.
    make sure the branch is the correct version


DATABASE NOTES
------

If you do not yet have a database, you will need to:
Open an interactive python2.7 shell in the base directory and run:
>>> from rndapp import init_db
>>> init_db()

THIS WILL ERASE THE CURRENT DATABASE. The repo should have a development database already in it.

