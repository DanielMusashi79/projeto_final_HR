"""
PROJETO FINAL - ANÁLISE EXPLORATÓRIA DE DADOS (EDA) COM PYTHON
Aluno: Daniel Roberto Cardoso
Curso: Visualização de Dados e Business Intelligence
Turma: T2

Este script realiza a leitura dos arquivos exportados do FreeSQL ('query_01.csv' e 'query_02.csv'),
executa análises estatísticas descritivas básicas e gera visualizações profissionais
para subsidiar decisões estratégicas de Recursos Humanos.
"""

# Importação das bibliotecas necessárias
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuração estética dos gráficos
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12

def processar_query_01(filepath):
    print("=" * 60)
    print(f"PROCESSANDO ARQUIVO: {filepath}")
    print("=" * 60)

    if not os.path.exists(filepath):
        print(f"Erro: O arquivo '{filepath}' não foi encontrado. Certifique-se de exportá-lo do FreeSQL.")
        return None
    
    # Carregar dados
    df = pd.read_csv(filepath)
    df.columns = df.columns.str.lower()
    print("\n---> Primeiras Linhas da Tabela:")
    print(df.head())

    # Métricas Estatísiticaas do Salário Geral
    salarios = df['salario']
    media = salarios.mean()
    mediana = salarios.median()
    minimo = salarios.min()
    maximo = salarios.max()
    desvio_padrao = salarios.std()

    print("\n---> Estatísticas Descritivas do Salário Geraal:")
    print(f"Média Salarial:     R$ {media:,.2f}")
    print(f"Mediana Salarial:   R$ {mediana:,.2f}")
    print(f"Salário Mínimo:     R$ {minimo:,.2f}")
    print(f"Salário Máximo:     R$ {maximo:,.2f}")
    print(f"Desvio Padrão:      R$ {desvio_padrao:,.2f}")

    # Estatística por Departamento
    print("\n---> Resumo Salarial por Departamento:")
    agg_dept = df.groupby('departamento')['salario'].agg(['count', 'mean', 'median', 'min', 'max']).reset_index()
    print(agg_dept.to_string(index=False))

    # --- VISUALIZAÇÕES ---
    # 1. Histograma de Distribuição Salarial Geral
    plt.figure(figsize=(10, 5))
    sns.histplot(df['salario'], kde=True, color='teal', bins=15)
    plt.axvline(media, color='red', linestyle='--', label=f'Média: R$ {media:,.0f}')
    plt.axvline(mediana, color='blue', linestyle='-', label=f'Mediana: R$ {mediana:,.0f}')
    plt.title('Distribuição Geral de Salários (Frequência)')
    plt.xlabel('Salário (R$)')
    plt.ylabel('Frequência de Funcionários')
    plt.legend()
    plt.tight_layout()
    plt.savefig('grafico_01_histograma_salarios.png', dpi=300)
    plt.close()
    print("\n[Sucesso] Histograma de Salários gerado e salvo como 'grafico_01_histograma_salarios.png'.")
    
    # 2. Boxplot de Salários por Departamento
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='departamento', y='salario', hue='departamento', legend=False, palette='Set2')
    plt.title('Dispersão Salarial por Departamento')
    plt.xlabel('Departamento')
    plt.ylabel('Salário (R$)')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('grafico_02_boxplot_departamento.png', dpi=300)
    plt.close()
    print("[Sucesso] Boxplot por Departamento gerado e salvo como 'grafico_02_boxplot_departamento.png'.")

    return df

def processar_query_02(filepath):
    print("\n" + "=" * 60)
    print(f"PROCESSANDO ARQUIVO: {filepath}")
    print("=" * 60)

    if not os.path.exists(filepath):
        print(f"Erro: O arquivo '{filepath}' não foi encontrado. Certifique-se de exportá-lo do FreeSQL.")
        return None
    
    df = pd.read_csv(filepath)
    df.columns = df.columns.str.lower()
    print("\n---> Primeiras Linhas da Tabela:")
    print(df.head())

    # Estatística de Funcionários por Região Geográfica
    print("\n---> Distribuição de Funcionários e Salário Médio por Região:")
    agg_regiao = df.groupby('regiao')['salario'].agg(['count', 'mean', 'median']).reset_index()
    print(agg_regiao.to_string(index=False))

    # --- VISUALIZAÇÕES ---
    # 3. Boxplot de Salário por Região Geográfica
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x='regiao', y='salario', hue='regiao', legend=False, palette='pastel')
    plt.title('Distribuição e Dispersão por Região Geográfica')
    plt.xlabel('Regiao')
    plt.ylabel('Salário (R$)')
    plt.tight_layout()
    plt.savefig('grafico_03_boxplot_regiao.png', dpi=300)
    plt.close()
    print("\n[Sucesso] Boxplot por Região gerado e salvo como 'grafico_03_boxplot_regiao.png'.")

    return df

if __name__ == "__main__":
    print("Iniciando Análise de Dados HR...")

    # Executar processamento
    df_salarios = processar_query_01('query_01.csv')
    df_regiao = processar_query_02('query_02.csv')

    print("\n" + "=" * 60)
    print("ANÁLISE FINALIZADA COM SUCESSO!")
    print("Todos os gráficos foram exportados no formato .png de alta resolução.")
    print("=" * 60)