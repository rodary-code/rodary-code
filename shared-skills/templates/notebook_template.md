# Análise de Dados — Template

**Projeto**: [Nome do Projeto]  
**Data**: [DD/MM/YYYY]  
**Análise**: [Descrição breve da análise]

---

## 1. Setup e Imports

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import sys

# Adicionar shared-skills ao path
sys.path.insert(0, '../../shared-skills/python')
from data_processing import cleaning, transformations
from visualization import plots
from ml import feature_engineering

# Configurar estilo
plots.set_style('seaborn-v0_8', 'Set2')
```

---

## 2. Carregamento de Dados

```python
# Carregar dados
df = pd.read_csv('../data/raw/dataset.csv')

# Verificação inicial
print(f"Shape: {df.shape}")
print(f"\nDtypes:\n{df.dtypes}")
print(f"\nPrimeiras linhas:\n{df.head()}")
print(f"\nInfo:\n{df.info()}")
```

---

## 3. Verificação de Qualidade

```python
# Missing values
print(f"Missing values:\n{df.isnull().sum()}")

# Duplicatas
duplicates = df.duplicated().sum()
print(f"Duplicatas: {duplicates}")

# Estatísticas descritivas
print(f"\nDescrição:\n{df.describe()}")
```

---

## 4. Exploração Exploratória (EDA)

### 4.1 Distribuições

```python
# Variáveis numéricas
numeric_cols = df.select_dtypes(include=['number']).columns
for col in numeric_cols:
    plots.plot_distribution(df[col], title=f'Distribuição de {col}')
    plt.show()
```

### 4.2 Correlações

```python
# Matriz de correlação
plots.plot_correlation_heatmap(df.select_dtypes(include=['number']))
plt.show()
```

### 4.3 Variáveis Categóricas

```python
# Contagem de categorias
categorical_cols = df.select_dtypes(include=['object']).columns
for col in categorical_cols:
    plots.plot_categorical(df[col], title=f'Contagem de {col}')
    plt.show()
```

### 4.4 Análises Customizadas

```python
# Adicionar suas análises específicas aqui
# Ex: segmentação por grupo, análise temporal, etc.
```

---

## 5. Limpeza e Transformação

```python
df_clean = df.copy()

# Remover duplicatas
df_clean = cleaning.remove_duplicates(df_clean)

# Tratar missing values
df_clean = cleaning.handle_missing_values(df_clean, strategy='drop')

# Detectar outliers
outliers = cleaning.detect_outliers(df_clean['valor_numerico'], method='iqr')
print(f"Outliers detectados: {outliers.sum()}")

# Codificar categóricas
df_clean = transformations.encode_categorical(df_clean, columns=['categoria'], method='label')

# Normalizar numéricas (se necessário)
df_clean = transformations.normalize_numeric(df_clean, columns=['valor_numerico'], method='minmax')

# Criar features de tempo (se aplicável)
df_clean = transformations.create_time_features(df_clean, 'data_coluna', features=['year', 'month', 'dow'])
```

---

## 6. Feature Engineering

```python
# Criar features de interação
df_features = feature_engineering.create_interaction_features(df_clean, [('col1', 'col2')])

# Criar features de razão
df_features = feature_engineering.create_ratio_features(df_features, [('numerador', 'denominador')])

# Binning
df_features = feature_engineering.create_binning_features(df_features, 'coluna_numerica', bins=5)
```

---

## 7. Análise Principal

```python
# Sua análise específica aqui
# Ex: agregações, análises de impacto, comparações, etc.

print("Resultado principal:")
# Adicionar interpretação e insights
```

---

## 8. Visualizações Finais

```python
# Gráficos para o relatório final
# Usar plots da shared-skills ou customizar conforme necessário
```

---

## 9. Conclusões

Summarizar os achados principais:

- **Insight 1**: [Descrição]
- **Insight 2**: [Descrição]
- **Insight 3**: [Descrição]

---

## 10. Próximos Passos

- [ ] Ação 1
- [ ] Ação 2
- [ ] Ação 3
