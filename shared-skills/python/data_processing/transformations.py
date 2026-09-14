"""Funções de transformação de dados."""
import pandas as pd


def encode_categorical(df: pd.DataFrame, columns: list, method: str = 'label') -> pd.DataFrame:
    """Codificar variáveis categóricas.

    Args:
        df: DataFrame
        columns: Colunas categóricas a codificar
        method: 'label' (0, 1, 2...) ou 'onehot'

    Returns:
        DataFrame com variáveis codificadas

    Example:
        >>> df_encoded = encode_categorical(df, columns=['gender'], method='label')
    """
    df_copy = df.copy()
    if method == 'label':
        for col in columns:
            df_copy[col] = pd.factorize(df_copy[col])[0]
    elif method == 'onehot':
        df_copy = pd.get_dummies(df_copy, columns=columns)
    return df_copy


def normalize_numeric(df: pd.DataFrame, columns: list, method: str = 'minmax') -> pd.DataFrame:
    """Normalizar variáveis numéricas.

    Args:
        df: DataFrame
        columns: Colunas numéricas a normalizar
        method: 'minmax' (0-1) ou 'zscore'

    Returns:
        DataFrame com variáveis normalizadas

    Example:
        >>> df_norm = normalize_numeric(df, columns=['price', 'quantity'])
    """
    df_copy = df.copy()
    for col in columns:
        if method == 'minmax':
            min_val = df_copy[col].min()
            max_val = df_copy[col].max()
            df_copy[col] = (df_copy[col] - min_val) / (max_val - min_val)
        elif method == 'zscore':
            mean = df_copy[col].mean()
            std = df_copy[col].std()
            df_copy[col] = (df_copy[col] - mean) / std
    return df_copy


def create_time_features(df: pd.DataFrame, date_column: str, features: list = None) -> pd.DataFrame:
    """Criar features a partir de coluna de data.

    Args:
        df: DataFrame
        date_column: Nome da coluna de data
        features: Lista de features a criar (['year', 'month', 'day', 'dow', 'quarter'])

    Returns:
        DataFrame com novas colunas de tempo

    Example:
        >>> df_time = create_time_features(df, 'purchase_date', features=['year', 'month', 'dow'])
    """
    if features is None:
        features = ['year', 'month', 'day', 'dow']

    df_copy = df.copy()
    df_copy[date_column] = pd.to_datetime(df_copy[date_column])

    if 'year' in features:
        df_copy[f'{date_column}_year'] = df_copy[date_column].dt.year
    if 'month' in features:
        df_copy[f'{date_column}_month'] = df_copy[date_column].dt.month
    if 'day' in features:
        df_copy[f'{date_column}_day'] = df_copy[date_column].dt.day
    if 'dow' in features:
        df_copy[f'{date_column}_dow'] = df_copy[date_column].dt.dayofweek
    if 'quarter' in features:
        df_copy[f'{date_column}_quarter'] = df_copy[date_column].dt.quarter

    return df_copy
