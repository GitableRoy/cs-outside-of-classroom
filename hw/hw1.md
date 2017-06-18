# Homework -- Week 1 (due Tuesday, 6/20/2017)

## Homework 1.0: What do I want to do?

* Figure out what you are currently interested in as a Computer Scientist
* Put together an [elevator speech][elev-speech] for yourself (start with
freewriting)
* Estimate where you see yourself in 3 years (this does not have to be a
definitive decision -- just an idea is fine)
* List up to 10 companies/startups you are most interested in
* List up to 10 position names that suit your current interest
* For all the job postings you find, list the most common requirements

### Why is this useful?

Setting clearer career goals and asking yourself what you are interested in can
help you find direction. Recognizing common industry requirements is a good way
to understand what one should look forward to during the interview season and
how one should prepare.

## Homework 1.1: Installing Linux on a Virtual Machine

Note for Macbook users: if you _really_ want to, you may just use the OSX
terminal. You will have to make sure you learn how to use a package manager and
standard UNIX tools listed in Homework 1.3.

Unless you are using a Linux distribution already, do the following:

* Download and install [Oracle VirtualBox][vbox] (as well as the extension pack
listed on the same page)
* Download a Linux distribution of your choice
    * Recommended: [Ubuntu][ubu] (it's free -- the donation on the download
    page is optional)
    * More lightweight, if needed: [Xubuntu][xubu]
    * [More info about major Linux distributions][linux-distros]
* Try setting up the downlaoded Linux distribution on a Virtual Machine using
VirtualBox. _Note_: if VirtualBox is not allowing you to select a 32-bit OS when
creating a new Virtual Machine, make sure you enable virtualization in your
motherboard. [This][vbox-64] article describes it in slightly more deteail. If
you are still having trouble, ask for help on our Slack channel.

### Resources

* [What is Linux?][what-linux]
* [Step-by-step tutorial to set up a Ubuntu VM on Windows][win-vm-tut]

### Why is this useful?

Almost all of the major tech companies run a distribution of Linux (or some
other UNIX-like OS) on their servers. Many of their services are virtualized,
because that provides a safer and easier to maintain environment for testing,
deploying, running etc. Using Linux on a VM is a safe way to experiment without
taking chances to screw up your computer (bootloader issues, partitioning,
crashes, drivers etc.).

We will be writing and compiling code on Linux during the upcoming workshop
classes (Macbook users can stick to OSX but have to use terminal to compile).

## Homework 1.2: `git` and GitHub

* Create a GitHub profile
* Learn basic git workflow.
    * Initializing or cloning a repository
    * Checking the status, history, adding files
    * Making commits (with _useful_ commit messages!)
    * Pushing to the remote repository (in our case, on GitHub)
    * etc.

### Resources

* [Learn git branching][git-branching]
* [git - the simple guide][git-simple]
* [Try github][try-git]
* [Setting up GitHub personal access tokens][github-tokens]
* [Official git website][git-scm] (Includes the fantastic _Pro Git_ book that
is free to read online)

### Why is this useful?

`git` is the undoubdtedly most popular version control system on the planet (at
the moment, at least). Many major tech companies use it to manage their
codebases. It is a tool every modern developer should know how to use.

GitHub hosts many open-source projects managed with `git` and is the modern
"developer's portfolio" website. It contains a multitude of convenient tools
for tracking progress, setting goals/milestones, logging issues, contributing
to projects with approval etc.

We will practice using `git` and GitHub throughout this workshop to manage
group projects and contribute to these tutorials.

## Homework 1.3: Command-line interface

### UNIX Commands on `bash` Shell

Learn basic UNIX command-line workflow. You will most likely be using a BASH
shell. Make sure you understand the tools listed below (at least on a basic
level):
* Directory navigation: `cd`, `pwd`, `ls`, `mkdir`
* File creation/deletion: `touch`, `rm`
* Relative paths: `..`, `.`
* Manual pages for commands/programs/packages: `man <command>`
* Execute as root user: `sudo`
* Run commands & time them: `time`
* etc.

### Package Manager

Understand what a package manager is and how to use it (on a basic level). On
Ubuntu, the package manager is Aptitude (`apt` on command-line). On OSX, you
need to install [`homebrew`][homebrew].

Learn these commands:
* Search for a package:
    * Aptitude: `apt-cache search <name>`
    * Homebrew: `brew search <name>`
* Install a package:
    * Aptitude: `sudo apt install <name>`
    * Homebrew: `brew install <name`
* Uninstall a package:
    * Aptitude: `sudo apt purge <name>`
    * Homebrew: `brew uninstall <name>`
* Update package list (check for updates, include stuff from new repositories):
    * Aptitude: `sudo apt update`
    * Homebrew: `brew update`
* Update all packages
    * Aptitude: `sudo apt upgrade`
    * Homebrew: `brew upgrade`


### Resources

* [A Command Line Crash Course][cli-crash-course]
* [Advanced Bash-sripting guide][tldp-abs] (Only for advanced students)
* [Bash Reference Manual][bash-ref] (**read the Introduction here if you don't
know what a shell is**)

### Why is this useful?

Almost anything you can possibly do with an operating system can be achieved by
running commands on a system shell. Any modern developer should know how to use
the shell on their system.

