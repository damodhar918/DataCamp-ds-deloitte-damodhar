#!/bin/bash ----> hash bang

pwd -- current path
ls --  list of files in current path


Save the above content and make the script executable −

$chmod +x test.sh
The shell script is now ready to be executed −

$./test.sh --- to execute program  in current dir


"""
 echo "What is your name?"
read PERSON
echo "Hello, $PERSON"
"""

VAR1="Zara Ali"
VAR2=100


readonly, unset

$./test.sh Zara Ali

#!/bin/sh

echo "File Name: $0" -- ./test.sh
echo "First Parameter : $1" -- Zara
echo "Second Parameter : $2" -- Ali
echo "Quoted Values: $@" -- Zara Ali
echo "Quoted Values: $*" -- Zara Ali
echo "Total Number of Parameters : $#" --2

$./test.sh Zara Ali 10 Years Old

#!/bin/sh

for TOKEN in $*
do
   echo $TOKEN
done

$0 -- The filename of the current script.
$n -- These variables correspond to the arguments with which a script was invoked. Here n is a positive decimal number corresponding to the position of an argument (the first argument is $1, the second argument is $2, and so on).
$# -- The number of arguments supplied to a script.
$* -- All the arguments are double quoted. If a script receives two arguments, $* is equivalent to $1 $2.
$@ -- All the arguments are individually double quoted. If a script receives two arguments, $@ is equivalent to $1 $2.
$? -- The exit status of the last command executed.
$$ -- The process number of the current shell. For shell scripts, this is the process ID under which they are executing.
$! -- The process number of the last background command.

echo $?   -- 0 or any no.


NAME[0]="Zara"
NAME[1]="Qadir"
NAME[2]="Mahnaz"
NAME[3]="Ayan"
NAME[4]="Daisy"
echo "First Index: ${NAME[0]}"
echo "Second Index: ${NAME[1]}"
echo "First Method: ${NAME[*]}"
echo "Second Method: ${NAME[@]}"

$ ./shell.txt
First Index: Zara
Second Index: Qadir
First Method: Zara Qadir Mahnaz Ayan Daisy
Second Method: Zara Qadir Mahnaz Ayan Daisy

Operator			Description															Example
+ (Addition)		Adds values on either side of the operator							`expr $a + $b` will give 30
- (Subtraction)		Subtracts right hand operand from left hand operand					`expr $a - $b` will give -10
* (Multiplication)	Multiplies values on either side of the operator					`expr $a \* $b` will give 200
/ (Division)		Divides left hand operand by right hand operand						`expr $b / $a` will give 2
% (Modulus)			Divides left hand operand by right hand operand and returns rem		`expr $b % $a` will give 0
= (Assignment)		Assigns right operand in left operand								a = $b would assign value of b into a
== (Equality)		Compares two numbers, if both are same then returns true.			[ $a == $b ] would return false.
!= (Not Equality)	Compares two numbers, if both are different then returns true.		[ $a != $b ] would return true.

Operator	Description	Example
-eq	Checks if the value of two operands are equal or not; if yes, then the condition becomes true.											[ $a -eq $b ] is not true.
-ne	Checks if the value of two operands are equal or not; if values are not equal, then the condition becomes true.							[ $a -ne $b ] is true.
-gt	Checks if the value of left operand is greater than the value of right operand; if yes, then the condition becomes true.				[ $a -gt $b ] is not true.
-lt	Checks if the value of left operand is less than the value of right operand; if yes, then the condition becomes true.					[ $a -lt $b ] is true.
-ge	Checks if the value of left operand is greater than or equal to the value of right operand; if yes, then the condition becomes true.	[ $a -ge $b ] is not true.
-le	Checks if the value of left operand is less than or equal to the value of right operand; if yes, then the condition becomes true.		[ $a -le $b ] is true.

[ $a <= $b ] is correct whereas, [$a <= $b] is incorrect.

Operator	Description	Example
!	This is logical negation. This inverts a true condition into false and vice versa.						[ ! false ] is true.
-o	This is logical OR. If one of the operands is true, then the condition becomes true.					[ $a -lt 20 -o $b -gt 100 ] is true.
-a	This is logical AND. If both the operands are true, then the condition becomes true otherwise false.	[ $a -lt 20 -a $b -gt 100 ] is false.

Operator	Description	Example
=	Checks if the value of two operands are equal or not; if yes, then the condition becomes true.					[ $a = $b ] is not true.
!=	Checks if the value of two operands are equal or not; if values are not equal then the condition becomes true.	[ $a != $b ] is true.
-z	Checks if the given string operand size is zero; if it is zero length, then it returns true.					[ -z $a ] is not true.
-n	Checks if the given string operand size is non-zero; if it is nonzero length, then it returns true.				[ -n $a ] is not false.
str	Checks if str is not the empty string; if it is empty, then it returns false.									[ $a ] is not false

