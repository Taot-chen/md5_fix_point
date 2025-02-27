import hashlib

def string_to_md5(string):
    md5_val = hashlib.md5(string.encode('utf8')).hexdigest()
    return md5_val

str_a = "54db1011d76dc70a0a9df3ff3e0b390f"
md5_result = string_to_md5(str_a)

print(f"{str_a} md5: {md5_result}")

