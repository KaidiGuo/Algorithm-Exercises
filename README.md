Explanation inside the code. 

Key functions added in the end of each question.

For question details, please go to [Leetcode](https://leetcode.com/problemset/algorithms/)

----

1. [Breadth First Search](https://github.com/KaidiGuo/Algorithm-Exercises/tree/master/Breadth-first%20Search)
   + Easy 101 Symmetric Tree -- `[re = list(reversed(li))]`
   + Easy 107 Binary Tree Level Order Traversal II --`[results[::-1]]`
   + Easy 559 Maximum Depth of N-ary Tree
   + Medium 993 Cousins in Binary Tree
   + Medium 515 Find Largest Value in Each Tree Row --`[float('-inf')]`
   
2. [Depth First Search]()
   
   Iteration VS recursive.

   ---
   + Pre-order traversal
   + In-order traversal
   + Post-order traversal
   + Medium 200 Number of Islands 
   
3. [Hashing](https://github.com/KaidiGuo/Algorithm-Exercises/tree/master/Hashing)
   
   The use of collections.Counter() and dictionary.
   
   ---
   + Easy 884 Uncommon Words from Two Sentences -- `[collections.Counter()]`
   + Easy 387 First Unique Character in a String -- `[collections.Counter()]`--`[float('inf')]`--`[index = string.find('c')]`
   + Easy 1512. Number of Good Pairs `[math.comb(n,k)]`
   + Medium 347 Top K Frequent Elements -- `[counts = sorted(dic.values())]`
   + Easy 1 Two Sum -- `[for i,item in enumerate(nums)]`
   + Medium 3 Longest Substring Without Repeating Characters
   + Medium 146. LRU Cache -- `[collections.OrderedDict()]`--`[dict.popitem(last=False)]`
   
4. [Sliding window](https://github.com/KaidiGuo/Algorithm-Exercises/tree/master/Linked%20List)

   When to use sliding window?
   Question like:
   - "finding the substring that meet certain criterion."

   Right pointer loop through list,
      while substr does not meet criterion, do something that impact the criterion
      move left pointer
   
   ---
   + Medium 438 Find All Anagrams in a String
   + Medium 209. Minimum Size Subarray Sum
   + **Medium 904. Fruit Into Baskets**
   
5. [Linked List](https://github.com/KaidiGuo/Algorithm-Exercises/tree/master/Linked%20List)
   + Medium 2 Add Two Numbers  -- `[carry = carry//10]`
   + Medium 19 Remove Nth Node From End of List
   + Easy 21 Merge Two Sorted Lists

6. [Tree](https://github.com/KaidiGuo/Algorithm-Exercises/tree/master/Linked%20List)
   + Medium 105 Construct Binary Tree from Preorder and Inorder Traversal  -- recursive

7. [Two Pointers](https://github.com/KaidiGuo/Algorithm-Exercises/tree/master/Linked%20List)
   
   When to use two pointers?
   Question like:
   - "handle the list/string IN PLACE, I want to do something when elements meet certain criterion"
   ---
   + Medium 763 Partition Labels
   + Easy 27. Remove Element
   + Easy 283. Move Zeroes
   + Easy 844. Backspace String Compare
   + Easy 977. Squares of a Sorted Array

8. [Array-binary search](https://github.com/KaidiGuo/Algorithm-Exercises/tree/master/Linked%20List)
   + Easy 937. Reorder Data in Log Files -- `[list.sort(reverse=False, key=(key1,key2))]`
   + Easy 704. Binary Search  -- `[Binary Search]`
   + Easy 69. Sqrt(x)  -- `[Binary Search]`
   + Easy 367. Valid Perfect Square  -- `[Binary Search]`
   

