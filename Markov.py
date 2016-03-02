import random

class MarkovNode:
    def __init__(self, input_string):
        self.terms = input_string.split(" ")
        self.states = {}
        for word in self.terms:
            self.states[word] = []
        for index in range(len(terms)-1):
            self.states[self.terms[index]].append(self.terms[index + 1])

        self.state = random.choice(self.terms)

    def next_state(self):
        self.state = random.choice(self.states[self.state])
        return self.state

    def current_state(self):
        return self.state
