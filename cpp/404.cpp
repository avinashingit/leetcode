/**
 * @Author: Avinash Kadimisetty <avinash>
 * @Date:   2019-02-19T17:05:12-06:00
 * @Email:  kavinash366@gmail.com
 * @Project: Leetcode
 * @Filename: 404.cpp
 * @Last modified by:   avinash
 * @Last modified time: 2019-02-19T17:05:21-06:00
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
    int sumOfLeftLeaves(TreeNode* root) {
        if(root == NULL) return 0;
        queue<TreeNode*> q;
        q.push(root);
        int result = 0;
        while(!q.empty()) {
            TreeNode* temp = q.front();
            q.pop();
            if(temp->left != NULL) {
                if(temp->left->left == NULL && temp->left->right == NULL)
                    result += temp->left->val;
                q.push(temp->left);
            }
            if(temp->right != NULL)
                q.push(temp->right);
        }
        return result;
    }
};
