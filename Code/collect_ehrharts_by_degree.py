def read_file(filename):
    in_data = dict()
    with open(filename, 'r') as file_in:
        for line in file_in:
            data = line.split(',')
            data[0] = data[0].strip()
            data[1] = data[1].strip()
            if data[1] == 'data missing':
                continue
            if data[1] in in_data.keys():
                in_data[data[1]].append(data[0])
            else:
                in_data[data[1]] = [data[0]]
    print(f'read file {filename} successfully')
    return in_data
    
def separate_grades(in_data):
    all_data = dict()
    for key, value in in_data.items():
        for i in range(len(key)):
            grade = ''
            if key[i] == 'x':
                if key[i+1] == '*' and key[i+2] == '*':
                    j = i + 3
                    while key[j] != '/' and key[j] != ' ':
                        grade += key[j]
                        j += 1
                        if j >= len(key):
                            break
                    break
                else:
                    grade = '1'
                    break
            else:
                grade = '0'
        if grade == '0':
            if '0' in all_data.keys():
                if key in all_data['0']:
                    for value2 in value:
                        all_data['0'][key].append(value2)
            else:
                all_data['0'] = dict()
                all_data['0'][key] = value
        else:
            if grade in all_data.keys():
                if key in all_data[grade]:
                    for value2 in value:
                        all_data[grade][key].append(value2)
                else:
                    all_data[grade][key] = value
            else:
                all_data[grade] = dict()
                all_data[grade][key] = value
    return all_data

def merge_data(total_data, in_data):
    for key, value in in_data.items():
        if key in total_data.keys():
            total_data[key] = total_data[key] + value
        else:
            total_data[key] = value
    return total_data

def write_to_file(all_data):
    for key, value in all_data.items():
        with open(f'ehrhart_files/degrees/degree{key}.txt', 'w') as file_out:
            for key2, value2 in value.items():
                print(f'{key2}, {value2}', file = file_out)

def main():
    total_data = dict()
    for i in range(1, 10):
        filename = f'ehrhart_files/GTP{i}.txt'
        in_data = read_file(filename)
        total_data = merge_data(total_data, in_data)
    for i in range(10, 22):
        filename = f'ehrhart_files/GTP10d{i}.txt'
        in_data = read_file(filename)
        total_data = merge_data(total_data, in_data)
    all_data = separate_grades(total_data)
    write_to_file(all_data)
    print('finished')
    
if __name__ == '__main__':
    main()
