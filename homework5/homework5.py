#File: homework5.py

#---3 Homework 1+2 Review---
#--3.1 Vocabulary Review--
"""
1. Git vs. GitHub - Git is a terminal language used to interact with your computer while github is an online reposiory used to store and share code
2. Terminal vs. Command Line - The ternminal is the software used to interact with the computer and hte command liune is where you enter the command
3. Local vs. Remote Repository - Local repository is a storage of files saved on your own peronal device while a remote is saved on the web
4. Version Control - Trackign and following updates to version code
5. Staging Area - The area your files are in before you commit them essentially holding them as they are saved
6. git add - adds files to the staging area to then be commited
7. git commit - saves the files locally with github
8. git push - saves the files remotely in the branch your in
9. git status - shows the current status of git commands 
10. git pull - saves files from a remote repository to your local repository
11. pwd - this pritns the working directory of the directory is in
12. ls - shows all child directories and files
13. cd - used to move to a different directory
14. nano - used to create and or edit a file
15. touch - creates a file of different types
16. mv - used to move files from one directory to another
17. rm - removes a file from your computer
18. cat - displays file contents and can concatinate 2 files together
"""

#--3.2 A Direcotry Tree--
"""
• You have been plopped into Judy’s directory system. What command will tell you what your current working directory is?
pwd

• The terminal responds by saying you are in ∼/python decal/judy decal. What command will list all the files in your current working directory?
ls

• Oh no! Brianna just sent out an announcement saying that there was a typo in homework.py. You will need to pull the brianna repo repository to find the updated file. What command(s) will let you move to the correct repository and pull the latest changes?
cd ../brianna_repo
git pull origin main

• How would you move this new homework.py to the homework/ folder in your personal repository?
mv ../judy_decal/homework

• How would you move yourself to the same repository as homework.py?
cd ../jusy_decal/homework

• You want to see the contents of homework.py in your terminal, how would you do this?
nano homework.py

• Great job! You just finished the homework for this week. What command(s) allow you to save the changes and push from your local repository to your remote repository?
git add . (adds all changed files to teh staging area)
git commit -m "done with homework"
git push origin main

• Oh no! Git gave you the following error. What commands should you call to resolve this error and push your homework properly? What does the error mean? (i.e. what did “Judy” do wrong when trying to push?)
    ! [rejected] main -> main (fetch first)
    error: failed to push some refs to ’https://github.com
    /judy/judy_decal.git’
    hint: Updates were rejected because the remote contains
    work that you do
    hint: not have locally. This is usually caused by another
    repository pushing
    hint: to the same ref. You may want to first integrate
    the remote changes
    hint: (e.g., ’git pull ...’) before pushing again.
    hint: See the ’Note about fast-forwards’ in ’git push
    --help’ for details.
This error message is because Judy did not pull the changes to the remote repository meaning when she pushed it the local version pre push did not match the remote version to fix this she should use git pull
    
• What absolute path will allow you to move to Recents/?
cd ~/Pictures
"""

#---4 Homework 3 Review---
#--4.1 Data types--
def checkdatatype(input):
    return type(input).__name__

#--4.2 Conditionals--
def evenorodd(int):
    if int % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

#---5 Loops---
def sum_of_list(lst):
    count = 0
    for i in lst:
        count += i
    return count

#---6 Homework 4 Review---
#--6.1 Lists--
def duplicatelist(lst):
    new_list = []
    for i in lst:
        new_list.append(i)
        new_list.append(i)
    return new_list

#--6.2 Debugging--
def square(num): #The error was in this line as they forgot the colon
    return num*num

# print(evenorodd(2785748939034))