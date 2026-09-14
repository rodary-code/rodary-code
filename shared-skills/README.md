# Shared Skills — Portfólio de Análise de Dados

Repositório centralizado de funções, scripts e templates reutilizáveis entre os projetos do portfólio.

## Estrutura

### `python/`
Módulos Python reutilizáveis:
- **`data_processing/`** — Limpeza, transformação e preparação de dados (tratamento de missing, encoding, scaling, etc.)
- **`visualization/`** — Funções de plotagem e estilo padrão para gráficos
- **`ml/`** — Feature engineering, pipelines e utilidades de Machine Learning

### `sql/`
Templates e queries SQL reutilizáveis:
- Transformações comuns (pivots, agregações, window functions)
- Queries de validação e qualidade de dados
- Padrões para extração de features

### `templates/`
- Notebook template com estrutura padrão (EDA, limpeza, análise)
- Checklists e guias de análise
- Configurações de estilo/tema

## Como usar

### Importar funções Python
No seu notebook/script do projeto:

```python
import sys
sys.path.insert(0, '../../shared-skills/python')

from data_processing import cleaning, transformations
from visualization import plots

# Usar as funções
df_clean = cleaning.remove_duplicates(df)
plots.set_style('seaborn')
```

### Usar templates
Copie o template desejado para seu projeto e adapte conforme necessário:
```bash
cp ../../shared-skills/templates/notebook_template.ipynb notebooks/01_eda.ipynb
```

### Usar queries SQL
Abra o arquivo `.sql` correspondente e copie/adapte a query para seu caso.

## Convenções

- **Python**: Use type hints e docstrings sucintas
- **Naming**: snake_case para funções/variáveis, PascalCase para classes
- **Reutilização**: Se encontrar código repetido entre 2+ projetos, mova para shared-skills
- **Documentação**: Cada função deve ter um exemplo de uso no docstring

## Contribuir

Ao adicionar uma skill nova:
1. Coloque no módulo correto (`data_processing`, `visualization`, etc.)
2. Adicione docstring com exemplo
3. Considere se há testes (especialmente para `data_processing`)
4. Atualize este README com o que foi adicionado
