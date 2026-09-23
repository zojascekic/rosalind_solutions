
def main():
    with open("rosalind_subs.txt", "r") as file:
        s = file.readline().strip()
        t = file.readline().strip()
        list_of_idx = []
        start = 0
        while True:
            idx = s.find(t, start)
            if idx == -1:
                break
            list_of_idx.append(idx+1)
            start = idx+1
    print(*list_of_idx)


if __name__ == "__main__":
    main()
