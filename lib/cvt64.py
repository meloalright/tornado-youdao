#cvt 64
import base64

'''
 @ int => base64-str
'''
def encvt64(num):
    return base64.b64encode(str(num).encode(encoding='utf-8')).decode()


'''
 @ base64-str => int
'''
def decvt64(s):
    return int(base64.b64decode((s.encode(encoding="utf-8"))).decode())