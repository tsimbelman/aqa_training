

def return_abonent_number(data_base, abonent_name, format_number=None):
    for i in data_base["id"]:
        if i["name"] in abonent_name:
            number = i["number"]
            format_number = number[5:]
            print('Number of' ,abonent_name, 'is:' ,format_number)
            return format_number
    if format_number is None:
        print('Nothing was found')

def main():
    return_abonent_number(data_base, abonent_name, format_number=None)

if __name__=='__main__':
    main()