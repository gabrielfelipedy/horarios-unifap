import re

class Horario:
    def __valid_code(self, code):
        code = code.split(" ")
        codes = []

        for horario in code:
            horario_regex = re.compile(r'^([1-7]){1,7}([ntNT])([1-5]){1,5}')
            result = horario_regex.search(horario)

            if result != None:
                codes.append(result.group(0))

        if(len(codes) != 0):
            return codes
        else:
            return []

    def __init__(self, code) -> None:
        self.__code = self.__valid_code(code)

    def get_code(self):
        return self.__code
