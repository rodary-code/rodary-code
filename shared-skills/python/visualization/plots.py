"""Funções de plotagem e configuração de estilo."""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def set_style(style: str = 'seaborn-v0_8', palette: str = 'husl') -> None:
    """Configurar estilo padrão para matplotlib/seaborn.

    Args:
        style: Estilo ('seaborn-v0_8', 'whitegrid', 'dark_background', etc.)
        palette: Paleta de cores ('husl', 'Set2', 'pastel', etc.)

    Example:
        >>> set_style('seaborn-v0_8', 'Set2')
    """
    sns.set_style(style)
    sns.set_palette(palette)
    plt.rcParams['figure.figsize'] = (12, 6)
    plt.rcParams['font.size'] = 10


def plot_distribution(series: pd.Series, title: str = '', bins: int = 30, ax=None) -> None:
    """Plotar distribuição de uma variável.

    Args:
        series: Série a plotar
        title: Título do gráfico
        bins: Número de bins para histograma
        ax: Matplotlib axis (None = cria novo)

    Example:
        >>> plot_distribution(df['price'], title='Distribuição de Preços')
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))

    ax.hist(series.dropna(), bins=bins, alpha=0.7, edgecolor='black')
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel('Valor')
    ax.set_ylabel('Frequência')
    plt.tight_layout()


def plot_categorical(series: pd.Series, title: str = '', ax=None) -> None:
    """Plotar contagem de categorias.

    Args:
        series: Série categórica a plotar
        title: Título do gráfico
        ax: Matplotlib axis (None = cria novo)

    Example:
        >>> plot_categorical(df['category'], title='Contagem por Categoria')
    """
    if ax is None:
        fig, ax = plt.subplots(figsize=(10, 6))

    series.value_counts().plot(kind='bar', ax=ax, color='skyblue', edgecolor='black')
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.set_xlabel('Categoria')
    ax.set_ylabel('Contagem')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()


def plot_correlation_heatmap(df: pd.DataFrame, figsize: tuple = (10, 8)) -> None:
    """Plotar matriz de correlação.

    Args:
        df: DataFrame com variáveis numéricas
        figsize: Tamanho da figura

    Example:
        >>> plot_correlation_heatmap(df.select_dtypes(include=['number']))
    """
    fig, ax = plt.subplots(figsize=figsize)
    corr = df.corr(numeric_only=True)
    sns.heatmap(corr, annot=True, fmt='.2f', cmap='coolwarm', center=0, ax=ax, cbar_kws={'label': 'Correlação'})
    ax.set_title('Matriz de Correlação', fontsize=14, fontweight='bold')
    plt.tight_layout()