Operator	Description	Example
-b file	Checks if file is a block special file; if yes, then the condition becomes true.										[ -b $file ] is false.
-c file	Checks if file is a character special file; if yes, then the condition becomes true.									[ -c $file ] is false.
-d file	Checks if file is a directory; if yes, then the condition becomes true.													[ -d $file ] is not true.
-f file	Checks if file is an ordinary file as opposed to a directory or special file; if yes, then the condition becomes true.	[ -f $file ] is true.
-g file	Checks if file has its set group ID (SGID) bit set; if yes, then the condition becomes true.							[ -g $file ] is false.
-k file	Checks if file has its sticky bit set; if yes, then the condition becomes true.											[ -k $file ] is false.
-p file	Checks if file is a named pipe; if yes, then the condition becomes true													[ -p $file ] is false.
-t file	Checks if file descriptor is open and associated with a terminal; if yes, then the condition becomes true.				[ -t $file ] is false.
-u file	Checks if file has its Set User ID (SUID) bit set; if yes, then the condition becomes true.								[ -u $file ] is false.
-r file	Checks if file is readable; if yes, then the condition becomes true.													[ -r $file ] is true.
-w file	Checks if file is writable; if yes, then the condition becomes true.													[ -w $file ] is true.
-x file	Checks if file is executable; if yes, then the condition becomes true.													[ -x $file ] is true.
-s file	Checks if file has size greater than 0; if yes, then condition becomes true.											[ -s $file ] is true.
-e file	Checks if file exists; is true even if file is a directory but exists.													[ -e $file ] is true.

#!/bin/sh

a=10
b=20

if [ $a == $b ]       
then
   echo "a is equal to b"
elif [ $a -gt $b ]
then
   echo "a is greater than b"
elif [ $a -lt $b ]
then
   echo "a is less than b"
else
   echo "None of the condition met"
fi


#!/bin/sh

FRUIT="kiwi"

case "$FRUIT" in
   "apple") echo "Apple pie is quite tasty." 
   ;;
   "banana") echo "I like banana nut bread." 
   ;;
   "kiwi") echo "New Zealand is famous for kiwi." 
   ;;
esac

#!/bin/sh

option="${1}" 
case ${option} in 
   -f) FILE="${2}" 
      echo "File name is $FILE"
      ;; 
   -d) DIR="${2}" 
      echo "Dir name is $DIR"
      ;; 
   *)  
      echo "`basename ${0}`:usage: [-f file] | [-d directory]" 
      exit 1 # Command to come out of the program with status 1
      ;; 
esac 


#!/bin/sh

a=0
while [ "$a" -lt 10 ]    # this is loop1
do
   b="$a"
   while [ "$b" -ge 0 ]  # this is loop2
   do
      echo -n "$b "
      b=`expr $b - 1`
   done
   echo
   a=`expr $a + 1`
done

#!/bin/sh

NUMS="1 2 3 4 5 6 7"

for NUM in $NUMS
do
   Q=`expr $NUM % 2`
   if [ $Q -eq 0 ]
   then
      echo "Number is an even number!!"
      continue
   fi
   echo "Found odd number"
done

Sr.No.	Escape & Description
\\ -- backslash
\a -- alert (BEL)
\b -- backspace
\c -- suppress trailing newline
\f -- form feed
\n -- new line
\r -- carriage return
\t -- horizontal tab
\v -- vertical tab


Sr.No.	Form & Description
${var} -- Substitute the value of var.
${var:-word} -- If var is null or unset, word is substituted for var. The value of var does not change.
${var:=word} -- If var is null or unset, var is set to the value of word.
${var:?message} -- If var is null or unset, message is printed to standard error. This checks that variables are set correctly.
${var:+word} -- If var is set, word is substituted for var. The value of var does not change.


VAR=ZARA
echo "$VAR owes <-\$1500.**>; [ as of (`date +%m/%d`) ]"
ZARA owes <-$1500.**>; [ as of (03/11) ]


DATE=`date`
echo "Current Date: $DATE"
Current Date: Sat Mar 11 11:56:05 IST 2023


who 

echo line 1 > users -- over ride
echo line 2 >> users -- append
wc -l users 
wc -l < users


command << delimiter
document
delimiter


$wc -l << EOF
   This is a simple lookup program 
	for good (and bad) restaurants
	in Cape Town.
EOF
3


Sr.No.	Command & Description
pgm > file -- Output of pgm is redirected to file
pgm < file -- Program pgm reads its input from file
pgm >> file -- Output of pgm is appended to file
n > file -- Output from stream with descriptor n redirected to file
n >> file -- Output from stream with descriptor n appended to file
n >& m -- Merges output from stream n with stream m
n <& m -- Merges input from stream n with stream m
<< tag Standard input comes from here through next tag at the start of line <<
| -- Takes output from one program, or process, and sends it to another

