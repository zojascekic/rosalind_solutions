
def main():
    with open("rosalind_dna.txt", "r") as file:
        dna_string = file.read()
        output = ""
        for base in dna_string:
            if base == "A":
                output += "T"
            elif base == "C":
                output += "G"
            elif base == "G":
                output += "C"
            elif base == "T":
                output += "A"
    print(output[::-1])


if __name__ == "__main__":
    main()
