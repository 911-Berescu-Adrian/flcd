from lab4.finite_automaton import FiniteAutomaton

fa = FiniteAutomaton("fa.in")
fa.display_states()
fa.display_alphabet()
fa.display_transitions()
fa.display_initial_state()
fa.display_final_states()

sequence = "ab"
if fa.verify_sequence(sequence):
    print(f"Sequence '{sequence}' is accepted by the FA.")
else:
    print(f"Sequence '{sequence}' is not accepted by the FA.")