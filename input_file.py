def main():
    input_file = "numbers.txt"

    try:
        with open(input_file, "r") as infile:
            text = infile.read()
    except FileNotFoundError:
        print(f"Input file '{input_file}' not found.")
        return


if __name__ == "__main__":
    main()