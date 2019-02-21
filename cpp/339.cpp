/**
 * @Author: Avinash Kadimisetty <avinash>
 * @Date:   2019-02-21T14:02:34-06:00
 * @Email:  kavinash366@gmail.com
 * @Project: Leetcode
 * @Filename: 339.cpp
 * @Last modified by:   avinash
 * @Last modified time: 2019-02-21T14:02:53-06:00
 * @License: MIT License
 */

 /**
  * // This is the interface that allows for creating nested lists.
  * // You should not implement it, or speculate about its implementation
  * class NestedInteger {
  *   public:
  *     // Constructor initializes an empty nested list.
  *     NestedInteger();
  *
  *     // Constructor initializes a single integer.
  *     NestedInteger(int value);
  *
  *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
  *     bool isInteger() const;
  *
  *     // Return the single integer that this NestedInteger holds, if it holds a single integer
  *     // The result is undefined if this NestedInteger holds a nested list
  *     int getInteger() const;
  *
  *     // Set this NestedInteger to hold a single integer.
  *     void setInteger(int value);
  *
  *     // Set this NestedInteger to hold a nested list and adds a nested integer to it.
  *     void add(const NestedInteger &ni);
  *
  *     // Return the nested list that this NestedInteger holds, if it holds a nested list
  *     // The result is undefined if this NestedInteger holds a single integer
  *     const vector<NestedInteger> &getList() const;
  * };
  */
 class Solution {
 public:
     int depthSum(vector<NestedInteger>& nestedList) {
         int sum = 0;
         for(int i=0;i<nestedList.size();i++) {
             findSum(nestedList[i], sum, 1);
         }
         return sum;
     }

     void findSum(NestedInteger nestedList, int &csum, int depth) {
         if(nestedList.isInteger()) {
             csum += depth*nestedList.getInteger();
         }
         else {
             vector<NestedInteger> l = nestedList.getList();
             for(int i=0;i<l.size();i++) {
                 findSum(l[i], csum, depth+1);
             }
         }
     }
 };
