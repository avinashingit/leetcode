/**
 * @Author: Avinash Kadimisetty <avinash>
 * @Date:   2019-02-23T19:19:07-06:00
 * @Email:  kavinash366@gmail.com
 * @Project: Leetcode
 * @Filename: 100.cpp
 * @Last modified by:   avinash
 * @Last modified time: 2019-02-23T19:19:13-06:00
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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if(p == NULL && q == NULL)
            return true;
        if(p == NULL || q == NULL) {
            return false;
        }
        if(p->val != q->val) {
            return false;
        }
        else {
            return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
        }
    }
};
