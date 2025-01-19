from collections import deque

def word_ladder_length(beginWord: str, endWord: str, wordList: list[str]) -> int:
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0

    queue = deque([(beginWord, 1)])  # (current word, transformation count)
    
    while queue:
        word, steps = queue.popleft()
        
        if word == endWord:
            return steps
        
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                transformed = word[:i] + char + word[i+1:]
                if transformed in wordSet:
                    queue.append((transformed, steps + 1))
                    wordSet.remove(transformed)  # Avoid revisiting
        
    return 0

# Example
print(word_ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 5
print(word_ladder_length("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0
