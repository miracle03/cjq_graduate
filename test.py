import hashlib

def md5(value):
    m = hashlib.md5()
    m.update(value.encode('UTF-8'))
    return m.hexdigest()
a="981911"
s=md5(a)
print(s)