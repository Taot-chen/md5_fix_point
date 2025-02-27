import os
import hashlib

def md5sum(fname):
    if not os.path.isfile(fname):
        return False
    try:
        with open(fname, 'rb') as f:
            m = hashlib.md5()
            while True:
                d = f.read(8096)
                if not d:
                    break
                m.update(d)
            return m.hexdigest()
    except:
        return False

file_md5 = md5sum("string2md5.py")
print(file_md5)
