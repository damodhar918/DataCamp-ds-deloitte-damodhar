---
title: Introduction to Bash Scripting
tag: bash
url: https://campus.datacamp.com/courses/introduction-to-bash-scripting/
---

# 1. From Command-Line to Bash Script
## Extracting scores with shell
```bash
cat start_dir/second_dir/soccer_scores.csv | grep 1959
```

## Searching a book with shell
```bash
cat two_cities.txt | egrep 'Sydney Carton|Charles Darnay' | wc -l
```

## A simple Bash script
```bash
#!/bin/bash

# Concatenate the file
cat *.txt

# Now save and run!
```

## Shell pipelines to Bash scripts
```bash
#!/bin/bash

# Create a single-line pipe
cat soccer_scores.csv | cut -d "," -f 2 | tail -n +2 | sort | uniq -c

# Now save and run!
```

## Extract and edit using Bash scripts
```bash
#!/bin/bash

# Create a sed pipe to a new file
cat soccer_scores.csv | sed 's/Cherno/Cherno City/g' | sed 's/Arda/Arda United/g' > soccer_scores_edited.csv

# Now save and run!
```

## Using arguments in Bash scripts
```bash
# Echo the first and second ARGV arguments
echo $1
echo $2

# Echo out the entire ARGV array
echo $*

# Echo out the size of ARGV
echo $#
```

## Using arguments with HR data
```bash
# Echo the first ARGV argument
echo $1 

# Cat all the files
# Then pipe to grep using the first ARGV argument
# Then write out to a named csv using the first ARGV argument
cat hire_data/* | grep "$1" > "$1".csv
```




# 2. Variables in Bash Scripting
## Using variables in Bash
```bash
# Create the required variable
yourname="Sam"

# Print out the assigned name (Help fix this error!)
echo "Hi there ${yourname}, welcome to the website!"
```

## Shell within a shell
```bash
echo "Right now it is `date`"
```

## Converting Fahrenheit to Celsius
```bash
$ cat script.sh
# Get first ARGV into variable
temp_f=$1

# Subtract 32
temp_f2=$(echo "scale=2; $temp_f - 32" | bc)

# Multiply by 5/9 and print
temp_c=$(echo "scale=2; $temp_f2 * 5 / 9" | bc)

# Print the celsius temp
echo $temp_c

$ bash script.sh 108
```

## Extracting data from files
```bash
# Create three variables from the temp data files' contents
temp_a=$(cat temps/region_A)
temp_b=$(cat temps/region_B)
temp_c=$(cat temps/region_C)

# Print out the three variables
echo "The three temperatures were $temp_a, $temp_b, and $temp_c"
```

## Creating an array
```bash
##
# Create a normal array with the mentioned elements
capital_cities=("Sydney" "New York" "Paris")

##
# Create a normal array with the mentioned elements using the declare method
declare capital_cities=()

# Add (append) the elements
capital_cities+="Sydney"
capital_cities+="New York"
capital_cities+="Paris"

##
# The array has been created for you
capital_cities=("Sydney" "New York" "Paris")

# Print out the entire array
echo ${capital_cities[@]}

# Print out the array length
echo ${#capital_cities[@]}
```

## Creating associative arrays
```bash
##
# Create empty associative array
declare -A model_metrics

# Add the key-value pairs
model_metrics[model_accuracy]=98
model_metrics[model_name]="knn"
model_metrics[model_f1]=0.82

##
# Declare associative array with key-value pairs on one line
declare -A model_metrics=([model_accuracy]=98 [model_name]="knn" [model_f1]=0.82)

# Print out the entire array
echo ${model_metrics[@]}

##
# An associative array has been created for you
declare -A model_metrics=([model_accuracy]=98 [model_name]="knn" [model_f1]=0.82)

# Print out just the keys
echo ${!model_metrics[@]}
```

## Climate calculations in Bash
```bash
# Create variables from the temperature data files
temp_b="$(cat temps/region_B)"
temp_c="$(cat temps/region_C)"

# Create an array with these variables as elements
region_temps=($temp_b $temp_c)

# Call an external program to get average temperature
average_temp=$(echo "scale=2; (${region_temps[0]} + ${region_temps[1]}) / 2" | bc)

# Append average temp to the array
region_temps+=($average_temp)

# Print out the whole array
echo ${region_temps[@]}
```




