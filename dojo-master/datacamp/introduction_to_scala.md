---
title: Introduction to Scala
tags: scala
url: https://www.datacamp.com/courses/introduction-to-scala
---

# 1. A Scalable Language
## What is Scala?
```scala
## True
Many of Scala's design decisions aimed to address criticisms of Java.
Scala source code is intended to be compiled to Java bytecode.
Scala is a general-purpose programming language.
Scala powers some of the world's largest websites, applications, and data engineering infrastructures.
Scala executable code runs on a Java virtual machine.

## False
Scala means "fudgesicle" in Swedish.
```

## Why use Scala?
```scala
## Scalable
Lego
Scala
Farmers' market
Bazaar

## Not scalable
The Taj Mahl
Empire State Building
Cathedral
```

## What makes Scala scalable?
```scala
## Object-oriented
Every operation is a mtehotd call.
Every value is an object.

## Functional
Operations of a program should map input values to output values rather than change data in place.
Functions are first-class values.
```

## Scala is object-oriented
```scala
// lable?// Calculate the difference between 8 and 5
val difference = 8 - 5

// Print the difference
println(difference)
```

## Define immutable variables (val)
```scala
// Define immutable variables for clubs 2♣ through 4♣
val twoClubs: Int = 2
val threeClubs: Int = 3
val fourClubs: Int = 4
```

## Don't try to change me
```scala
// Define immutable variables for player names
val playerA: String = "Alex"
val playerB: String = "Chen"
var playerC: String = "Marta"

// Change playerC from Marta to Umberto
playerC = "Umberto"
```

## Define mutable variables (var)
```scala
// Define mutable variables for all aces
var aceClubs: Int = 1
var aceDiamonds: Int = 1
var aceHearts: Int = 1
var aceSpades: Int = 1
```

## You can change me
```scala
// Create a mutable variable for Alex as player A
var playerA: String = "Alex"

// Change the point value of A♦ from 1 to 11
aceDiamonds = 11

// Calculate hand value for J♣ and A♦
println(jackClubs + aceDiamonds)
```

## Pros and cons of immutability
```txt
## Pros
You have to write fewer tests.
Your code is easier to reason about.
Your data won't be changed inadvertently.

## Cons
More memory required due to data copying.
```


# 2. Workflows, Functions, Collections
## Create and run a Scala script
```txt
Open a bank file in your text editor of choice.
Write one line of code in the file: `println("Let's play Twenty-One!")`.
Save the file in your desired working directory with the name `game.scala`.
Open a command prompt. Navigate to your desired working directory, then type `scala game.scala` and click enter.
Observe `Let's play Twenty-One!` printed to output.
```

## What do functions do?
```
Functions are invoked with a list of arguments to produce a result.
```

## Call a function
```scala
// Calculate hand values
var handPlayerA: Int = queenDiamonds + threeClubs + aceHearts + fiveSpades
var handPlayerB: Int = kingHearts + jackHearts

// Find and print the maximum hand value
println(maxHand(handPlayerA, handPlayerB))
```

## Arrays
```scala
// Create and parameterize an array for a round of Twenty-One
var hands: Array[Int] = new Array[Int](3)
```

## Initialize an array
```scala
// Create and parameterize an array for a round of Twenty-One
val hands: Array[Int] = new Array[Int](3)

// Initialize the first player's hand in the array
hands(0) = tenClubs + fourDiamonds

// Initialize the second player's hand in the array
hands(1) = nineSpades + nineHearts

// Initialize the third player's hand in the array
hands(2) = twoClubs + threeSpades
```

## An array, all at once
```scala
// Create, parameterize, and initialize an array for a round of Twenty-One
val hands = Array(tenClubs + fourDiamonds,
              nineSpades + nineHearts,
              twoClubs + threeSpades)
```

## Updating arrays
```scala

// Initialize player's hand and print out hands before each player hits
hands(0) = tenClubs + fourDiamonds
hands(1) = nineSpades + nineHearts
hands(2) = twoClubs + threeSpades
hands.foreach(println)

// Add 5♣ to the first player's hand
hands(0) = hands(0) + fiveClubs

// Add Q♠ to the second player's hand
hands(1) = hands(1) + queenSpades

