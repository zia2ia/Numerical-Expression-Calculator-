# Numerical-Expression-Calculator

## This project implements a Python-based infix-to-postfix expression calculator while handling expression validation.

This command-line application is designed to process and evaluate mathematical expressions inputed by the user. The project is structured around two primary classes: the Stack class and the Calculate class. 

Stack class: Provides the foundational data structure with its most basic operations necessary to be used in validating the parentheses of the expression, converting from infix to postfix, and evaluating the postfix expression. 

Calculate Class: Handles the core functionality of the program. It validates the input expression, ensuring no missing or unmatched parentheses pairs and that the expression is syntactically sound. While also handling more specific edge cases. The program will repeat until a valid expression is given and will output why an expression is considered invalid. Once validated, the expression is converted into postfix notation while handling implicit multiplication if found. Finally, the class calculates the result of the newly converted postfix expression.

## Installation Instructions 

1. The best way to install and use this program would be to access the file submitted under this repository named "Python_Project_PostfixCaclulator.py".
2. Then to rather download or copy the raw file.
3. Make sure Python (version 3.x is recommended) and a source code editor are installed.
4. Then paste it or upload it into any file in your source code editor.
5. Enter the correct file path in bash and then run the program.
6. Interact with it through the command line.

## Usage

This project is designed exclusively for calculating numerical expressions. To ensure proper functionality, include spaces between every character in the expression. Examples of valid expressions include 3 ^ 9, 4 ( 9 / 3 ), or ( 8 + 7 ) * 4 { 1 - 9 }.

The program validates all expressions to confirm they are correctly formatted. No calculations will be performed until a valid expression is entered. Examples of invalid expressions include ( a + 9 ), + ( 9 - 2 ), or 4 ( 9 9 ) / 0. The program will prompt the user to correct any errors before proceeding with the calculation. 


