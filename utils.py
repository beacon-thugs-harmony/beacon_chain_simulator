
def xor(string1, string2):
    bytes1 = bytearray(string1, "ascii")
    bytes2 = bytearray(string2, "ascii")
    output = []
    for x in range(len(bytes1)):
        output.append(chr(bytes1[x]^bytes2[x]%256))
    return "".join(output)

def convert_to_int(str, length_of_bytes_we_use_for_demo = 32):
    result = 0
    for i in range(length_of_bytes_we_use_for_demo):
        result = result + ord(str[i]) << ((length_of_bytes_we_use_for_demo - i - 1) * 8)
    return result
