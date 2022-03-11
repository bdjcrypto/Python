To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

Welcome to Ubuntu 20.04 LTS (GNU/Linux 5.10.16.3-microsoft-standard-WSL2 x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Fri Mar 11 07:03:58 CST 2022

  System load:  0.0                Processes:             8
  Usage of /:   0.4% of 250.98GB   Users logged in:       0
  Memory usage: 2%                 IPv4 address for eth0: 172.17.137.176
  Swap usage:   0%

0 updates can be installed immediately.
0 of these updates are security updates.


The list of available updates is more than a week old.
To check for new updates run: sudo apt update


This message is shown once once a day. To disable it please create the
/home/linux_brian/.hushlogin file.
linux_brian@DESKTOP-VI7NKI3:~$ cd
linux_brian@DESKTOP-VI7NKI3:~$ pwd
/home/linux_brian
linux_brian@DESKTOP-VI7NKI3:~$ cd python_projects
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ grep Beautiful zen.txt
Beautiful is better than ugly.
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ grep beautiful zen.txt
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ grep -i beautiful zen.txt
Beautiful is better than ugly.
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ grep -o Beautiful zen.txt
Beautiful
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ grep -o is zen.txt
is
is
is
is
is
is
is
is
is
is
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ python3
Python 3.8.2 (default, Mar 13 2020, 10:14:16)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import re
>>> l = "beautiful"
>>> l = "Beautiful is better than ugly."
>>> matches = re.findall("Beautiful",l)
>>> print(matches)
['Beautiful']
>>> exit()
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ grep -i ^if zen.txt
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it's a good idea.
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ grep idea.$ zen.txt
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it's a good idea.
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ echo zen.txt
zen.txt
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ pythonc3

Command 'pythonc3' not found, did you mean:

  command 'python3' from deb python3 (3.8.2-0ubuntu2)

Try: sudo apt install <deb name>

linux_brian@DESKTOP-VI7NKI3:~/python_projects$ python3
Python 3.8.2 (default, Mar 13 2020, 10:14:16)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import re
>>> zen = """Although never is often better than right now. /
... If the implementation is hard to explain, it's a bad idea /
... If the impementation is easy to explain, it may be a good idea. /
... Namespaces are one honking great idea -- let's do more of those!"""
>>> m = re.findall("^If, zen, re.MULTILINE)
  File "<stdin>", line 1
    m = re.findall("^If, zen, re.MULTILINE)
                                          ^
SyntaxError: EOL while scanning string literal
>>> m = re.findall("^If", zen, re.MULTILINE)
>>> PRINT(M)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'PRINT' is not defined
>>> print(m)
['If', 'If']
>>> echo Two too. | grep -i t[ow]o
  File "<stdin>", line 1
    echo Two too. | grep -i t[ow]o
         ^
SyntaxError: invalid syntax
>>> exit()
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ echo Two too. | grep -i t[ow]o
Two too.
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ echo Two too. | grep -i [two]
Two too.
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ grep -i [aeiou] zen.txt
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should always be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it's a good idea.
Namespaces are one honking great idea -- let's do more of those!
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ python3
Python 3.8.2 (default, Mar 13 2020, 10:14:16)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import re
>>> string = "Two too."
>>> m = re.findall("[two]",string,re.IGNORECASE)
>>> print(m)
['T', 'w', 'o', 't', 'o', 'o']
>>> m = re.findall("t[ow]o",string,re.IGNORECASE)
>>> print(m)
['Two', 'too']
>>> echo 123 hi 34 hello. | grep [[:digit:]]
  File "<stdin>", line 1
    echo 123 hi 34 hello. | grep [[:digit:]]
         ^
SyntaxError: invalid syntax
>>> exit()
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ echo 123 hi 34 hello. | grep [[:digit:]]
123 hi 34 hello.
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ python3
Python 3.8.2 (default, Mar 13 2020, 10:14:16)
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import re
>>> line = "123?34 hello?"
>>> m = re.findall("\d",line,re.IGNORECASE)
>>> print(m)
['1', '2', '3', '3', '4']
>>> exit()
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ echo two twoo not too. | grep -o two*
two
twoo
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ echo __hello__there | grep -o __.*__
__hello__
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ echo amoeba | grep -o a.*a
amoeba
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ echo penis | grep -o e.*i
eni
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ echo I ate a pie and it was delicious. | grep -o -i i.*i
I ate a pie and it was delici
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ echo I love $ | grep \\$
I love $
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ "import this" | grep Dutch
import this: command not found
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ cat zen.txt
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should always be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it's a good idea.
Namespaces are one honking great idea -- let's do more of those!
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ cat zen.txt | grep Dutch
Although that way may not be obvious at first unless you're Dutch.
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ echo Challenge 1 Complete!
Challenge 1 Complete!
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ "Arizona 479, 501, 870. California 209, 213, 650." | grep [[:digit:]]
Arizona 479, 501, 870. California 209, 213, 650.: command not found
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ echo Arizona 479, 501, 870. California 209, 213, 650. | grep [[:digit:]]
Arizona 479, 501, 870. California 209, 213, 650.
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ echo Challenge 2 complete!
Challenge 2 complete!
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ echo The ghost that says boo haunts the loo. | grep -o .*oo
The ghost that says boo haunts the loo
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ echo The ghost that says boo haunts the loo. | grep -o .*?oo
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ echo The ghost that says boo haunts the loo, tudaloo! | grep -o .oo
boo
loo
loo
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ echo loo poo tudaloo | grep -o  .oo
loo
poo
loo
linux_brian@DESKTOP-VI7NKI3:~/python_projects$ Challenge 3 completed!
Challenge: command not found
linux_brian@DESKTOP-VI7NKI3:~/python_projects$