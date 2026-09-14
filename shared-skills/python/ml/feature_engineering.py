"""Funções de feature engineering."""
import pandas as pd
import numpy as np


def create_interaction_features(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """Criar features de interação entre variáveis.

    Args:
        df: DataFrame
        columns: Pares de colunas para criar interação, ex: [('col1', 'col2')]

    Returns:
        DataFrame com novas colunas de interação

    Example:
        >>> df_inter = create_interaction_features(df, [('price', 'quantity')])
    """
    df_copy = df.copy()
    for col1, col2 in columns:
        df_copy[f'{col1}_x_{col2}'] = df_copy[col1] * df_copy[col2]
    return df_copy


def create_ratio_features(df: pd.DataFrame, ratios: list) -> pd.DataFrame:
    """Criar features de razão entre variáveis.

    Args:
        df: DataFrame
        ratios: Pares de colunas para criar razão, ex: [('numerator', 'denominator')]

    Returns:
        DataFrame com novas colunas de razão

    Example:
        >>> df_ratio = create_ratio_features(df, [('revenue', 'cost')])
    """
    df_copy = df.copy()
    for num, denom in ratios:
        df_copy[f'{num}_div_{denom}'] = df_copy[num] / (df_copy[denom].replace(0, np.nan))
    return df_copy


def create_binning_features(df: pd.DataFrame, column: str, bins: int = 5, labels: list = None) -> pd.DataFrame:
    """Binning de variável contínua em categorias.

    Args:
        df: DataFrame
        column: Coluna a binarizar
        bins: Número de bins ou lista de edges
        labels: Rótulos dos bins

    Returns:
        DataFrame com nova coluna binada

    Example:
        >>> df_bin = create_binning_features(df, 'age', bins=5, labels=['0-20', '20-40', '40-60', '60-80', '80+'])
    """
    df_copy = df.copy()
    df_copy[f'{column}_binned'] = pd.cut(df_copy[column], bins=bins, labels=labels)
    return df_copy
