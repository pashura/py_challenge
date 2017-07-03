#  challenge 1


def main(input_data):
    result = ""
    for i in input_data:
        result += chr((ord(i) + 2) % 97 % 26 + 97) if i not in [' ', '.', '(', ')', '\''] else i
    print(result)

if __name__ == '__main__':
    text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddga" \
                 "gclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc" \
                 " spj."
    main('map')
