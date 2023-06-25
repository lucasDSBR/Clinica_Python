import mysql.connector

mydb = mysql.connector.connect(
	host='',
	user='',
	password='',
	database=''
)


con = mydb.cursor()

'Criando tabelas iniciais'
con.execute(("""
	CREATE TABLE IF NOT EXISTS pacientes (
		id INT AUTO_INCREMENT PRIMARY KEY,
		nome VARCHAR(100),
		idade INT);
	"""))
con.execute(("""
	CREATE TABLE IF NOT EXISTS medicos (
		id INT AUTO_INCREMENT PRIMARY KEY,
		nome VARCHAR(100),
		idade INT);
	"""))
con.execute(("""
	CREATE TABLE IF NOT EXISTS agendamentos (
		id INT AUTO_INCREMENT PRIMARY KEY,
		descAtendimento VARCHAR(100),
		idMedico INT,
		FOREIGN KEY (idMedico) REFERENCES medicos(id),
		idPaciente INT,
		FOREIGN KEY (idPaciente) REFERENCES pacientes(id)
	);"""))



def registrarPacienteDb(nome, idade):
	con.execute(("INSERT INTO pacientes (nome, idade) VALUES ('"+ nome +"', "+ idade +");"))
	mydb.commit()

def refistrarMedicoDb(nome, idade):
	con.execute(("INSERT INTO medicos (nome, idade) VALUES ('"+ nome +"', "+ idade +");"))
	mydb.commit()

def refistrarAgendamentoDb(descAtendimento, idMedico, idPaciente):
	con.execute(("INSERT INTO agendamentos (descAtendimento, idMedico, idPaciente) VALUES ('"+ descAtendimento +"', "+ idMedico +", "+ idPaciente +");"))
	mydb.commit()

def buscarMedicos():
	con.execute(("SELECT * FROM medicos"))
	print("===== LISTA DE MÉDICOS =====")
	print("Codigo\tNome\tIdade")
	for (medico) in con:
		print(str(medico[0]) + "\t" + medico[1] + "\t" + str(medico[2]))
	print("==============================")

def buscarPacientes():
	con.execute(("SELECT * FROM pacientes"))
	print("===== LISTA DE PACIENTES =====")
	print("Codigo\tNome\tIdade")
	for (medico) in con:
		print(str(medico[0]) + "\t" + medico[1] + "\t" + str(medico[2]))
	print("==============================")