/**
 * @Author: Avinash Kadimisetty <avinash>
 * @Date:   2019-02-06T11:37:31-06:00
 * @Email:  kavinash366@gmail.com
 * @Project: Leetcode
 * @Filename: 113.cpp
 * @Last modified by:   avinash
 * @Last modified time: 2019-02-06T11:38:16-06:00
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
     vector<vector<int>> pathSum(TreeNode* root, int sum) {
         vector<vector<int>> paths;
         vector<int> path;
         traverse(root, path, paths, sum);
         return paths;
     }

     void traverse(TreeNode* root, vector<int> &path, vector<vector<int>> &paths, int sum) {
         if(root == NULL) return;
         path.push_back(root->val);
         sum -= root->val;
         if(root->left == NULL && root->right == NULL && sum == 0) {
             paths.push_back(path);
         }
         traverse(root->left, path, paths, sum);
         traverse(root->right, path, paths, sum);
     }
 };
