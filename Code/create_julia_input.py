import matrix_generator as mg

for i in range(1, 11):
    print(i)
    mg.write_file('polytopes/GTP' + str(i) + '.txt', 
                  'julia_input/GTP' + str(i) + '.jl')
