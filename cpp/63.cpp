/**
 * @Author: Avinash Kadimisetty <avinash>
 * @Date:   2019-02-19T17:50:57-06:00
 * @Email:  kavinash366@gmail.com
 * @Project: LeetCode
 * @Filename: 63.cpp
 * @Last modified by:   avinash
 * @Last modified time: 2019-02-19T17:51:05-06:00
 * @License: MIT License
 */



class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int rows = obstacleGrid.size();
        int cols = obstacleGrid[0].size();
        vector<vector<long>> dp(rows, vector<long>(cols, 0));
        cout<<rows<<"-"<<cols<<endl;
        int replace_val = 1;
        for(int i=0;i<cols;i++)
        {
            if(obstacleGrid[0][i] == 1) {
                replace_val = 0;
            }
            dp[0][i] = replace_val;

        }
        replace_val = 1;
        for(int i=0;i<rows;i++)
        {
            if(obstacleGrid[i][0] == 1) {
                replace_val = 0;
            }
            dp[i][0] = replace_val;
        }
        for(int i=1;i<rows;i++) {
            for(int j=1;j<cols;j++) {
                if(obstacleGrid[i][j] == 1) {
                    dp[i][j] = 0;
                }
                else {
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
                }
            }
        }
        return (int)dp[rows-1][cols-1];
    }
};