# 3. Control Statements in Bash Scripting
## Sorting model results
```bash
# Extract Accuracy from first ARGV element
accuracy=$(grep Accuracy $1 | sed 's/.* //')

# Conditionally move into good_models folder
if [ $accuracy -ge 90 ]; then
    mv $1 good_models/
fi

# Conditionally move into bad_models folder
if [ $accuracy -lt 90 ]; then
    mv $1 bad_models/
fi
```

## Moving relevant files
```bash
$ cat script.sh
# Create variable from first ARGV element
sfile=$1

# Create an IF statement on sfile's contents
if grep -q 'SRVM_' $sfile && grep -q 'vpt' $sfile ; then
	# Move file if matched
	mv $sfile good_logs/
fi

$ bash script.sh logfiles8.txt
$ bash script.sh log1.txt
$ bash script.sh logdays.txt
```

## A simple FOR loop
```bash
# Use a FOR loop on files in directory
for file in inherited_folder/*.R
do
    # Echo out each file
    echo $file
done
```

## Cleaning up a directory
```bash
# Create a FOR statement on files in directory
for file in robs_files/*.py
do
    # Create IF statement using grep
    if grep -q 'RandomForestClassifier' $file ; then
        # Move wanted files to to_keep/ folder
        mv $file to_keep/
    fi
done
```

## Days of the week with CASE
```bash
$ cat script.sh
# Create a CASE statement matching the first ARGV element
case $1 in
  # Match on all weekdays
  Monday|Tuesday|Wednesday|Thusday|Friday)
  echo "It is a Weekday!";;
  # Match on all weekend days
  Saturday|Sunday)
  echo "It is a Weekend!";;
  # Create a default
  *)
  echo "Not a day!";;
esac

$ bash script.sh Wednesday
$ bash script.sh Saturday 
```

## Moving model results with CASE
```bash
# Use a FOR loop for each file in 'model_out/'
for file in model_out/*
do
    # Create a CASE statement for each file's contents
    case $(cat $file) in
      # Match on tree and non-tree models
      *"Random Forest"*|*GBM*|*XGBoost*)
      mv $file tree_models/ ;;
      *KNN*|*Logistic*)
      rm $file ;;
      # Create a default
      *) 
      echo "Unknown model in FILE" ;;
    esac
done
```


# 4. Functions and Automation
## Uploading model results to the cloud
```bash
# Create function
function upload_to_cloud () {
  # Loop through files with glob expansion
  for file in output_dir/*results*
  do
    # Echo that they are being uploaded
    echo "Uploading $file to cloud"
  done
}

# Call the function
upload_to_cloud
```

## Get the current day
```bash
# Create function
function what_day_is_it {

  # Parse the results of date
  current_day=$(date | cut -d " " -f1)

  # Echo the result
  echo $current_day
}

# Call the function
what_day_is_it
```

## A percentage calculator
```bash
# Create a function 
function return_percentage () {

  # Calculate the percentage using bc
  percent=$(echo "scale=2; 100 * $1 / $2" | bc)

  # Return the calculated percentage
  echo $percent
}

# Call the function with 456 and 632 and echo the result
return_test=$(return_percentage 456 632)
echo "456 out of 632 as a percent is $return_test%"
```

## Sports analytics function
```bash
# Create a function
function get_number_wins () {

  # Filter aggregate results by argument
  win_stats=$(cat soccer_scores.csv | cut -d "," -f2 | egrep -v 'Winner'| sort | uniq -c | egrep "$1")

}

# Call the function with specified argument
get_number_wins "Etar"

# Print out the global variable
echo "The aggregated stats are: $win_stats"
```

## Summing an array
```bash
# Create a function with a local base variable
function sum_array () {
  local sum=0
  # Loop through, adding to base variable
  for number in "$@"
  do
    sum=$(echo "$sum + $number" | bc)
  done
  # Echo back the result
  echo $sum
}
# Call function with array
test_array=(14 12 23.5 16 19.34)
total=$(sum_array "${test_array[@]}")
echo "The total sum of the test array is $total"
```

## Creating cronjobs
```bash
# Create a schedule for 30 minutes past 2am every day
30 2 * * * bash script1.sh

# Create a schedule for every 15, 30 and 45 minutes past the hour
15,30,45 * * * * bash script2.sh

# Create a schedule for 11.30pm on Sunday evening, every week
30 23 * * 0 bash script3.sh
```

## Scheduling cronjobs with crontab
```bash
##
$ crontab -l

##
$ crontab -e
30 2 * * * bash extract_data.sh

##
$ crontab -l
```
