from collections import deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if len(beginWord) != len(endWord):
            return []
        words = set(wordList)
        if endWord not in words:
            return []
        q = deque([beginWord])
        parents = {beginWord: []}
        found = False

        while q and not found:
            level_words = set()

            for _ in range(len(q)):
                temp = q.popleft()

                for j in range(len(temp)):
                    for k in "abcdefghijklmnopqrstuvwxyz":
                        newt = temp[:j] + k + temp[j + 1:]

                        if newt in words:
                            if newt not in level_words:
                                level_words.add(newt)
                                q.append(newt)
                                parents[newt] = [temp]
                            else:
                                parents[newt].append(temp)

                            if newt == endWord:
                                found = True

            words -= level_words

        if not found:
            return []

        ans = []

        def dfs(word, path):
            if word == beginWord:
                ans.append(path[::-1])
                return

            for parent in parents[word]:
                dfs(parent, path + [parent])

        dfs(endWord, [endWord])

        return ans