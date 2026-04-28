def main():
    input_file = "numbers.txt"
    even_file = "even_numbers.txt"
    odd_file = "odd_numbers.txt"
    
    try:
        with open(input_file, "r") as infile:
            text = infile.read()
    except FileNotFoundError:
        print(f"Input file '{input_file}' not found.")
        return

    numbers = []
    for token in text.split():
        try:
            numbers.append(int(token))
        except ValueError:
            continue

    with open(even_file, "w") as even_out, open(odd_file, "w") as odd_out:
        for number in numbers:
            if number % 2 == 0:
                even_out.write(f"{number}\n")
            else:
                odd_out.write(f"{number}\n")

if __name__ == "__main__":
    main()