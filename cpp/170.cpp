/**
 * @Author: Avinash Kadimisetty <avinash>
 * @Date:   2019-02-21T14:31:03-06:00
 * @Email:  kavinash366@gmail.com
 * @Project: Elements of Programming Interviews
 * @Filename: 170.cpp
 * @Last modified by:   avinash
 * @Last modified time: 2019-02-21T14:31:04-06:00
 * @License: MIT License
 */



class TwoSum {
    map<int, int> m;
    vector<int> v;
public:
    /** Initialize your data structure here. */
    TwoSum() {

    }

    /** Add the number to an internal data structure.. */
    void add(int number) {
        m[number] = v.size();
        v.push_back(number);

    }

    /** Find if there exists any pair of numbers which sum is equal to the value. */
    bool find(int value) {
        for(int i=0;i<v.size();i++) {
            if(m.find(value-v[i]) != m.end()) {
                if(m[value-v[i]] != i) {
                    return true;
                }
            }
        }
        return false;
    }
};

/**
 * Your TwoSum object will be instantiated and called as such:
 * TwoSum obj = new TwoSum();
 * obj.add(number);
 * bool param_2 = obj.find(value);
 */
