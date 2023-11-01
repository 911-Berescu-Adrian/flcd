from symbol_table import SymbolTable

st = SymbolTable()

st.insert_string_constant("a")
st.insert_string_constant("aag")
st.insert_string_constant("b")
st.insert_string_constant("c")

print(st.lookup_string_constant("a"))
print(st.lookup_string_constant("aag"))
print(st.lookup_string_constant("b"))
print(st.lookup_string_constant("d"))

print(st.find_position_string_constant("a"))
print(st.find_position_string_constant("aag"))
print(st.find_position_string_constant("c"))

st.insert_int_constant(2)
st.lookup_int_constant(2)
print(st)