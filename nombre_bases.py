def main():
    def get_initial_base():
        base_func = input("Entrer la base initiale du nombre : \n")
        if base_func.isnumeric():
            if int(base_func) > 0:
                return int(base_func)
        print("Ce n'est pas une base correcte")
        return get_initial_base()


    def get_number():
        number_func = input("Entrer le nombre à convertir : \n")
        if number_func.isnumeric():
            if int(number_func) > 0:
                return int(number_func)
        print("Ce n'est pas un nombre correct")
        return get_number()


    def get_final_base():
        base_func = input("Entrer la base de conversion : \n")
        if base_func.isnumeric():
            if int(base_func) > 0:
                return int(base_func)
        print("Ce n'est pas une base correcte")
        return get_final_base()


    def convert_number_to_base10(numbers_to_convert, base_initial):
        list_to_base10 = []
        number_to_base10 = 0
        a = 0
        for number in numbers_to_convert:
            list_to_base10.append(int(number) * (base_initial ** (int(len(numbers_to_convert)) - 1 - a)))

            a += 1

        for number in list_to_base10:
            number_to_base10 = number_to_base10 + number

        return number_to_base10


    def convert_base10_to_number(numbers_to_convert, base_final):
        result_list = []
        result = ""
        remaining_value = numbers_to_convert

        while True:
            if not remaining_value == 0:
                result_list.append(remaining_value % base_final)
                remaining_value = (remaining_value // base_final)
            else:
                break

        result_list.reverse()
        for number in result_list:
            result = result + str(number)

        return int(result)


    def traslate_in_index(number_to_translate):
        indexs = {
            "0": "₀", "1": "₁", "2": "₂", "3": "₃", "4": "₄", "5": "₅", "6": "₆",
            "7": "₇", "8": "₈", "9": "₉"}
        result = ""

        for number in str(number_to_translate):
            result = result + indexs[number]

        return result


    def convert(initial_base=None, numbers=None, final_base=None):
        if initial_base is None:
            initial_base = get_initial_base()
        if numbers is None:
            numbers = get_number()
        if final_base is None:
            final_base = get_final_base()

        numbers = str(numbers)
        result = convert_base10_to_number(convert_number_to_base10(numbers, initial_base), final_base)

        print("[" + str(numbers) + "]" + traslate_in_index(initial_base) + " = [" + str(result) + "]" + traslate_in_index(final_base))


    convert()
    input("Appuyer sur entrée pour quitter ...")


if __name__ == '__main__':
    main()