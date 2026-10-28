class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        bobPath,adj = {},defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bobTraverse(gate,parent,step):
            bobPath[gate] = step
            if gate==0: return True
            for nei in adj[gate]:
                if nei==parent: continue
                if bobTraverse(nei,gate,step+1): return True
            
            del bobPath[gate]
            return False
        
        bobTraverse(bob,-1,0)
        
        max_net_income,queue = float("-inf"),deque()
        queue.append((0,-1,0,0))
        while queue:
            gate,parent,cur_net_income,step = queue.popleft()
            cur_net_income += self.getGateAmount(bobPath,gate,step,amount)
            if len(adj[gate])==1 and gate!=0:
                max_net_income = max(max_net_income,cur_net_income)
                
            for nei in adj[gate]:
                if nei==parent: continue
                queue.append((nei,gate,cur_net_income,step+1))
        
        return max_net_income

    def getGateAmount(self,bobPath,gate,step,amount):
        if gate not in bobPath: return amount[gate]
        if bobPath[gate]>step: return amount[gate]
        if bobPath[gate]==step: return amount[gate]//2
        return 0
        