from collections import deque

def word_ladder_length(beginWord: str, endWord: str, wordList: list[str]) -> int:
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0

    queue = deque([(beginWord, 1)])
    
    while queue:
        current_word, steps = queue.popleft()
        
        for i in range(len(current_word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                next_word = current_word[:i] + c + current_word[i+1:]
                
                if next_word == endWord:
                    return steps + 1
                
                if next_word in wordSet:
                    wordSet.remove(next_word)
                    queue.append((next_word, steps + 1))
                    
    return 0

# Example
print(word_ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 5
print(word_ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))         # 0