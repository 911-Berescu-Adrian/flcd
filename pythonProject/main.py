from symbol_table import SymbolTable

st = SymbolTable()

st.insert("a")
st.insert("b")
st.insert("c")

print(st.lookup("a"))
print(st.lookup("b"))
print(st.lookup("d"))

print(st.find_position("a"))
print(st.find_position("c"))

