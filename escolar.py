alunos = [
    (1, "Ana Luiza", "9753", "3 A"),
    (2, "Aquiles Lima", "8642", "2 B"),
    (3, "Calebe Cardoso", "9853", "1 C"),
    (4, "Derek Luan", "5319", "3 B"),
    (5, "Gabriel Mendes", "8721", "2 A"),
    (6, "Heloisa Mendes", "9236", "1 A"),
    (7, "Ianne Dama", "1234", "3 C"),
    (8, "Jose Alencar", "5469", "2 C"),
    (9, "Sthefanny Carvalho", "9524", "1 B"),
    (10, "Yaren Silva", "9951", "3 A"),
]

professores = [
    (1, "Jessica Pereira", "Lingua Portuguesa"),
    (2, "Felipe Peixoto", "Matematica"),
    (3, "Pedro Ricardo", "Geografia"),
    (4, "Pablo Silva", "Historia"),
    (5, "Alessandra", "Biologia"),
    (6, "Glacilda", "Ingles"),
    (7, "Aurine", "Educacao Fisica"),
    (8, "Andreane", "Quimica"),
    (9, "Carlos Henrique", "Fisica"),
    (10, "Edilene", "Artes"),
]

materias = [
    (1, "Lingua Portuguesa", "80h", 1),
    (2, "Matematica", "80h", 2),
    (3, "Geografia", "60h", 3),
    (4, "Historia", "60h", 4),
    (5, "Biologia", "60h", 5),
    (6, "Ingles", "60h", 6),
    (7, "Educacao Fisica", "60h", 7),
    (8, "Quimica", "40h", 8),
    (9, "Fisica", "40h", 9),
    (10, "Artes", "40h", 10),
]

ids_professores = {p[0] for p in professores}
for m in materias:
    id_mat, _, _, id_prof = m
    assert id_prof in ids_professores, f"FK invalida: professor {id_prof} nao existe (materia {id_mat})"

def calcular_larguras(cabecalho, registros):
    larg = [len(str(c)) for c in cabecalho]
    for reg in registros:
        for i, val in enumerate(reg):
            larg[i] = max(larg[i], len(str(val)))
    return larg

def linha_sep(larg):
    return "+" + "+".join("-" * (l + 2) for l in larg) + "+"

def linha_dados(valores, larg):
    celulas = [" " + str(v).ljust(larg[i]) + " " for i, v in enumerate(valores)]
    return "|" + "|".join(celulas) + "|"

def formatar_tabela(nome, cabecalho, registros):
    larg = calcular_larguras(cabecalho, registros)
    sep = linha_sep(larg)
    larg_total = sum(larg) + len(larg) * 3 + 1
    titulo = " TABELA: " + nome.upper() + " "
    linhas = [
        sep,
        "|" + titulo.center(larg_total - 2) + "|",
        sep,
        linha_dados(cabecalho, larg),
        sep,
    ]
    for reg in registros:
        linhas.append(linha_dados(reg, larg))
    linhas.append(sep)
    return "\n".join(linhas)

cab_alunos = ["ID Aluno", "Nome Completo", "Matricula", "Turma"]
cab_professores = ["ID Professor", "Nome Completo", "Area de Atuacao"]
cab_materias = ["ID Materia", "Nome da Materia", "Carga Horaria", "ID Professor (FK)"]

with open("tabelas_escola.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("=" * 60 + "\n")
    arquivo.write("   SISTEMA ESCOLAR - DADOS FICTICIOS\n")
    arquivo.write("=" * 60 + "\n\n")
    arquivo.write(formatar_tabela("Alunos", cab_alunos, alunos))
    arquivo.write("\n\n")
    arquivo.write(formatar_tabela("Professores", cab_professores, professores))
    arquivo.write("\n\n")
    arquivo.write(formatar_tabela("Materias", cab_materias, materias))
    arquivo.write("\n\n")
    arquivo.write("-" * 60 + "\n")
    arquivo.write("RELACIONAMENTO:\n")
    arquivo.write("  - Materias.ID Professor (FK)  ->  Professores.ID Professor\n")
    arquivo.write("-" * 60 + "\n")

print('Arquivo "tabelas_escola.txt" gerado com sucesso!')
