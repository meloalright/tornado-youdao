import bcrypt

def gen_hash(password):
    password = bytes(password, encoding = "utf-8")
    return str(bcrypt.hashpw(password, bcrypt.gensalt()), 'utf-8')  # encode


def check(password, password_hash):
    password = bytes(password, encoding = "utf-8")
    password_hash = bytes(password_hash, encoding = "utf-8")
    return bcrypt.checkpw(password, password_hash)