// Add K♣ to the third player's hand
hands(2) = hands(2) + kingClubs

// Print out hands after each player hits
hands.foreach(println)
```

## Initialize and prepend to a list
```scala
// Initialize a list with an element for each round's prize
val prizes = List(10, 15, 20, 25, 30)
println(prizes)

// Prepend to prizes to add another round and prize
val newPrizes = 5 :: prizes
println(newPrizes)
```

## Initialize a list using cons and Nil
```scala
// Initialize a list with an element each round's prize
val prizes = 10 :: 15 :: 20 :: 25 :: 30 :: Nil
println(prizes)
```

## Concatenate Lists
```scala
// The original NTOA and EuroTO venue lists
val venuesNTOA = List("The Grand Ballroom", "Atlantis Casino", "Doug's House")
val venuesEuroTO = "Five Seasons Hotel" :: "The Electric Unicorn" :: Nil

// Concatenate the North American and European venues
val venuesTOWorld = venuesNTOA ::: venuesEuroTO
```



# 3. Type Systems, Control Structures, Style
## Static typing vs. dynamic typing
```scala
## Statically-typed language
Types are checked before run time.
The type of a variable is known at compile time.
Types are checked before execution time.

## Dynamically-typed language
Types are checked during execution.
Types are checked during run time.
Types are checked on the fly.
```

## Pros and cons of static type systems
```scala
## Pros
Your program behaves as expected (i.e., prove the absence of common type-related bugs)
Safe refactorings.
Increased performance at run time.
Documentation in the form of type annotations (`: Int` in `val fourHearts: Int = 4`)

## Cons
The time it takes to check types.

## Cons addressed by Scala's type system
Code is verbose (i.e., code is longer/more annoying to write)
The language is not flexible (e.g., one strict way of composing a type)
```

## if and printing
```scala
// Point value of a player's hand
val hand = sevenClubs + kingDiamonds + threeSpades

// Congratulate the player if they have reached 21
if (hand == 21) {
    println("Twenty-One!")
}
```

## if expressions result in a value
```scala
// Point value of a player's hand
val hand = sevenClubs + kingDiamonds + threeSpades

// Inform a player where their current hand stands
val informPlayer: String = {
  if (hand > 21)
    "Bust! :("
  else if (hand == 21) 
    "Twenty-One! :)"
  else
    "Hit or stay?"
}

// Print the message
print(informPlayer)
```

## if and else inside of a function
```scala
// Find the number of points that will cause a bust
def pointsToBust(hand: Int): Int = {
  // If the hand is a bust, 0 points remain
  if (bust(hand))
    0
  // Otherwise, calculate the difference between 21 and the current hand
  else
    21 - hand
}

// Test pointsToBust with 10♠ and 5♣
val myHandPointsToBust = pointsToBust(tenSpades + fiveClubs)
println(myHandPointsToBust)
```

## A simple while loop
```scala
// Define counter variable
var i = 0

// Define the number of loop iterations
val numRepetitions = 3

// Loop to print a message for winner of the round
while (i < numRepetitions) {
  if (i < 2)
    println("winner")
  else
    println("chicken dinner")
  // Increment the counter variable
  i = i + 1
}
```

## Loop over a collection with while
```scala
// Define counter variable
var i = 0

// Create list with five hands of Twenty-One
var hands = List(16, 21, 8, 25, 4)

// Loop through hands
while (i < hands.length) {
  // Find and print number of points to bust
  println(pointsToBust(hands(i)))
  // Increment the counter variable
  i += 1
}
```

## Converting while to foreach
```scala
// Find the number of points that will cause a bust
def pointsToBust(hand: Int) = {
  // If the hand is a bust, 0 points remain
  if (bust(hand))
    println(0)
  // Otherwise, calculate the difference between 21 and the current hand
  else
    println(21 - hand)
}

// Create list with five hands of Twenty-One
var hands = List(16, 21, 8, 25, 4)

// Loop through hands, finding each hand's number of points to bust
hands.foreach(pointsToBust)
```

## Signs of style
```scala
## Imperative-style code
Type `Unit`
Side effects
`var`

## Functional-style code
No side effects
Non-`Unit` value types (e.g. `Int`)
`val`
```
