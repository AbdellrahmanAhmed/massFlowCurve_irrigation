out_Flow = int(input("Out Flow: \n"))
max_Storage = int(input("Max Storage: \n"))
B_Year = int(input("B. Year: \n"))
E_Year = int(input("E. Year: \n"))
inFlow = []

try:
    i = B_Year
    while True:
        inFlow.append(int(input(f"In Flow for Year {i} : \n")))
        i = 1 + i
except:
    pass

m = 0
s_d = 0
spill = 0
n = 0

for k in range(len(inFlow)):
    s_d = (inFlow[k] + s_d) - out_Flow
    n = n + 1
    if s_d > max_Storage:
        spill = s_d - max_Storage
    else:
        spill = 0

    print(f"""
    |================================= {B_Year + n} ================================|
            In Flow = {inFlow[k]}     Storage = {s_d}    Spill = {spill}
    |=======================================================================|""")
    s_d = s_d - spill
    spill = 0