# Calling one function from another
number_one () {
   echo "This is the first function speaking..."
   number_two
}

number_two () {
   echo "This is now the second function speaking..."
}

# Calling function one.
number_one

This is the first function speaking...
This is now the second function speaking...

unset -f function_name


echo "This is Unix" | sed "s/Unix/Linux/"
This is Linux

sed "s/Unix/Linux/" path > new


grep -->  find in file.
grep [OPTIONS] PATTERN [FILE...]
grep "ERROR" log.txt  --  find lins which have the value "ERROR"
grep -i "ERROR" log.txt  --  find lins which have the value "ERROR" with ignore case
grep -v "INFO" log.txt -- inverser of above onw
grep -A 5 ERROR log.txt
grep -B 5 ERROR log.txt
grep -C 5 ERROR log.txt


sed --> It’s a more powerful tool than grep as it offers more options for text processing purposes, including the substitute command, which sed is most commonly known for.
sed [OPTIONS] SCRIPT FILE... --->substitute command
sed -n '/ERROR/ p' log.txt --> grep "ERROR" log.txt 
's/pattern/replacement/' --> Substituting Matched String With Replacement
sed 's/ERROR/CRITICAL/' log.txt  --> replacement
sed -ibackup 's/ERROR/CRITICAL/' log.txt
sed '3 s/ERROR/CRITICAL/' log.txt -->  only applies to 3rd line
sed '3,5 s/ERROR/CRITICAL/' log.txt -- > can applay b/w
sed -n '3,/ERROR/ p' log.txt --> regrex pattern.


awk -->It not only offers a multitude of built-in functions for string, arithmetic, and time manipulation but also allows the user to define his own functions just like any regular scripting language
awk [options] script file ---->  
'(pattern){action}' 
awk '/ERROR/{print $0}' log.txt
awk '{gsub(/ERROR/, "CRITICAL")}{print}' log.txt
awk 'BEGIN {print "LOG SUMMARY\n--------------"} {print} END {print "--------------\nEND OF LOG SUMMARY"}' log.txt
awk '{print $1, $2}' log.txt
awk -F "," '{print $1, $2}' log.txt
awk '{count[$2]++} END {print count["ERROR"]}' log.txt
awk '{ if ($1 > 1598863888 ) {print $0} }' log.txt\





ls <dir name>-- list
ls ~ list home directory
ls -ltr -- detailed list “ltr” stands for l- long listing, t- time, r- recursive.

df -- sisk filesystem
df -h "-h" human readable form

mkdir <new dir name> --  create a new directory
rmdir <dir name> --  create a new directory
rm <file name> --  create a new directory
pwd  --- “Present Working Directory”

cd -- change directory
cd / --root directory of users Linux filesystem
cd ~ --home directory of the user.
cd.. --nav one directory level up 
cd - --nav previous directory or simply go one directory back to the directory which user visited
clear -- clear console screen
mv <old> <new> -- move a particular file/directory from one place to another or rename file
cp <old> <new> -- copy " "
cat <file name> --  ouput of file
du -- “Disk Utility”.
du -sh (“-s”= Summary and “-h”= Human Readable)
touch <file name> - empty file will create
who -- no. users
echo -- to display typed or stored data
date -- current day and time on the Linux termina

gzip filename -- compress
touch filename
locate filename
echo String
grep “String” filename
grep "String" filename1 filename2
$ clear
$ logout
exit
wc [-l/-w/-c] filename
sort [-u/-n] filename
kill -- stop
ps -ax detailed information like CPU usage, user id, command name and memory usage.
uptime 
sleep number [suffix] 
sleep no [_/m/d] -- sec/min/days
seq n1 n2 -- Prints number starting from n1 to n2.
$ cut c(n) filename
$ cut -c(n), (n) file.txt
$ paste filename
$ paste filename1 filename2
cal -- calendar
uniq filename -- one unique lines
$ uniq -c filename
$ uniq -d filename

du - disk usage
du -a/-h
find ./dir_name - search current and substitute
diff filename1 filename2
join filename1 filename2
split -l/-b filename

hostname -domputer name
rev String
$ tar -czvf archivename.tar.gz /path/to/directory or file
-c: Creates an archive.
-z: Compresses the archive with gzip.
-v: Display progress in the terminal while creating the archive. v is always optional in these Linux commands.
f: Allows you to specify the filename of the archive.
$ tar -xzvf archive.tar.gz
-x extract

sudo apt-get install --apt-get is the command-line tool for working with APT software 
sudo apt-get update/upgrade
which filename -- It takes one or more arguments where for each of its arguments it prints the full path of the executable.
filename -version
top filename
who
tail filename -n 1000
head filename
head -n myfile.txt














