# Passo a Passo
# Receber entradas do usuário para os horários
# Organizar em uma tabela
# Mostrar com interface gráfica
from horario import Disciplina

if __name__ == "__main__":
    dis = Disciplina("6T1345 3T5", "Ciencia")
    print(dis.get_times())
