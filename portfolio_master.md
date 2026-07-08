# Portfolio Master — Rodrigo Ary (Análise de Dados)

Documento de contexto e coordenação do portfólio completo. Este arquivo é a fonte de verdade sobre o estado, decisões e roadmap de todos os projetos. Cada projeto individual tem seu próprio `portfolio_project_<nome>.md` com detalhes técnicos e de negócio.

## Objetivo do portfólio

Demonstrar experiência prática como analista de dados em múltiplos contextos de negócio (varejo/ecommerce, finanças, marketing, operações, etc.) e múltiplos tipos de análise (exploratória, diagnóstica, preditiva, prescritiva), usando um stack realista: SQL, Python, dashboards de BI e Machine Learning.

## Convenções do portfólio

- **Um repositório GitHub por projeto**, nomeado `portfolio-<nome>` (ex: `portfolio-ecommerce`).
- Conta GitHub: `rodary-code`.
- Repositório de perfil `rodary-code/rodary-code` funciona como landing page (README renderizado automaticamente no perfil), listando e linkando todos os projetos.
- Cada projeto local vive em `C:\Users\Rodri\Documents\VS Claude Code - Portfolio\portfolio-<nome>\` e é seu próprio repositório git, independente.
- Cada projeto tem:
  - `portfolio_project_<nome>.md` — contexto interno (objetivo de negócio, dataset, decisões, metodologia, estado atual). Não é o README público.
  - `README.md` — apresentação pública do projeto (o que um recrutador/gestor vê no GitHub).
  - `data/raw` e `data/processed` — dados brutos e tratados (grandes volumes vão para `.gitignore`, mantendo apenas amostras ou instruções de download).
  - `notebooks/` — exploração e análise em Jupyter.
  - `src/` — scripts reutilizáveis (ETL, features, modelos).
  - `dashboard/` — artefatos de BI (Power BI/Tableau/Streamlit).
  - `reports/figures/` — gráficos e exports usados no README/relatório final.

## Estado do portfólio

| Projeto | Repositório | Contexto de negócio | Stack principal | Status |
|---|---|---|---|---|
| Ecommerce | [portfolio-ecommerce](https://github.com/rodary-code/portfolio-ecommerce) | Varejo online (vendas, logística, satisfação do cliente) | Python, ML, BI Dashboard | EDA inicial concluída |

## Roadmap / próximos projetos (ideias, não confirmados)

- Análise financeira (ex: crédito, inadimplência, fraude)
- Marketing/growth (ex: funil de aquisição, atribuição, churn de assinatura)
- Operações/supply chain
- RH/People Analytics

## Log de decisões

- **2026-07-08**: Definida estrutura de 1 repositório por projeto (em vez de monorepo), para dar destaque individual a cada projeto no GitHub.
- **2026-07-08**: Primeiro projeto definido como `portfolio-ecommerce`, usando o dataset público Olist Brazilian E-Commerce (relacional, ~100k pedidos, 2016-2018), com foco em Python (tratamento/análise), Machine Learning e Dashboard de BI.
- **2026-07-08**: EDA inicial do projeto ecommerce concluída. Achado-chave: atraso na entrega derruba a nota média de satisfação de 4,29 para 2,27 — forte candidato a alvo de modelagem preditiva na próxima etapa.
