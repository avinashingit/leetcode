/**
 * @Author: Avinash Kadimisetty <avinash>
 * @Date:   2019-02-06T17:14:30-06:00
 * @Email:  kavinash366@gmail.com
 * @Project: Leetcode
 * @Filename: 58.cpp
 * @Last modified by:   avinash
 * @Last modified time: 2019-02-06T17:14:38-06:00
 * @License: MIT License
 */
 class Solution {
 public:
     int lengthOfLastWord(string s) {
         int size = s.size();
         if(size == 0) return 0;
         int i = size - 1;
         while(s[i] == ' ') {
             i--;
         }
         int length = 0;
         while(s[i] != ' ' and i >= 0) {
             length += 1;
             i--;
         }
         return length;
     }
 };
