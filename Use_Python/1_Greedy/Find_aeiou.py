while True:
    input_string = input()

    if input_string == '#':
        break

    count = 0

    for char in input_string:
        if char in 'aeiouAEIOU':
            count += 1

    print(count)