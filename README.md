# SPOJ_history

It basically crawls through a user's page and generate a list of questions correctly answered, sorted in ascending order(according to time of submission).

Uses concept of MultiProcessing to speed up Crawling.

You need to provide your user name in file and simply open terminal and enter "python filename.py" to run the script.
There are 2 types of script, one which uses multiprocessing and one without it.

There is considerable difference in crawling using multiprocessing and without it.
Suppose you want to search history of submission for "anudeep2011", then without using multiprocessing it takes 1min 30 sec and with multiprocessing it takes 26 sec to do the same task.


NOTE : The Project is created solely for purpose of learning.

You can also use the following link : https://spojcrawl.herokuapp.com/

