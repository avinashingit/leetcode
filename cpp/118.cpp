/**
 * @Author: Avinash Kadimisetty <avinash>
 * @Date:   2019-03-07T01:22:40-06:00
 * @Email:  kavinash366@gmail.com
 * @Project: Elements of Programming Interviews
 * @Filename: 118.cpp
 * @Last modified by:   avinash
 * @Last modified time: 2019-03-07T01:22:43-06:00
 * @License: MIT License
 */



class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> result;
        if(numRows == 0) return result;
        vector<int> v(1, 1);
        result.push_back(v);
        pascal(result, 2, numRows);
        return result;
    }

    void pascal(vector<vector<int>> &result, int level, int maxlevel) {
        if(level > maxlevel) return;
        vector<int> temp;
        for(int i=0;i<level;i++) {
            if(i==0 || i== level-1) {
                temp.push_back(1);
            }
            else {
                temp.push_back(result[level-2][i-1]+ result[level-2][i]);
            }
        }
        result.push_back(temp);
        pascal(result, level+1, maxlevel);
    }
};
