# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.) 

> > Command | Description
> > ------- | ----------
> > pwd | Show current working directory path
> > mkdir | Create a directory
> > rmdir | Delete a directory
> > touch filename | Create a file using the `touch` command
> > rm | Delete a file
> > mv oldfilename newfilename | Rename old file name to new file name
> > ls -a | List hidden files
> > cp | Copy a file from one directory to another
> > find | Find a file
> > hostname | Show my computer's network name

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > Command | Description
> > ------- | ----------
> > ls | List files
> > ls -a | List hidden files
> > ls -l | List files in long format
> > ls -lh | List files in long format with readable file size
> > ls -lah | Lists all files in human readable format
> > ls -t | List files sorted by date and time
> > ls -Glp | List files in long format and directories as /

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > My favorites are `ls-lh` `ls -p` `ls -p1` `ls -R` `ls -a`

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs reads data from standard input and allows you to use standard input in commands that otherwise can't support it. One example of how to use it would be to enhance the find and remove commands. You can first find all files that meet a certain criteria (e.g. end in .txt) and then use the xargs command to delete all files found.

 

