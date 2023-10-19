# Passo a Passo
# Receber entradas do usuário para os horários
# Organizar em uma tabela
# Mostrar com interface gráfica
from horario import Horario

if __name__ == "__main__":
    horario = Horario("6T1345 3T5")
    print(horario.get_code())
