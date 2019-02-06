/**
 * @Author: Avinash Kadimisetty <avinash>
 * @Date:   2019-02-06T12:45:17-06:00
 * @Email:  kavinash366@gmail.com
 * @Project: Leetcode
 * @Filename: 257.cpp
 * @Last modified by:   avinash
 * @Last modified time: 2019-02-06T12:45:26-06:00
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
 #include <string>
 class Solution {
 public:
     vector<string> binaryTreePaths(TreeNode* root) {
         string s = "";
         vector<string> v;
         generatePaths(root, s, v);
         return v;
     }

     void generatePaths(TreeNode* root, string s, vector<string> &v) {
         if(root == NULL) return;
         if(root->left == NULL && root->right == NULL) {
             s += to_string(root->val);
             v.push_back(s);
         }
         else {
             s += to_string(root->val);
             s += "->";
         }
         generatePaths(root->left, s, v);
         generatePaths(root->right, s, v);
     }
 };
