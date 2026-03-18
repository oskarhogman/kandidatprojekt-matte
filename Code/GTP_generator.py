def partition(n : int):
    result = [[n]]

    for i in range(1, n):
        a = n-i
        R = partition(i)
        for r in R:
            if r[0] <= a:
                result.append([a] + r)

    return result

def generate_GTPs(lambda_size : int):
    lambda_list = partition(lambda_size)
    with open('polytopes/GTP' + str(lambda_size) + '.txt', 'w') as out:
        for lambdanr in lambda_list:
            for rowsumdiff in lambda_list:
                if lambdanr < rowsumdiff:
                    continue
                #elif len(rowsumdiff) == len([i for i in rowsumdiff if i == 1]):
                    #continue
                else:
                    polyprint = ''
                    for i in lambdanr:
                        polyprint += str(i) + ' '
                    polyprint += ': '
                    for j in rowsumdiff:
                        polyprint += str(j) + ' '
                    print(polyprint, file = out)

for i in range(1, 10):
    generate_GTPs(i)
