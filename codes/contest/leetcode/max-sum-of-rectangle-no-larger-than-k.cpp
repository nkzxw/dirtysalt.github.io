/* coding:utf-8
 * Copyright (C) dirlt
 */

#include <vector>
#include <set>
using namespace std;

// NOTE(yan): 解法非常好，最重要的是确保两个矩阵是可以相减，得到一个sub matrix.

class Solution {
  public:
    int maxSumSubmatrix(vector<vector<int>>& matrix, int k) {
        int n = matrix.size();
        int m = matrix[0].size();
        int res = INT_MIN;
        for (int i = 0; i < m; i++) {
            vector<int> acc(n, 0);
            for (int j = i; j < m; j++) {
                for (int k = 0; k < n; k ++) {
                    acc[k] += matrix[k][j];
                }
                set<int> seen;
                int cum = 0;
                seen.insert(cum);
                for(int value: acc) {
                    cum += value;
                    auto it = seen.lower_bound(cum - k );
                    if (it != seen.end()) {
                        int max_sum = cum - *it;
                        res = max(res, max_sum);
                    }
                    seen.insert(cum);
                }
            }
        }
        return res;
    }
};
