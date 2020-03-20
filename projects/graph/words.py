from util import Queue


# Load words from dictionary
f = open('words.txt', 'r')
word_set = set(f.read().lower().split("\n"))
f.close()


def get_neighbors(word):
    '''
    Get all words one letter apart from given word
    '''

    results = []
    list_word = list(word)

    for i in range(len(list_word)):
        for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            temp_word = list_word.copy()
            temp_word[i] = letter

            joined_word = "".join(temp_word)

            if joined_word in word_set and joined_word != word:
                results.append(joined_word)
    
    return results

def word_ladder(begin_word, end_word):
    q = Queue()
    visited = set()

    q.enqueue([begin_word])

    while q.size() > 0:
        path = q.dequeue()
        word = path[-1]

        if word == end_word:
            return path

        if word not in visited:
            visited.add(word)

            for neighbor in get_neighbors(word):
                path_copy = path.copy()
                path_copy.append(neighbor)

                q.enqueue(path_copy)


print("HERE")
print(word_ladder("sail", "boat"))
print("END")