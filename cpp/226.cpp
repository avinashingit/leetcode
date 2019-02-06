/**
 * @Author: Avinash Kadimisetty <avinash>
 * @Date:   2019-02-06T16:44:52-06:00
 * @Email:  kavinash366@gmail.com
 * @Project: Leetcode
 * @Filename: 226.cpp
 * @Last modified by:   avinash
 * @Last modified time: 2019-02-06T16:44:59-06:00
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
     TreeNode* invertTree(TreeNode* root) {
         inverttree(root);
         return root;
     }

     void inverttree(TreeNode* root) {
         if(root == NULL) return;
         TreeNode* temp = root->left;
         root->left = root->right;
         root->right = temp;
         invertTree(root->left);
         invertTree(root->right);
     }
 };
