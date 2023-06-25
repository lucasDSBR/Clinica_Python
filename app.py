import dbConection
def refistrarPaciente():
	print("NOVO PACIENTE")
	print("================================")
	print("DADOS DO PACIENTE:")
	nome = input("Nome do paciente: ")
	idade = input("Idade do paciente: ")
	dbConection.registrarPacienteDb(nome, idade)
	menu()

def refistrarMedico():
	print("NOVO MÉDICO")
	print("================================")
	print("DADOS DO MÉDICO:")
	nome = input("Nome do medico: ")
	idade = input("Idade do medico: ")
	dbConection.refistrarMedicoDb(nome, idade)
	menu()


def refistrarAgendamento():
	print("NOVO AGENDAMENTO")
	print("================================")
	dbConection.buscarMedicos()
	dbConection.buscarPacientes()
	print("DADOS DO AGENDAMENTO:")
	descAtendimento = input("Descicao do agendamento: ")
	idMedico = input("Codico do medico: ")
	idPaciente = input("Codico do paciente: ")
	dbConection.refistrarAgendamentoDb(descAtendimento, idMedico, idPaciente)
	menu()


def menu():
	print("""
		Bem Vindo a Cílina MONDI
		Escolha uma opção para dar proceguimento no atendimento:

		1) Registrar Paciente;
		2) Registrar Médico;
		3) Registrar Agendamento de Consultas;
		4) Relatórios
	""")
	opcao = input("Opção: ")
	if(opcao == "1"):
		refistrarPaciente()
	if(opcao == "2"):
		refistrarMedico()
	if(opcao == "3"):
		refistrarAgendamento()
	if(opcao == "4"):
		menu()

def main():
	menu()


if __name__ == '__main__':
	main()