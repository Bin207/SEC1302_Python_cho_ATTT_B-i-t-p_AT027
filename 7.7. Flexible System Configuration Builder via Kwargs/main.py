def make_config(service, *ports, **settings):
    port = "NONE" if not ports else ", ".join(str(i) for i in sorted(ports))
    setting = "DEFAULT" if not settings else ", ".join(f"{key}={value}" for key, value in sorted(settings.items()))
    return f"SERVICE: {service}\nPORTS: {port}\nSETTINGS: {setting}"

def sol():
    service_name = input()
    p = input().strip()
    ip = input().strip()
    
    ports = () if p == "NONE" else tuple(map(int, p.split(",")))
    setting = {}
    if ip != "DEFAULT":
        for i in ip.split(','):
            key, value = i.split('=', 1)
            setting[key.strip()] = value.strip()
        
    print(make_config(service_name, *ports, **setting))
 
def main():
    t = int(input())
    for _ in range(t):
        sol()
        

if __name__ == "__main__":
    main()
