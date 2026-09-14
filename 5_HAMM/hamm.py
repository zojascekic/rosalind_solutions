
def string_diff(string1, string2):
    count = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            count += 1
    return count


def main():
    with open("sample.txt", "r") as file:
        s = file.readline().strip()
        t = file.readline().strip()
    return (string_diff(s, t))


if __name__ == "__main__":
    print(main())
