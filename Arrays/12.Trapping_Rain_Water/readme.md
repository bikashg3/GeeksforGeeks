# Trapping Rain Water



Given n non-negative integers in array representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example:

Input:

3

2 0 2

Output:

2

Structure is like below

|   |

| _ |


We can trap 2 units of water in the middle gap.




Input:

The first line of input contains an integer T denoting the number of test cases. The description of T test cases follows.

Each test case contains an integer N followed by N numbers to be stored in array.


Output:

Print trap units of water in the middle gap.



Constraints:

1<=T<=100

3<=N<=100

0<=Arr[i]<10



Example:

Input:

2

4

7 4 0 9

3

6 9 9



Output:

10

0

