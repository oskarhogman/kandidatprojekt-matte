def read_file(filename):
    polynomials = []
    with open(filename, 'r') as file_in:
        for line in file_in:
            data = line.split(',')
            polynomials.append(data[0].strip())
    return polynomials
    
def write_file(all_polynomials):
    with open('ehrhart_files/all_ehrharts.txt', 'w') as file_out:
        for ehrhart in all_polynomials:
            print(ehrhart, file = file_out)
    
def main():
    all_polynomials = []
    for i in range(0, 22):
        polynomials = read_file(f'ehrhart_files/degrees/degree{i}.txt')
        all_polynomials = all_polynomials + polynomials
    write_file(all_polynomials)
    print('finished')
    
if __name__ == '__main__':
    main()
