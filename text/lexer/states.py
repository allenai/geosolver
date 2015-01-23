__author__ = 'minjoon'


class Token(object):
    def __init__(self, sentence, index):
        self.sentence = sentence
        self.index = index
        self.word = sentence[index]
        self.name = self.index
        self.label = "%s-%d" % (self.word, self.index)

    def __repr__(self):
        return "%s(word=%s, index=%d)" % (self.__class__.__name__, self.word, self.index)

