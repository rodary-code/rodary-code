"""Funções de limpeza de dados."""
import pandas as pd
import numpy as np


def remove_duplicates(df: pd.DataFrame, subset: list = None, keep: str = 'first') -> pd.DataFrame:
    """Remove linhas duplicadas.

    Args:
        df: DataFrame a limpar
        subset: Colunas para considerar (None = todas)
        keep: 'first', 'last' ou False (remove todas as duplicatas)

    Returns:
        DataFrame sem duplicatas

    Example:
        >>> df_clean = remove_duplicates(df, subset=['id', 'email'])
    """
    return df.drop_duplicates(subset=subset, keep=keep)


def handle_missing_values(df: pd.DataFrame, strategy: str = 'drop', fill_value=None) -> pd.DataFrame:
    """Tratar valores faltantes.

    Args:
        df: DataFrame a processar
        strategy: 'drop', 'forward_fill', 'backward_fill' ou 'fill_value'
        fill_value: Valor para preenchimento (se strategy='fill_value')

    Returns:
        DataFrame com missing values tratados

    Example:
        >>> df_clean = handle_missing_values(df, strategy='drop')
    """
    if strategy == 'drop':
        return df.dropna()
    elif strategy == 'forward_fill':
        return df.fillna(method='ffill')
    elif strategy == 'backward_fill':
        return df.fillna(method='bfill')
    elif strategy == 'fill_value':
        return df.fillna(fill_value)
    else:
        raise ValueError(f"Strategy '{strategy}' not recognized")


def detect_outliers(series: pd.Series, method: str = 'iqr', threshold: float = 1.5) -> pd.Series:
    """Detectar outliers usando IQR ou z-score.

    Args:
        series: Série a analisar
        method: 'iqr' ou 'zscore'
        threshold: Múltiplo do IQR (se method='iqr') ou z-score (se method='zscore')

    Returns:
        Boolean Series indicando outliers

    Example:
        >>> outliers = detect_outliers(df['price'], method='iqr')
    """
    if method == 'iqr':
        Q1 = series.quantile(0.25)
        Q3 = series.quantile(0.75)
        IQR = Q3 - Q1
        return (series < Q1 - threshold * IQR) | (series > Q3 + threshold * IQR)
    elif method == 'zscore':
        z_scores = np.abs((series - series.mean()) / series.std())
        return z_scores > threshold
    else:
        raise ValueError(f"Method '{method}' not recognized")
