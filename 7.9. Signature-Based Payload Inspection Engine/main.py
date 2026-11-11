def inspect_payload(payload_text, signatures):
    text = payload_text.lower()
    
    result = []
    for sig_id, pattern, severity_level in signatures:
        if pattern.lower() in text:
            result.append((sig_id, pattern, severity_level))
    
    if not result:
        return ["CLEAN: No threats detected"]
    
    result.sort(key=lambda x: (-x[2], x[0]))
    return [f"[ALERT {sid}] SEV:{sev} PATTERN:'{pat}'" for sid, pat, sev in result]   
    
    
def main():
    s = int(input())
    signature = []
    for _ in range(s):
        rule = tuple(input().strip().split(','))
        signature.append((rule[0], rule[1], int(rule[2])))
    
    p = int(input())
    for i in range(1, p + 1):
        rp = input()
        print(f"--- PAYLOAD {i} ---")
        for alert in inspect_payload(rp, signature):
            print(alert)

if __name__ == "__main__":
    main()
