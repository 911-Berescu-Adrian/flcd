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
        self.output_states = []