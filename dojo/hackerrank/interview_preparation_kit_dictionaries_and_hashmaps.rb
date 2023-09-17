##
# Hash Tables: Ransom Note
#
#!/bin/ruby

require 'json'
require 'stringio'

# Complete the checkMagazine function below.
def checkMagazine(magazine, note)
  chk1 = note - magazine == []
  chk2 = lambda do
    note_hash = note.group_by {|n| n}
    magazine_hash = magazine.group_by {|m| m}
    note_hash.keys.all? do |key|
      (magazine_hash[key].size || 0) >= note_hash[key].size
    end
  end

  puts chk1 && chk2.call ? 'Yes' : 'No'
end

mn = gets.rstrip.split

m = mn[0].to_i

n = mn[1].to_i

magazine = gets.rstrip.split(' ').map(&:to_s)

note = gets.rstrip.split(' ').map(&:to_s)

checkMagazine(magazine, note)

##
# Two Strings
#
#!/bin/ruby

require 'json'
require 'stringio'

# Complete the twoStrings function below.
def twoStrings(s1, s2)
  s1.split("") & s2.split("") != [] ? 'YES' : 'NO'
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

q = gets.to_i

q.times do |q_itr|
  s1 = gets.to_s.rstrip

  s2 = gets.to_s.rstrip

  result = twoStrings(s1, s2)

  fptr.write(result)
  fptr.write("\n")
end

fptr.close()

##
# Sherlock and Anagrams
#
#!/bin/ruby

require 'json'
require 'stringio'

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s)
  chk = lambda { |a,b| a.sort == b.sort }
  result = []

  1.upto(s.size-1) do |i|
    cmb = s.chars.each_cons(i).combination(2).to_a
    result += cmb.select do |c|
      chk.call(c[0], c[1])
    end
  end

  result.size
end

fptr = File.open(ENV['OUTPUT_PATH'], 'w')

q = gets.to_i

q.times do |q_itr|
  s = gets.to_s.rstrip

  result = sherlockAndAnagrams(s)

  fptr.write(result)
  fptr.write("\n")
end

fptr.close()
