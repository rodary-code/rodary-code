# Checklist de Análise de Dados

Use este checklist como referência para estruturar uma análise completa de dados.

## 1. Entendimento do Problema

- [ ] Objetivo de negócio está claro?
- [ ] Qual é a pergunta principal a responder?
- [ ] Quem é o stakeholder? Que ação ele vai tomar com os insights?
- [ ] Qual é o escopo temporal (período de análise)?
- [ ] Existem restrições ou premissas críticas?

## 2. Coleta e Preparação de Dados

- [ ] Dados foram coletados corretamente?
- [ ] Tamanho da amostra é adequado?
- [ ] Período de análise está correto?
- [ ] Há dados faltantes (missings)? Em que volume?
- [ ] Há duplicatas? Removidas?
- [ ] Tipos de dados estão corretos?
- [ ] Nomes de colunas estão padronizados?

## 3. Análise Exploratória (EDA)

- [ ] Estatísticas descritivas geradas (média, mediana, desvio padrão, min, max)
- [ ] Distribuições verificadas para cada variável
- [ ] Correlações entre variáveis calculadas
- [ ] Outliers identificados e tratados
- [ ] Variações sazonais ou tendências detectadas
- [ ] Segmentações exploradas (por categoria, tempo, grupo, etc.)

## 4. Limpeza e Transformação

- [ ] Valores faltantes tratados (removidos, imputados ou marcados)
- [ ] Outliers tratados (removidos, winsorized ou transformados)
- [ ] Variáveis categóricas codificadas (label encoding, one-hot, etc.)
- [ ] Variáveis numéricas normalizadas/escaladas (se necessário)
- [ ] Features de tempo criadas (ano, mês, dia da semana, etc.)
- [ ] Features de interação criadas (se aplicável)
- [ ] Dados transformados estão prontos para análise/modelagem

## 5. Análise Principal

- [ ] Pergunta principal foi respondida?
- [ ] Insights secundários foram explorados?
- [ ] Padrões ou anomalias foram documentados?
- [ ] Causas potenciais foram investigadas?
- [ ] Comparações temporais foram feitas (se aplicável)?
- [ ] Validação cruzada ou testes de robustez realizados?

## 6. Validação

- [ ] Resultados fazem sentido do ponto de vista de negócio?
- [ ] Há evidência estatística suficiente?
- [ ] Tamanho do efeito é relevante?
- [ ] Limites da análise foram documentados?
- [ ] Possíveis vieses foram considerados?

## 7. Comunicação e Documentação

- [ ] Gráficos são claros e auto-explicativos?
- [ ] Títulos e rótulos estão em português/bem-formatados?
- [ ] Legendas explicam o que cada cores/símbolos representam?
- [ ] Códigos estão comentados e legíveis?
- [ ] README do projeto explica os arquivos e as etapas?
- [ ] Notebooks seguem ordem lógica (1_eda, 2_limpeza, 3_análise, etc.)?

## 8. Entrega Final

- [ ] README.md publicamente apresentável?
- [ ] Figuras/gráficos exportados para relatório?
- [ ] Conclusões e recomendações estão claras?
- [ ] Próximos passos ou limitações foram listados?
- [ ] Repositório está limpo e bem organizado?

---

**Dica**: Customize este checklist para seu caso específico. Use-o como guia, não como regra rígida.
