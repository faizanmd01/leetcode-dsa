from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr):
        n = len(arr)

        mp = defaultdict(list)

        for i in range(n):
            mp[arr[i]].append(i)

        q = deque()
        visited = [False] * n

        q.append(0)
        visited[0] = True

        steps = 0

        while q:
            size = len(q)

            for _ in range(size):

                currIdx = q.popleft()

                if currIdx == n - 1:
                    return steps

                #================================================================
                #EXPLORE ALL POSSIBLE OPTIONS

                if currIdx + 1 < n and not visited[currIdx + 1]: #OPTION-1 (Move Forward)
                    visited[currIdx + 1] = True
                    q.append(currIdx + 1)

                if currIdx - 1 >= 0 and not visited[currIdx - 1]: #OPTION-2 (Move Backward)
                    visited[currIdx - 1] = True
                    q.append(currIdx - 1)

                for newIdx in mp[arr[currIdx]]: #OPTION-3 (Move to same valued idx)
                                                #newIdx could be before currIdx or after currIdx
                    if not visited[newIdx]:
                        visited[newIdx] = True
                        q.append(newIdx)

                #===================================================================
                mp[arr[currIdx]].clear() #EXPLAINED BELOW :)

            steps += 1

        return -1