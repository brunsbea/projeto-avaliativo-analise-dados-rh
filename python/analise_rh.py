# ============================================
# Projeto Avaliativo - Análise de Dados de RH
# Autor: Beatriz Rocha Bruns
# ============================================

# Importação das bibliotecas
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Caminho da raiz do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Caminhos para os CSVs
query1 = pd.read_csv(BASE_DIR / "data" / "query_01.csv")
query2 = pd.read_csv(BASE_DIR / "data" / "query_02.csv")

print("Arquivos carregados com sucesso!\n")
print(f"Query 1: {len(query1)} registros")
print(f"Query 2: {len(query2)} registros")

# ============================================
# Conhecendo os dados
# ============================================

print("\n================ QUERY 1 ================\n")

print("Primeiras linhas:")
print(query1.head())

print("\nInformações da tabela:")
print(query1.info())

print("\nResumo estatístico:")
print(query1.describe())

print("\nValores nulos:")
print(query1.isnull().sum())

print("\n================ QUERY 2 ================\n")

print("Primeiras linhas:")
print(query2.head())

print("\nInformações da tabela:")
print(query2.info())

print("\nResumo estatístico:")
print(query2.describe())

print("\nValores nulos:")
print(query2.isnull().sum())

# ============================================
# Análise 1 - Salário médio por departamento
# ============================================

salario_departamento = (
    query1.groupby("DEPARTMENT_NAME")["SALARY"]
    .mean()
    .sort_values(ascending=False)
)

print("\n===== Salário médio por departamento =====\n")
print(salario_departamento)

# ============================================
# Análise 2 - Salário médio por cargo
# ============================================

salario_cargo = (
    query1.groupby("JOB_TITLE")["SALARY"]
    .mean()
    .sort_values(ascending=False)
)

print("\n===== Salário médio por cargo =====\n")
print(salario_cargo)

# ============================================
# Análise 3 - Funcionários por região
# ============================================

funcionarios_regiao = (
    query2["REGION_NAME"]
    .value_counts()
)

print("\n===== Funcionários por região =====\n")
print(funcionarios_regiao)

# ============================================
# Análise 4 - Média salarial por região
# ============================================

media_regiao = (
    query2.groupby("REGION_NAME")["SALARY"]
    .mean()
    .sort_values(ascending=False)
)

print("\n===== Média salarial por região =====\n")
print(media_regiao)

# ============================================
# Análise 5 - Estatísticas dos salários
# ============================================

print("\n===== Estatísticas dos salários =====")

print(f"Média: {query1['SALARY'].mean():.2f}")
print(f"Mediana: {query1['SALARY'].median():.2f}")
print(f"Mínimo: {query1['SALARY'].min():.2f}")
print(f"Máximo: {query1['SALARY'].max():.2f}")

# ============================================
# Gráfico 1 - Salário médio por departamento
# ============================================

plt.figure(figsize=(10, 6))

salario_departamento.plot(kind="bar")

plt.title("Salário médio por departamento")
plt.xlabel("Departamento")
plt.ylabel("Salário médio")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.show()

# ============================================
# Gráfico 2 - Funcionários por região
# ============================================

plt.figure(figsize=(6, 5))

funcionarios_regiao.plot(kind="bar")

plt.title("Quantidade de funcionários por região")
plt.xlabel("Região")
plt.ylabel("Quantidade de funcionários")

plt.xticks(rotation=0)

plt.tight_layout()

plt.show()

# ==========================================
# Gráfico 3 - Salário médio por região
# ==========================================

media_salario_regiao = query2.groupby("REGION_NAME")["SALARY"].mean().sort_values(ascending=False)

plt.figure(figsize=(6,4))
media_salario_regiao.plot(kind="bar")

plt.title("Salário médio por região")
plt.xlabel("Região")
plt.ylabel("Salário médio")

plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

# ==========================================
# Gráfico 4 - Histograma dos salários
# ==========================================

plt.figure(figsize=(8,5))

plt.hist(query1["SALARY"], bins=10, edgecolor="black")

plt.title("Distribuição dos salários")
plt.xlabel("Salário")
plt.ylabel("Quantidade de funcionários")

plt.tight_layout()
plt.show()