def main():
    name_list = []

    while(True):
        try:
            name = input("Name: ")
        except EOFError:
            print(print_names(name_list))
            exit()
        else:
            name_list.append(name)


def print_names(name_list):

    out_text = "Adieu, adieu, to "
    len_list = len(name_list)

    out_text += name_list[0]

    if len_list == 1:
        return out_text

    elif len_list == 2:
        out_text += " and {}".format(name_list[-1])
        return out_text

    else:
        for name in name_list[1:-1]:
            out_text += ", {}".format(name)

        out_text += ", and {}".format(name_list[-1])
        return out_text

if __name__ == "__main__":
    main()
