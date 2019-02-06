/**
 * @Author: Avinash Kadimisetty <avinash>
 * @Date:   2019-02-06T11:35:14-06:00
 * @Email:  kavinash366@gmail.com
 * @Project: Leetcode
 * @Filename: 94.cpp
 * @Last modified by:   avinash
 * @Last modified time: 2019-02-06T11:35:31-06:00
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
     vector<int> inorderTraversal(TreeNode* root) {
         vector<int> v;
         inorder(v, root);
         return v;
     }

     void inorder(vector<int> &v, TreeNode* root) {
         if(root != NULL) {
             if(root->left != NULL)
                 inorder(v, root->left);
             v.push_back(root->val);
             if(root->right != NULL)
                 inorder(v, root->right);
         }
     }
 };
