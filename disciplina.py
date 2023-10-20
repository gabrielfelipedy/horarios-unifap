import re

class Disciplina:
    def __valid_times(self, times):
        times = times.split(" ")
        valids = []

        for horario in times:
            horario_regex = re.compile(r'^([1-6])([ntNT])([1-5]){1,5}')
            result = horario_regex.search(horario)

            if result != None:
                valids.append(result.group(0))

        if(len(valids) != 0):
            return valids
        else:
            return []

    def __init__(self, times, name) -> None:
        self.__times = self.__valid_times(times)
        self.__name = name

    def get_times(self):
        return self.__times

    def join_table(self, table):
        ret = table.insert(
            {
                "times": self.__times, 
                "name": self.__name
            }
        )

        return ret;
