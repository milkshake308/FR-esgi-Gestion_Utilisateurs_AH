import random
import hash


def generate_passwd():
    element = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-*/~$%&.:?!@"
    passwd = ""

    for i in range(9): passwd = passwd + element[random.randint(0, len(element) - 1)]
    passwd_hash = hash.sha256_generator(passwd)
    return passwd, passwd_hash
