
OPERATORS_LIST = {"KYIVSTAR": "096", "VODAFONE": "050", "LIFE": "093" }

def get_operator_name(number):
    for key in OPERATORS_LIST.keys():
        if OPERATORS_LIST[key] == number[3:6]:
            print(key)

def main():
    print_key()

if __name__=='__main__':
    main()

