
def xor(string1, string2):
    bytes1 = bytearray(string1, "ascii")
    bytes2 = bytearray(string2, "ascii")
    output = []
    for x in range(len(bytes1)):
        output.append(bytes1[x]^bytes2[x])
    return "".join(map(chr, output))