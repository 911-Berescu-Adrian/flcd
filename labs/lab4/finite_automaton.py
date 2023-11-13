import re

class Transition:
    def __init__(self, _from, _to, _label):
        self._from = _from
        self._to = _to
        self._label = _label

class FiniteAutomaton:
    def __init__(self, filename):
        self.filename = filename
        self.states = []
        self.alphabet = []
        self.transitions = []
        self.initial_state = ""
        self.final_states = []
        self.read_fa(filename)

    def read_fa(self, filename):
        with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if line.startswith("states:"):
                    self.states = set(re.findall(r'\w+', line)[1:])
                elif line.startswith("alphabet:"):
                    self.alphabet = set(re.findall(r'\w+', line)[1:])
                elif line.startswith("initial_state:"):
                    self.initial_state = re.findall(r'\w+', line)[1]
                elif line.startswith("final_states:"):
                    self.final_states = set(re.findall(r'\w+', line)[1:])
                elif line.startswith("transitions:"):
                    for line in file:
                        parts = re.findall(r'\w+', line)
                        if len(parts) == 3:
                            self.transitions.append(Transition(*parts))
                        else:
                            print("Invalid transition format:", line)

    def display_states(self):
        print("states:", self.states)

    def display_alphabet(self):
        print("alphabet:", self.alphabet)

    def display_transitions(self):
        print("transitions:")
        for transition in self.transitions:
            print(transition._from, transition._to, transition._label)

    def display_initial_state(self):
        print("initial state:", self.initial_state)

    def display_final_states(self):
        print("final states:", self.final_states)

    def verify_sequence(self, sequence):
        current_state = self.initial_state
        for symbol in sequence:
            found = False
            for transition in self.transitions:
                if transition._from == current_state and transition._label == symbol:
                    current_state = transition._to
                    found = True
                    break
            if not found:
                return False
        return current_state in self.final_states