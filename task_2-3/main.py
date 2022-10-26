'''
Phone books is script with several plagin modules what should do read json file and execute next task:
1.Return and print number in format: w/o country code and cell operator code
2.Return and print name of cell operator depending on number
'''

import json_module, abonent_module, operator_module


def main():
    json_module.pretty_print()
    contack_book = json_module.data_base()

    abonent_name = input('Enter abonent name:')
    abonent_module.return_abonent_number(contack_book, abonent_name)

    abonent_number = input('Enter abonent number:')
    print(abonent_number)
    operator_module.get_operator_name(abonent_number)

if __name__ == '__main__':
    main()