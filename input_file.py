def main():
    input_file = "numbers.txt"

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

if __name__ == "__main__":
    main()