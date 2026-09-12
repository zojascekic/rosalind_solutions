
def main():
    with open("rosalind_dna.txt", "r") as file:
        dna_string = file.read()
        count_a = 0
        count_c = 0
        count_g = 0
        count_t = 0

        for char in dna_string:
            if char == "A":
                count_a += 1
            elif char == "C":
                count_c += 1
            elif char == "G":
                count_g += 1
            elif char == "T":
                count_t += 1
    print(count_a, count_c, count_g, count_t)


if __name__ == "__main__":
    main()
