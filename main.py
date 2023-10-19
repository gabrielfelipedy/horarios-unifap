# Passo a Passo
# Receber entradas do usuário para os horários
# Organizar em uma tabela
# Mostrar com interface gráfica
from disciplina import Disciplina
from table import Table

if __name__ == "__main__":
    t = Table()

    while(True):
        name = str(input("Digite o nome da disciplina: "))
        horarios = str(input("Digite os horários: "))

        dis = Disciplina(horarios, name)
        dis.join_table(t)

        t.get_table()

        cont = str(input("Deseja continuar [s/n]? "))

        if cont.lower() == 'n': break
