import sympy as sp

def ehrhart_polynomial(h_star, d):
    # Define the symbolic variable
    x = sp.symbols('x', integer=True)
    polynomial = 0
    # Sum over the h*-vector
    for j, h in enumerate(h_star):
        # Add h_j^* * binomial(t + d - j, d)
        polynomial += h * sp.binomial(x + d - j, d).expand(func=True)
    # Expand the polynomial for a cleaner form
    return sp.expand(polynomial)

def h_star_to_list(h_star_str):
    h_star_str = h_star_str.replace('- ', '+ -')
    splitted = h_star_str.split('+')
    for i in range(len(splitted)):
        splitted[i] = splitted[i].strip()

    h_star_list = []
    for elem in splitted:
        negative = False
        if elem[0] == '-':
            negative = True
            elem = elem.replace('-', '')
        if elem.find('x') != -1 and elem.find('x') == 0:
            elem = '1'
        elif elem.find('x') != -1:
            elem = elem[:elem.find('x')-1]
        if negative:
            h_star_list.insert(0, -1*int(elem))
        else:
            h_star_list.insert(0, int(elem))

    return h_star_list

def read_file(filename):
    in_data = []
    with open(filename, 'r') as file_in:
        for line in file_in:
            if line[:5] == 'Total':
                break
            data = line.split(',')
            if data[1] == ' Unable to create polyhedron or calculate h*' or data[1] == ' Dimension too high':
                in_data.append((data[0], 'data missing', data[2].strip()))
            else:
                in_data.append((data[0], data[1], int(data[2])))
    return in_data

def write_file(filename, ehrharts):
    with open(filename, 'w') as file_out:
        for ehrhart in ehrharts:
            print(f'{ehrhart[0]}, {ehrhart[1]}, {ehrhart[2]}', file = file_out)

def calculate_ehrharts(file_in, file_out):
    in_data = read_file(file_in)
    
    ehrharts = []
    for h_star in in_data:
        if h_star[1] == 'data missing':
            poly = 'data missing'
        else:
            as_list = h_star_to_list(h_star[1])
            poly = ehrhart_polynomial(as_list, h_star[2])
        ehrharts.append((h_star[0], poly, h_star[2]))
    
    write_file(file_out, ehrharts)

def main():
    for i in range(1, 10):
        file_in = f'julia_output/GTP{i}.txt'
        file_out = f'ehrhart_files/GTP{i}.txt'
        calculate_ehrharts(file_in, file_out)

'''
# Example usage:
# Define an h*-vector and the dimension of the polytope.
h_star = [1, 3, 2]  # For instance, h*(P) = 1 + 3t + 2t^2 for a 2-dimensional polytope
d = 2
poly = ehrhart_polynomial(h_star, d)
print("The Ehrhart polynomial is:")
sp.pprint(poly)
print(poly)
print(h_star_to_list('x^2 + 3x - 1'))
'''

if __name__ == '__main__':
    main()