On most modern UNIX-based systems, that shell is `bash` (**B**ourne-**a**gain
**Sh**ell). On Windows, there is `cmd` and `PowerShell` (PowerShell is more
similar to UNIX shells).

We will be using `bash` as it ships with most UNIX-like systems and outlines
the basic workflow of many other modern shells.

## Homework 1.4: Text Editor

Set up a text editor of your preference and learn how to use it. Make sure you
learn some of its major shortcuts. Download/bookmark a cheat sheet and explore
it. I recommend Atom for beginners and vim for advanced users (it will really
take some effort to learn vim). Both of those editors are free and open-source.
For practice, you can rewrite and debug programs you have already written while
doing your best to utilize shorcuts that are appropriate.

#### Atom

Installation on Ubuntu:  
 _Note:_ Atom is not included in any of the Ubuntu's `apt` repositories by
 default. There is a repository by **webupd8team** that provides it. You may
 also download the `.deb` file from the official website, but I'll leave the
 installation up to you to figure out (I showed how to do that in class).  
* Add the repository to apt: `sudo add-apt-repository ppa:webupd8team/atom`
* Refresh(update) apt's local package records: `sudo apt update`
* Install Atom: `sudo apt install atom`

#### Vim

Installation on Ubuntu: `sudo apt install vim`

Run `vimtutor` after installing for a really useful `vim` tutorial.

### Resources

* [Atom Cheat Sheet (Mac)][atom-cs-mac]
* [Atom Cheat Sheet (Linux)][atom-cs-linux]
* [Atom Flight Manual][atom-flight] (Official Atom Tutorial)
* [Vim Cheat Sheet][vim-cs]
* [Interactive vim Tutorial][openvim]

### Why is this useful?

A text editor is one of the tools that any developer will spend a great portion
of their time with. Knowing how to utilize one to its full extent can
significantly speed up the development process.

## Homework 1.5: Programming Language Revision

Revise your understanding of at least one mainstream programming language of
your choice. Review Standard I/O, File I/O, style conventions, standard library
etc. Make sure that you set up the compiler (and/or interpreter) for the
language of your choice to work on your command-line interface. If you are
using C++, you might be using `g++` or `clang++` to compile. If you are using
Java, you probably want to use `javac` to compile and `java` to run. If you are
using Python, you will probably use `python` to interpret.

If you think you're comfortable with your language, test yourself with a few
quizzes on [geeksforgeeks.org][g4g]. If you find concepts there that you
haven't heard of, search for them on the internet or ask on our Slack channel.


### Resources

* [C++ Reference][cppref]
* [Learn C++][learncpp]
* [Java 8 Documentation][javaref]
* [Python Reference][py]
* [Install Oracle Java 8 On Ubuntu][oracle-ubuntu]
* [Anaconda][conda] (Useful Python management tool / Data Science platform)

### Why is this useful?

> We must learn to walk before we can run.

Writing code is just the means of implementing whatever has been designed. That
being said, ability to write clean & correct code will lead to a much smoother
process of learning algorithms, data structures, and software development in
general.

You will write code in upcoming workshop sessions. You will also write code for
homework (a lot of it). Eliminate the language barrier before it starts biting
you.

[elev-speech]: http://sfp.ucdavis.edu/files/163926.pdf
[vbox]: https://www.virtualbox.org/wiki/Downloads
[ubu]: https://www.ubuntu.com/download/desktop
[xubu]: https://xubuntu.org/getxubuntu/
[linux-distros]: https://distrowatch.com/dwres.php?resource=major
[vbox-64]: http://www.fixedbyvonnie.com/2014/11/virtualbox-showing-32-bit-guest-versions-64-bit-host-os/
[what-linux]: https://www.linux.com/what-is-linux
[win-vm-tut]: https://www.lifewire.com/install-ubuntu-linux-windows-10-steps-2202108
[git-branching]: http://learngitbranching.js.org/
[git-simple]: http://rogerdudler.github.io/git-guide/
[try-git]: https://try.github.io/
[github-tokens]: https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/
[git-scm]: https://git-scm.com/
[bash-ref]: https://www.gnu.org/software/bash/manual/html_node/index.html
[cli-crash-course]: https://learnpythonthehardway.org/book/appendixa.html
[tldp-abs]: http://www.tldp.org/LDP/abs/html/
[homebrew]: https://brew.sh/
[atom-cs-mac]: https://blog.bugsnag.com/atom-editor-cheat-sheet/
[atom-cs-linux]: https://github.com/zyzo/atom-cheatsheet
[atom-flight]: https://flight-manual.atom.io/
[vim-cs]: https://vim.rtorr.com/
[openvim]: http://www.openvim.com/
[g4g]: http://www.geeksforgeeks.org/
[cppref]: http://en.cppreference.com/w/
[learncpp]: http://www.learncpp.com/
[javaref]: http://docs.oracle.com/javase/8/docs/
[py]: https://docs.python.org/
[oracle-ubuntu]: http://www.webupd8.org/2012/09/install-oracle-java-8-in-ubuntu-via-ppa.html
[conda]: https://www.continuum.io/Anaconda-Overview
