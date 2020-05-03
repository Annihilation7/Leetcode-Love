

class Solution {
private:
    vector<vector<int>> res;
    int time = 0;
public:
    vector<vector<int>> criticalConnections(int n, vector<vector<int>>& connections) {
        vector<unordered_set<int>> graph = build_graph(n, connections);
        // 初始化三个数组
        vector<int> disc(n, -1);
        vector<int> low(n, -1);
        vector<int> parents(n, -1);

        for(int i = 0; i < n; i++)
            if(disc[i] == -1)
                dfs(i, parents, low, disc, graph);

        return res;
    }

    vector<unordered_set<int>> build_graph(const int& n, const vector<vector<int>>& connections){
        vector<unordered_set<int>> res = vector<unordered_set<int>>(n, unordered_set<int>());
        for(const auto& c: connections){
            res[c[0]].insert(c[1]);
            res[c[1]].insert(c[0]);
        }
        return res;
    }

    void dfs(int u, vector<int>& parents, vector<int>& low, vector<int>& disc, const vector<unordered_set<int>>& graph){
        if(disc[u] != -1)
            return;
        low[u] = disc[u] = time++;
        for(const auto& v: graph[u]){
            if(disc[v] == -1){
                parents[v] = u;
                dfs(v, parents, low, disc, graph);
                if(low[v] > disc[u])
                    res.push_back(vector<int>{u, v});
                low[u] = min(low[u], low[v]);
            }
            else if(parents[u] != v)  // 有环，就再更新一次
                low[u] = min(low[u], disc[v]);
        }
    }
};