def describe_city(city, country='Vietnam'):
    print(f"{city.strip().title()} is in {country.strip().title()}.")

def main():
    n = int(input())
    for i in range(n):
        s = input()
        if "," in s:
            ct = s.split(",", 1)
            describe_city(ct[0], ct[1])
        else:
            describe_city(s)

if __name__ == "__main__":
    main()
