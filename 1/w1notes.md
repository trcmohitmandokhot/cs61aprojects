# CS 61A FALL 2019 Notes
[cs61a-fall2019](https://inst.eecs.berkeley.edu/~cs61a/fa19/)
Notes.

## Lecture 1

Review language in composing programs [Sec1.2](https://composingprograms.com/pages/12-elements-of-programming.html). The language describes three key elements of a programming language.
- Ability to provide primitive building blocks
- Abstraction
- Ability to build up on abstraction by combination

An expression contains an *operator* and *operands*.   
An expression is evaluated by an interpretor using an evaluation procedure.  
*Evaluation Procedure of an Expression:*
1) Identify the function referred to by the operator. Identify the operands as arguments.
2) Apply the function to the arguments.
**Everything is an expression.** Expressions -> sub-expressions.

A programming language works like this: *Interpret expression by applying the evaluation proceedure repeatedly*

Expression Tree: A technique to visualize the computing procedure and its outcomes. 

## Lecture 2
The composing programs book code executor is [online](http://pythontutor.com/composingprograms.html#mode=edit)
An alternative online interpretor is [code.cs61a.org](https://code.cs61a.org/)
I like the first option better for simpler programs and drawing environment diagrams.   

Names: A variable name may refer to a built-in function, or other functions imported from modules, unless defined explicitly by the user.

Environment Diagrams: *A technique to track execution of a program in an environment, which can have multiple frames.*  
- Global Frame
- A local frame, followed by the global frame.

A user defined function is made up of two facets. The "def" expression and the "call" expression. 
*Execution procedure for the "def" expression*
1) Create a function (where?) using the defined signature
2) Abstract(?) the lines of code inside the indent in an executable block
3) Bind the value of function to name of function in global frame
*Execution procedure for the "call" expression*
1) Create a local frame (f1,f2,...)
2) Assign the value of the passed argument to formal parameter
3) Execute code block and return value

**Expression and Environments VIMP(Why?)**
1) An environment is a sequence of frames.
2) A name evaluates to the value bound to that name, in the earliest frame of the current environment in which that name is found. (Very confusing)

