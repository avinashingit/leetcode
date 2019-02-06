/**
 * @Author: Avinash Kadimisetty <avinash>
 * @Date:   2019-02-06T11:36:34-06:00
 * @Email:  kavinash366@gmail.com
 * @Project: Leetcode
 * @Filename: 112.cpp
 * @Last modified by:   avinash
 * @Last modified time: 2019-02-06T11:36:47-06:00
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

    bool hasPathSum(TreeNode* root, int sum) {
        if(root == NULL) return false;
        sum -= root->val;
        if(root->left == NULL && root->right == NULL) return (sum == 0);
        return hasPathSum(root->left, sum) or hasPathSum(root->right, sum);
    }
};
