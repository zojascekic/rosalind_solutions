
def gc_content(dna):
    count_c, coung_g = [dna.count(base) for base in "CG"]
    sum = count_c + coung_g
    return (sum / len(dna) * 100)


def main():
    data_dict = {}
    with open("sample.txt", "r") as file:
        current_header = None

        for line in file:
            line = line.strip()
            if line.startswith(">"):
                current_header = line[1:]
                data_dict[current_header] = ""
            else:
                data_dict[current_header] += line
        for header in data_dict:
            data_dict[header] = gc_content(data_dict[header])
        max_value = max(data_dict.values())
        max_name = max(data_dict, key=data_dict.get)  # type: ignore
        print(f"{max_name}\n{max_value}")


if __name__ == "__main__":
    main()
