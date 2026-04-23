alunos = [
    (1,  "Ana Luiza",  "9753", "3º A"),
    (2,  "Aquiles Lima",    "8642", "2º B"),
    (3,  "Calebe Cardoso",         "9853", "1º C"),
    (4,  "Derek Luan",        "5319", "3º B"),
    (5,  "Gabriel Mendes",     "8721", "2º A"),
    (6,  "Heloisa Mendes",   "9236", "1º A"),
    (7,  "Ianne Dama",      "1234", "3º C"),
    (8,  "José Alencar",       "5469", "2º C"),
    (9,  "Sthefanny Carvalho",        "9524", "1º B"),
    (10, "Yaren Silva",    "9951", "3º A"),
]

professores = [
    (1,  "Jéssica Pereira",    "Língua Portuguesa"),
    (2,  "Felipe Peixoto",     "Matemática"),
    (3,  "Pedro Ricardo",      "Geografia"),
    (4,  "Pablo Silva",      "História"),
    (5,  "Alessandra",  "Biologia"),
    (6,  "Glacilda",    "Inglês"),
    (7,  "Aurine",   "Educação Física"),
    (8,  "Andreane",      "Química"),
    (9,  "Carlos Henrique",    "Física"),
    (10, "Edilene",       "Artes"),
]

materias = [
    (1,  "Língua Portuguesa",        "80h", 1),
    (2,  "Matemática", "80h", 2),
    (3,  "Geografia",          "60h", 3),
    (4,  "História",          "60h", 4),
    (5,  "Biologia",            "60h", 5),
    (6,  "Inglês",           "60h", 6),
    (7,  "Educação Física",         "60h", 7),
    (8,  "Química",         "40h", 8),
    (9,  "Física",   "40h", 9),
    (10, "Artes",             "40h", 10),
]

ids_alunos = {a[0] for a in alunos}

for m in materias:
    id_mat, _, _, id_aluno = m
    assert id_aluno in ids_alunos, f"FK inválida: aluno {id_aluno} não existe (matéria {id_mat})"

def calcular_larguras(cabecalho, registros):
    larg = [len(str(c)) for c in cabecalho]
    for reg in registros:
        for i, val in enumerate(reg):
            larg[i] = max(larg[i], len(str(val)))
    return larg

def linha_sep(larg):
    return "+" + "+".join("-" * (l + 2) for l in larg) + "+"

def linha_dados(valores, larg):
    celulas = [f" {str(v):<{larg[i]}} " for i, v in enumerate(valores)]
    return "|" + "|".join(celulas) + "|"

def formatar_tabela(nome, cabecalho, registros):
    larg       = calcular_larguras(cabecalho, registros)
    sep        = linha_sep(larg)
    larg_total = sum(larg) + len(larg) * 3 + 1
    titulo     = f" TABELA: {nome.upper()} "
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

cab_alunos      = ["ID Aluno", "Nome Completo", "Matrícula", "Turma"]
cab_professores = ["ID Professor", "Nome Completo", "Área de Atuação"]
cab_materias    = ["ID Matéria", "Nome da Matéria", "Carga Horária", "ID Aluno (FK)"]

with open("tabelas_escola.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("=" * 60 + "\n")
    arquivo.write("   SISTEMA ESCOLAR — DADOS FICTÍCIOS\n")
    arquivo.write("=" * 60 + "\n\n")
    arquivo.write(formatar_tabela("Alunos", cab_alunos, alunos))
    arquivo.write("\n\n")
    arquivo.write(formatar_tabela("Professores", cab_professores, professores))
    arquivo.write("\n\n")
    arquivo.write(formatar_tabela("Matérias", cab_materias, materias))
    arquivo.write("\n\n")
    arquivo.write("-" * 60 + "\n")
    arquivo.write("RELACIONAMENTO:\n")
    arquivo.write("  - Materias.ID Aluno (FK)  ->  Alunos.ID Aluno\n")
    arquivo.write("-" * 60 + "\n")

print('Arquivo "tabelas_escola.txt" gerado com sucesso!')
