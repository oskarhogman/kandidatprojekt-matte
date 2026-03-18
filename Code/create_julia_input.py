import matrix_generator as mg

for i in range(9, 10):
    print(i)
    mg.write_file('polytopes/GTP' + str(i) + '.txt', 
                  'julia_input/GTP' + str(i) + '.jl')
