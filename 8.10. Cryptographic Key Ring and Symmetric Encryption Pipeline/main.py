class Key:
    def __init__(self, key_id, algorithm, raw_key_str):
        self.key_id = key_id
        self.algorithm = algorithm
        self.raw_key_str = raw_key_str
        self.is_revoked = False
        self.usage_count = 0
    
    def revoke(self):
        self.is_revoked = True
    
    def get_info(self):
        return f"KEY {self.key_id} [{self.algorithm}] (Active: {not self.is_revoked}, Used: {self.usage_count})"

class KeyRing:
    def __init__(self):
        self.keys = {}
    
    def add_key(self, key_obj):
        self.keys[key_obj.key_id] = key_obj
    
    def get_key(self, key_id):
        return self.keys.get(key_id, None)
    
    def revoke_key(self, key_id):
        if self.keys.get(key_id):
            self.keys.get(key_id).revoke()
            return True
        return False
    
    def list_keys(self):
        return [self.keys[i].get_info() for i in sorted(self.keys.keys())]

class CipherPipeline:
    def __init__(self, keyring: KeyRing):
        self.keyring = keyring

    def encrypt(self, key_id, plaintext):
        key = self.keyring.get_key(key_id)
        if key is None:
            return "ERROR: KEY_NOT_FOUND"
        
        if key.is_revoked:
            return "ERROR: KEY_REVOKED"
        
        key.usage_count += 1
        algo = key.algorithm
        
        if algo == "REV":
            ciphertex = plaintext[::-1]
        elif algo == "ROT":
            k = int(key.raw_key_str)
            ciphertex = "".join(chr(32 + ((ord(c) - 32 + k) % 95)) if 32 <= ord(c) <= 126 else c for c in plaintext)
        elif algo == "XOR":
            ciphertex = "".join(f"{ord(plaintext[i]) ^ ord(key.raw_key_str[i % len(key.raw_key_str)]):02x}" for i in range(len(plaintext)))
        else:
            ciphertex = plaintext
            
        return f"ENC:{ciphertex}"
        
    def decrypt(self, key_id, ciphertext):
        key = self.keyring.get_key(key_id)
        if key is None:
            return "ERROR: KEY_NOT_FOUND"
        
        if key.is_revoked:
            return "ERROR: KEY_REVOKED"
        
        key.usage_count += 1
        algo = key.algorithm
        
        if algo == "REV":
            plaintext = ciphertext[::-1]
        elif algo == "ROT":
            k = int(key.raw_key_str)
            plaintext = "".join(chr(32 + ((ord(c) - 32 - k) % 95)) if 32 <= ord(c) <= 126 else c for c in ciphertext)
        elif algo == "XOR":
            bytes_list = [int(ciphertext[i:i+2], 16) for i in range(0, len(ciphertext), 2)]
            plaintext = "".join(chr(b ^ ord(key.raw_key_str[i % len(key.raw_key_str)])) for i, b in enumerate(bytes_list))
        else:
            plaintext = ciphertext
            
        return f"DEC:{plaintext}"
            
def main():
    k_c = int(input())
    keyring = KeyRing()
    for _ in range(k_c):
        key_id, algorithm, raw_key_str = [x.strip() for x in input().split()]
        keyring.add_key(Key(key_id, algorithm, raw_key_str))
    pipeline = CipherPipeline(keyring)    
    
    q = int(input())
    for _ in range(q):        
        tp = input()
        if tp == "KEYS":
            for info in keyring.list_keys():
                print(info)
        else:
            tp = tp.split(' ', 2)
            if tp[0] == "ENC":
                print(pipeline.encrypt(tp[1], tp[2]))
            elif tp[0] == "DEC":
                print(pipeline.decrypt(tp[1], tp[2]))
            else:
                keyring.revoke_key(tp[1])
    
if __name__ == "__main__":
    main()
