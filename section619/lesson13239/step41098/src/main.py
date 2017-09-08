number_of_unique_chars, size_of_encoded_str = map(int, input().split())

chars_with_codes = dict()
for each in range(number_of_unique_chars):
    line = str(input()).split(': ')
    char = line[0]
    char_code = line[1]

    chars_with_codes[char_code] = char

encoded_str = str(input())


def decode_str(encoded_str : str, chars_with_codes : dict):
    decoded_str = str()

    idx = 0
    while not idx == len(encoded_str):
        char_code = str()
        while chars_with_codes.get(char_code) is None:
            char_code += encoded_str[idx]
            idx += 1
        decoded_str += chars_with_codes[char_code]

    return decoded_str


print(decode_str(encoded_str, chars_with_codes))