def getplaintext():
    ans = input("Enter plain text\n")
    return ans.lower()


def getciphertext():
    ans = input("Enter cipher text\n")
    return ans.lower()


def getkey():
    ans = input("Enter key\n")
    return int(ans)


def encrypt(pt, key):
    ciphertext = ""
    for x in pt:
        if x == " " or x == "," or x == "?" or x == "!" or x == ":":
            ciphertext = ciphertext + " "
        else:
            index = (ord(x)) - 97
            temp = ((index + key) % 26)
            ciphertext = ciphertext + chr(temp + 97)
    return ciphertext


def decrypt(ct, key):
    plaintext = ""
    for x in ct:
        if x == " " or x == "," or x == "?" or x == "!" or x == ":":
            plaintext = plaintext + " "
        else:
            index = (ord(x)) - 97
            temp = ((index - key) % 26)
            plaintext = plaintext + chr(temp + 97)
    return plaintext


def bruteforce(ct):
    for key in range(26):
        print(decrypt(ct,key) + "    ------> Key = " + str(key))


if __name__ == '__main__':
    ans = input("1-Encrypt\n2-Decrypt with key\n3-Brute force\n")
    ans = int(ans)
    if ans == 1:
        pt = getplaintext()
        key = getkey()
        ct = encrypt(pt, key)
        print(ct)
        quit()

    if ans == 2:
        ct = getciphertext()
        key = getkey()
        pt = decrypt(ct, key)
        print(pt)
        quit()

    if ans == 3:
        ct = getciphertext()
        bruteforce(ct)
        quit()

    else:
        print("Wrong input")
        quit()

