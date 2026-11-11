def sol():
    kq = {}
    while True:
        n = int(input())
        if n == 0:
            break
        kq["Count"] = kq.get("Count", 0) + 1
        kq["Sum"] = kq.get("Sum", 0) + n
        
    if not kq:
        print("NO_DATA")
    else:
        kq["Average"] = kq["Sum"] / kq["Count"]
        for key, value in kq.items():
            if key == "Average":
                print(f"{key}: {value:.2f}")
            else:
                print(f"{key}: {value}")

def main():
    t = int(input())
    for _ in range(t):
        sol()
    
if __name__ == "__main__":
    main()
