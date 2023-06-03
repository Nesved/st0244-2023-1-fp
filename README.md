# st0244-2023-1-fp
Members: NESVED LONDOÑO QUINTERO 
Operatyng System: Windows 11 Pro 21H1 
Python version: 3.10
This code implements a unification algorithm in Python. The algorithm takes a list of 
constraints and tries to find a solution that unifies all the constraints.

The unification algorithm is used in the field of logic programming and type inference 
to find variable assignments that make the constraints true. In this case, the constraints 
are types, and the goal is to find a type assignment that is compatible.

The code consists of several functions:

The unify(C) function implements the unification algorithm. It takes a list of constraints 
C and returns a list of unifications if the constraints can be unified, or an error message 
if it's not possible. The function uses recursion to solve the constraints one by one.

The apply_substitution(substitution, term) function applies a substitution to a term. It 
takes a substitution dictionary and a term and returns the term with the substitution applied. 
The term can be a variable (represented as a string) or a tuple of terms.

The FV(term) function returns the free variables in a term. It takes a term and returns a set 
of free variables.

The is_valid_type(type_str) function checks if a string represents a valid type. It checks 
if the type is "Nat" or "Bool" or if it matches the pattern of a variable or a type function.

The parse_type(type_str) function parses a string and returns the corresponding type. It 
recognizes the types "Nat" and "Bool" and the pattern of variables and type functions.

The get_subconstraints(S, T) function returns the sub-constraints of two terms. It takes 
two terms and returns a list of sub-constraints, which are pairs of terms.

The read_constraints(filename) function reads the constraints from a text file. The file should 
have one constraint per line in the format "type1 = type2". The function returns a list of 
constraints.

The format_unifications(unifications) function formats the unifications into a readable list. 
It takes a list of variable-value pairs and returns a list of formatted strings in the format 
"variable -> value".

The main() function is the main function of the program. It prompts the user for the name of a 
file that contains the constraints, reads the constraints from the file, calls the unify function 
to solve the constraints, and displays the result.

The program is executed by calling the main() function if it is run directly as a script, i.e., 
if the file is executed and not imported as a module in another program.
