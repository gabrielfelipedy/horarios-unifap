import pandas as pd

days = {
    "2": "Segunda",
    "3": "Terça",
    "4": "Quarta",
    "5": "Quinta",
    "6": "Sexta",
    "7": "Sábado"
}

class Table:
    def __init__(self) -> None:
        days_of_week = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
        horarios = ["1T", "2T", "3T", "4T", "5T", "1N", "2N", "3N", "4N", "5N"]

        self.__table = pd.DataFrame(index=horarios, columns=days_of_week)
        self.__table = self.__table.fillna("'")

    def insert(self, matter):
        times = matter['times']
        name = matter['name']

        if(len(times) == 0):
            print("Empty")
            return
        else:
            print(f"Achou {times}")

            for time in times:
                day_of_week = time[0]
                shift = time[1]
                horarios = time[2:]

                for h in horarios:
                    self.__table.loc[f"{h}{shift}", f"{days[day_of_week]}"] = name 
                

    def get_table(self):
        print(self.__table)
