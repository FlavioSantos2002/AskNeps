def main():
    nd = int(input())
    s = 0
    for c in range(nd):
        s = s + int(input())
        if (s>=1000000):
            print(c+1)
            break

if __name__ == "__main__":
    main()
