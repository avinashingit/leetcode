/**
 * @Author: Avinash Kadimisetty <avinash>
 * @Date:   2019-02-06T16:35:56-06:00
 * @Email:  kavinash366@gmail.com
 * @Project: Leetcode
 * @Filename: 104.cpp
 * @Last modified by:   avinash
 * @Last modified time: 2019-02-06T16:36:04-06:00
 * @License: MIT License
 */

 /**
  * Definition for a binary tree node.
  * struct TreeNode {
  *     int val;
  *     TreeNode *left;
  *     TreeNode *right;
  *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
  * };
  */
 class Solution {
 public:
     int maxDepth(TreeNode* root) {
         if(root == NULL) return 0;
         else return 1 + max(maxDepth(root->left), maxDepth(root->right));
     }
 };
