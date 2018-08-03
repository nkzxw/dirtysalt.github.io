/* coding:utf-8
 * Copyright (C) dirlt
 */

// TODO(yan): still not work.

#include <iostream>
#include <queue>
#include <vector>
using namespace std;

class Solution {
public:
    struct Item {
        int v;
        int h;
        Item(int v, int h) {
            this->v = v;
            this->h = h;
        }
    };

    /**
     * @param n: n nodes labeled from 0 to n - 1
     * @param edges: a undirected graph
     * @return:  a list of all the MHTs root labels
     */
    int bfs(vector< vector<int> >& adj, int src, int minh) {
        queue< Item > Q;
        int n = adj.size();
        int seen = 0;

        vector<bool> visited(n, false);
        Q.push(Item(src, 1));
        visited[src] = true;
        int maxh = 1;
        seen += 1;

        while(!Q.empty()) {
            Item item = Q.front();
            Q.pop();
            int v = item.v;
            int h = item.h;
            for(int i = 0; i < adj[v].size(); i++) {
                int to = adj[v][i];
                if (!visited[to]) {
                    Q.push(Item(to, h + 1));
                    visited[to] = true;
                    seen += 1;
                    maxh = max(maxh, h+1);
                    if ((seen == n) || (maxh > minh)) {
                        return maxh;
                    }
                }
            }
        }
        return maxh;
    }

    vector<int> findMinHeightTrees(int n, vector< vector<int> > &edges) {
        // Wirte your code here
        vector< vector<int> > adj;
        for (int i = 0; i < n; i++) {
            vector<int> nxts;
            adj.push_back(nxts);
        }
        for (int i = 0; i < edges.size();i++) {
            int u = edges[i][0];
            int v = edges[i][1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        vector< Item > res;
        int minh = n;
        for (int src = 0; src < n; src++) {
            int h = bfs(adj, src, minh);
            minh = min(minh, h);
            res.push_back(Item(src, h));
        }
        vector<int> out;
        for (int i = 0; i < res.size(); i++) {
            int src = res[i].v;
            int h = res[i].h;
            if (h == minh) {
                out.push_back(src);
            }
        }
        return out;
    }
};

int main() {
    vector< vector< int >> edges = {{3,0},{3,1},{3,2},{3,4},{5,4}};
    int n = 6;
    Solution s;
    vector<int> out = s.findMinHeightTrees(n, edges);
    cerr << "[";
    for(int i = 0; i < out.size(); i++) {
        cerr << out[i] << " ";
    }
    cerr << "]" << endl;
    return 0;
}
