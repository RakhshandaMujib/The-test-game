# The-test-game
Remember the test game we played in middle school- where we’d just write a statement or a question, cancel letters, add some numbers and finally come up with a percentage that would support or answer the same?</br>
No?</br>
Here’s a recap.</br></br>
Suppose, I’m asking: “**IS PROGRAMMING SILLY GAMES OKAY?**”</br>
The steps to come up with an answer (just for the fun of it) are as follows:</br></br>
•	**Step 1:** Moving from left to right, count the number of occurrences for each letter that we come across in the question. 
So, to start with we’ll have 3 ‘I’s followed by 3 ‘S’s and so on and so forth till we cancel all the letters and get a list of numbers (the counts of each letter). </br>
For our example we’ll have something like this:</br>
	  I: 3, S: 3, P: 1, R: 2, O: 2, G: 3, A: 3, M: 3, N: 1, L: 2, Y: 2, E: 1, K: 1</br>
	  3, 3, 1, 2, 2, 3, 3, 3, 1, 2, 2, 1, 1</br>
*Note: For every count >= 10 we’ll have to split the number into single digits. So, in case a letter X had 13 occurrences, our list would have 1 and 3 as separate digits. This rule will be followed in all the subsequent steps. In other words, no two or more digit numbers are allowed, if found, we split them into numbers of single digits* </br>
•	**Step 2:** Add the first number to the last; the second to the second last, third to the third last and so on till all the numbers have been added. We not the sum and derive our new list. In case, the total number of digits is odd, the middle number in the list is carried on with the new list. </br>
So, for our list of numbers the new list is: </br>
	  4, 4, 3, 4, 3, 6, 3</br>
•	**Step 3:** We repeat the above process till we reach a list with only 2 numbers or a list that has 1, 0, and 0 as its digits.
Thus, we shall have the following result:</br>
    7, 1, 0, 6, 4</br>
    1, 1, 7, 0</br>
    1, 8</br></br>
In either case, the digits we are left, when combined to form a single number is the final result. So, in our case, we’re 18% positive that programming silly games is okay.</br></br>

Too bad!</br>
But, it’s okay as long as we enjoyed coding the same, right? </br>
Have fun!</br></br>

*P.S.: Like all other games, there is nothing to be serious about the results. It is just a silly game.* =)
