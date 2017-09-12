### Notes on if-statements & loops:
#### Rules for if-statements:    
1) **Every** *if*-statement must have an *else*!    
2) If this else should never run because it doesn't make sense, then you must use a die function in the else that prints out an error message and dies.    
3) Never nest if-statements more than two deep.   
#4) Treat if-statements like paragraphs, where *if-elif-else* grouping is like a set of sentences. Put blank lines before and after.    
5) Your boolean tests should be **simple**! If they are complex, move their calculations to variables earlier in your function and use a good name for the variable.

### Rules for Loops:
1) Use a *while* loop **only** to loop forever, and that means probably never...this only applies to python, and other languages might be different
2) Use *for*-loop for all other kinds of looping, esp. if there is a **fixed or limited** number of things to loop over

### Functions:
#### Functions do three things:
  * they name **pieces of code** the way variables name strings and numbers;  
  * they take arguments like `def print_one (arg1):`, or multiple arguments like `def print_two_again(arg1, arg2):`;  
  * you can make your own "mini-scripts" using the two features above.  
#### Create a function checklist:
1) Did you start your function definition with `def`?
2) Does your function name have only characters and _ (underscore) characters?
3) Did you put an open parenthesis ( right after the function name?
4) Did you put your arguments after the parenthesis ( separated by commas?
5) Did you make each argument unique (meaning no duplicated names)?
6) Did you put a close parenthesis and a colon **):** after the arguments?
7) Did you indent all lines of code you want in the function four spaces? No more, no less.
8) Did you "end" your function by going back to writing with no indent?
#### Use or Call a function checklist:
1) Did you call/use/run this function by typing its name?
2) Did you put the ( character after the name to run it?
3) Did you put the values you want into the parenthesis separated by commas?
4) Did you end the function call with a ) character?


### Tips for debugging:
1) The best way to debug is to use print to print out the values of variables at points in the program to see where they go wrong
2) Do **NOT** write massive files of code before you try to run them. Code a little, run a little, fix a little.


### The general workflow for designing a game program:
1) Draw a map for your game, including all the "rooms" and "traps" that the players need to go through;
2) Before coding it up, write a list of tasks you need to complete to finish the program (e.g., functions, loops, and modules required);
3) Pick the easiest thing from your to do list;
4) Write out English comments in your source file as a guide for how you would accomplish this task in your code;
5) Write some of the code under the English comments;
6) Quickly run your script so see if that code worked;
7) Repeat 4, 5, and 6 until it works;
8) Pick the next easiest task and repeat.
