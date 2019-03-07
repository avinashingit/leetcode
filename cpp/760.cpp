/**
 * @Author: Avinash Kadimisetty <avinash>
 * @Date:   2019-03-07T17:56:18-06:00
 * @Email:  kavinash366@gmail.com
 * @Project: Elements of Programming Interviews
 * @Filename: 760.cpp
 * @Last modified by:   avinash
 * @Last modified time: 2019-03-07T17:56:20-06:00
 * @License: MIT License
 */



class Solution {
public:
    vector<int> anagramMappings(vector<int>& A, vector<int>& B) {
        map<int, int> m;
        for(int i=0;i<B.size();i++)
            m[B[i]] = i;
        vector<int> result;
        for(int i=0;i<A.size();i++)
            result.push_back(m[A[i]]);
        return result;
    }
};
