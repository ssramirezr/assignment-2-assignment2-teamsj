# Assignment 2 - Formal Languages And Compilers

**Group members:** Juan José Gómez Vélez and Santiago Manco Maya

The assignment was to implement the Cocke-Kasami-Younger (CKY) algorithm presented in Kozen, Lecture 27.

Given a context-free grammar G = (N, Σ, P, S) in Chomsky normal form (CNF) and a string x ∈ Σ∗, the CKY algorithm decides whether or not x ∈ L(G).

## Versions and Programming Language

**Version of the OS used:** Windows 11.

**Programming Language:** Python 3.10.12

**Tools:** IDE Visual Studio Code

## Instructions for running the implementation

**1.** Download the cky.py file.

**2.** Use the cd command in the console to access the folder where the file cky.py is located.

**3.** Run the cky.py file by using the next command:
```
py cky.py
```
**4.** The program will print ‘yes’ when a string is generated by the grammar G, it prints ‘no’ otherwise. For example:
```
3   
5 5
S AB BA SS AC BD
C SB
D SA
A a
B b
aabbab
yes
aabb
yes
ab
yes
aa
no
b
no
4 3
S AB AC SS
C SB
A a
B b
abab
yes
aaabbbaabbab
yes
aabab
no
2 6
S AS b  
A a
ab           
yes
aaaaaaaa
no
aaaaaaaaaaab
yes
b
yes
bb
no
abb
no
```


[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/ktyD1gKg)
