log = []

def sol():
    timestamp,service_name,response_time_ms,status_code = input().split(',')
    log.append((timestamp,service_name, int(response_time_ms), int(status_code)))

def main():
    t = int(input())
    for _ in range(t):
        sol()
        
    for time, service, response, status in sorted(log, key = lambda x: (-x[3], -x[2], x[1])):
            print(f"[{status}] {service} ({response}ms) @ {time}")

if __name__ == "__main__":
    main()
