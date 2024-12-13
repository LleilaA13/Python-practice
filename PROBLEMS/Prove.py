# %% ---- FUNC1 ----
def func1(D):
    D = {k: sorted(v, reverse=True) for k, v in D.items()}
    lista = []
    for k, v in D.items():
        # Check if the index k is within the bounds of the list v
        if k < len(v):
            lista.append(v[k])
    return lista

if __name__ == "__main__":
    D = {4: ["c", "h", "f", "g", "e"], 2: ["a", "z", "b", "w"], 0: ["a", "b", "a"]}
    print(func1(D)) # ['c', 'b', 'b']
# %%  ---- FUNC2 ----
def func2(list_all, list_rm):
    for i in list_all[:]:
        if i not in list_rm:
            list_all.remove(i)
    return list_all

# %%  ---- FUNC3 ----