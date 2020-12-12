def solution():

    for i in range(21):
        s = '0' + str(i) if i // 10 == 0 else str(i)
        

        d = defaultdict(dict)
        for u, v, t, p in a:
            d[u][v] = [t,p]
            d[v][u] = [t,p]

        def dfs(cur, units, profit):
            global ans
            if not d[cur]:
                ans = max(ans, profit)
                return
            if units < min(t for t, p in d[cur].values()):
                ans = max(ans, profit)
                return
            for nxt in list(d[cur].keys()):
                t, p = d[cur][nxt]
                if units < t: continue
                d[cur].pop(nxt); d[nxt].pop(cur)
                dfs(nxt, units - t, profit + p)
                d[cur][nxt] = [t, p]
                d[nxt][cur] = [t, p]

        ans = 0
        for i in range(1, n + 1):
            if i in d:
                dfs(i, m, 0)
        print(f'output={ans}')