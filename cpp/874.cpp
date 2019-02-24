/**
 * @Author: Avinash Kadimisetty <avinash>
 * @Date:   2019-02-23T19:09:11-06:00
 * @Email:  kavinash366@gmail.com
 * @Project: Leetcode
 * @Filename: 874.cpp
 * @Last modified by:   avinash
 * @Last modified time: 2019-02-23T19:09:17-06:00
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
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> leaves1, leaves2;
        get_leaves(root1, leaves1);
        get_leaves(root2, leaves2);
        return leaves1 == leaves2;
    }

    void get_leaves(TreeNode* root, vector<int> &path) {
        if(root == NULL)
            return;
        if(root->left == NULL && root->right == NULL) {
            path.push_back(root->val);
            return;
        }
        get_leaves(root->left, path);
        get_leaves(root->right, path);
    }
};
