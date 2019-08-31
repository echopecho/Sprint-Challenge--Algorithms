#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) If the while state were just 'a < n' that would bring the runtime to O(n), but in this problem n is multiplied by itself 3 times. The while loop will run n^3 times with respect to n, so that would bring it out to O(n^3). The setting of a in the first and third lines both just have a runtime of O(1), so they can be disregarded. Even though we are doing a calculation of n \* n, that operation is constant.

b) The runtime for this function would be O(n \* log(n)). The for loop will have a runtime of O(n) as that just iterates through every integer up to n. The while loop will step through j at a rate of 2 times what ever the previous value of j was. This will end up getting to n at an exponential rate. That rate is calculated but the inverse operator of exponent of base 2 (i.e. log base2 of n).

c) This would just be a runtime of O(n). The recursive case only calls itself one time, so the number of times is related directly to the number of bunnies (or n).

## Exercise II

To minimize the number of eggs used and lost we should start in the middle of the building floor(n / 2). If the egg breaks then we know we need to go lower and higher if it doesn't. Whichever way we go, we then divide the number of remaining floors in half and test from that floor. We continue repeating this process until dividing the number of floors is less than 1. The runtime of this would be O(log(n)).
