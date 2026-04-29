def process_integer_file(source_path='integer.txt', even_path='double.txt', odd_path='triple.txt'):

    even_squares = []
    odd_cubes = []

    with open(source_path, 'r') as source_file:
        for line in source_file:
            for token in line.split():
                try:
                    value = int(token)
                except ValueError:
                    continue

                if value % 2 == 0:
                    even_squares.append(str(value * value))
                else:
                    odd_cubes.append(str(value * value * value))

    with open(even_path, 'w') as even_file:
        even_file.write('\n'.join(even_squares))

    with open(odd_path, 'w') as odd_file:
        odd_file.write('\n'.join(odd_cubes))
        
    print(f"Wrote {len(even_squares)} even squares to '{even_path}' and {len(odd_cubes)} odd cubes to '{odd_path}'.")


if __name__ == '__main__':
    process_integer_file()
