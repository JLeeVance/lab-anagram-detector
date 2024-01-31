class Anagram:

    def __init__(self, word):
        self.word = word

    def match(self, list_of_ana):
        matched_list = []
        for word in list_of_ana:
            if sorted(word) == sorted(self.word):
                matched_list.append(word)
        return matched_list
         




list_of_ana = ['enlists', 'google', 'inlets', 'banana']
listen = Anagram("listen")
print(listen.match(list_of_ana))