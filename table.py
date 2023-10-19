import pandas as pd

class Table:
    def __init__(self) -> None:
        days_of_week = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
        horarios = ["1T", "2T", "3T", "4T", "5T", "1N", "2N", "3N", "4N", "5N"]
        self.table = pd.DataFrame(index=horarios, columns=days_of_week)
        self.table.loc[:, "Segunda"] = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
        self.table.loc[:, "Terça"] = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
        self.table.loc[:, "Quarta"] = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
        self.table.loc[:, "Quinta"] = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
        self.table.loc[:, "Sexta"] = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
        self.table.loc[:, "Sábado"] = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]

    def insert(self, matter):
        
        print(self.table)

        times = matter['times']
        if(len(times) == 0):
            print("Empty")
        else:
            print(f"Achou {times}")

            for time in times:
                day_of_week = time[0]
                shift = time[1]
                horarios = time[2:]

                print(f"""
dia da semana: {day_of_week}
turno: {shift}
horarios: {horarios}
                      """)
