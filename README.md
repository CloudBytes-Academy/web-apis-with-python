# Starter Kit: Web APIs with Python

This is the starter kit associate with "Building Web APIs with Python" which the following version available

1. Kindle: 
2. Udemy:

## Usage Instructions

This repository contains the starter kit for each exercise in a separate branch. 

If you are unfamiliar with Git and GitHub, please read the instructions on usage below carefully and follow the steps. 

### 1. Fork to create your own copy of the repository

**Step 1**: Login to [GitHub](https://github.com) and navigate to [this repository](https://github.com/UberPython/web-apis-with-python)

```http
https://github.com/UberPython/web-apis-with-python
```

**Step 2**: Create a Fork of the repository by clicking on the fork button on top right side of the webpage as shown below

![image-20210604203326830](C:\Users\rehan\AppData\Roaming\Typora\typora-user-images\image-20210604203326830.png)

This will create a copy of the repository in your account. 

**Step 3**: Clone this new repository in your account. To Copy the Git URL press on the Green "Code" button and then click on the clipboard icon as shown below

![image-20210604204305086](C:\Users\rehan\AppData\Roaming\Typora\typora-user-images\image-20210604204305086.png)

Or you can run the following command from your terminal with Git installed, replacing "<myUserName>" with our actual GitHub username

```bash
git clone https://github.com/<myUserName>/web-apis-with-python.git
```

### 2. Navigate to the starter kit

From the terminal, run the below command to navigate to a particular branch, replace "<branch-name>" with the name of the branch (typically provided in the exercise)

```bash
git checkout <branch-name>
```

The "branch-name" should match exactly to the branch specified in the exercises. 

You should also set the upstream (online) branch by running

```bash
git push --set-upstream origin <branch-name>
```

### 3. Track the changes and push it to your repository on GitHub

This involves 4 steps.

**Step 1**: Check the changes you have made by running

```bash
git status
```

This will highlight the files that been added, deleted or changed. 

**Step 2**: Add the changes to the working tree

```bash
git add <file-name>
```

`git status` will provide you will list of files, you will need to do this with each file that has been added or changed.

**Step 3**: Record and commit the changes

```bash
git commit -m "<What changes have you done?>"
```

**Step 4**: Push your changes to GitHub (origin)

```bash
git push
```

This requires the `git push --set-upstream origin <branch-name>` completed as specified in section 2 above