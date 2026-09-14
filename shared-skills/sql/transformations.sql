-- Templates de transformações SQL reutilizáveis

-- ============================================================================
-- AGREGAÇÕES E PIVOTS
-- ============================================================================

-- Template: Agregação por grupos
-- SELECT
--   group_column,
--   COUNT(*) as count,
--   AVG(numeric_col) as avg_value,
--   SUM(numeric_col) as total_value,
--   MAX(numeric_col) as max_value,
--   MIN(numeric_col) as min_value
-- FROM table_name
-- GROUP BY group_column
-- ORDER BY count DESC;


-- Template: Pivot (agregação em colunas)
-- SELECT
--   *
-- FROM (
--   SELECT row_column, pivot_column, value_column FROM table_name
-- )
-- PIVOT (SUM(value_column) FOR pivot_column IN ('category_1', 'category_2', 'category_3'))


-- ============================================================================
-- WINDOW FUNCTIONS
-- ============================================================================

-- Template: Rank e dense rank
-- SELECT
--   id,
--   sale_amount,
--   RANK() OVER (ORDER BY sale_amount DESC) as rank,
--   DENSE_RANK() OVER (ORDER BY sale_amount DESC) as dense_rank,
--   ROW_NUMBER() OVER (ORDER BY sale_amount DESC) as row_num
-- FROM sales


-- Template: Running total / Moving average
-- SELECT
--   date,
--   amount,
--   SUM(amount) OVER (ORDER BY date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) as running_total,
--   AVG(amount) OVER (ORDER BY date ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as moving_avg_7d
-- FROM transactions
-- ORDER BY date


-- Template: Year-over-year comparison
-- SELECT
--   EXTRACT(MONTH FROM date) as month,
--   EXTRACT(YEAR FROM date) as year,
--   SUM(amount) as total,
--   LAG(SUM(amount)) OVER (PARTITION BY EXTRACT(MONTH FROM date) ORDER BY EXTRACT(YEAR FROM date)) as prev_year_total
-- FROM sales
-- GROUP BY EXTRACT(YEAR FROM date), EXTRACT(MONTH FROM date)


-- ============================================================================
-- FEATURE ENGINEERING
-- ============================================================================

-- Template: Bins / Categorização
-- SELECT
--   id,
--   amount,
--   CASE
--     WHEN amount < 100 THEN 'Low'
--     WHEN amount BETWEEN 100 AND 500 THEN 'Medium'
--     ELSE 'High'
--   END as amount_category
-- FROM transactions


-- Template: Combinação de features
-- SELECT
--   id,
--   customer_id,
--   purchase_date,
--   DATEDIFF(day, previous_purchase_date, purchase_date) as days_since_last_purchase,
--   DATEDIFF(day, registration_date, purchase_date) as customer_lifetime_days
-- FROM sales
-- JOIN customers ON sales.customer_id = customers.id


-- ============================================================================
-- VALIDAÇÃO E QUALIDADE DE DADOS
-- ============================================================================

-- Template: Detecção de duplicatas
-- SELECT
--   id,
--   COUNT(*) as duplicate_count
-- FROM table_name
-- GROUP BY id
-- HAVING COUNT(*) > 1


-- Template: Verificação de missing values
-- SELECT
--   column_name,
--   COUNT(*) as total_rows,
--   SUM(CASE WHEN column_name IS NULL THEN 1 ELSE 0 END) as null_count,
--   ROUND(100.0 * SUM(CASE WHEN column_name IS NULL THEN 1 ELSE 0 END) / COUNT(*), 2) as null_percentage
-- FROM table_name
-- GROUP BY column_name


-- Template: Detecção de outliers (Z-score)
-- SELECT
--   id,
--   value,
--   (value - avg_value) / STDDEV(value) OVER () as z_score
-- FROM table_name
-- WHERE ABS((value - avg_value) / STDDEV(value) OVER ()) > 3
