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