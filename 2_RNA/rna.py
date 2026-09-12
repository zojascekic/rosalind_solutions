
def main():
    with open("rosalind_dna.txt", "r") as file:
        dna_string = file.read()
        output = dna_string.replace("T", "U")
    print(output)


if __name__ == "__main__":
    main()
