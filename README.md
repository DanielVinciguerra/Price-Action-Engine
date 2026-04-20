# Price Action Engine 📈

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://img.shields.io/badge/status-active-brightgreen.svg)]()

Implementação algorítmica robusta dos fundamentos de **Price Action** para análise automatizada da estrutura de mercado. Este motor foi projetado para identificar níveis técnicos críticos e fornecer insights baseados em dados para estratégias de negociação quantitativas e discricionárias.

---

## 🚀 Recursos Principais

- **Análise de Estrutura de Mercado**: Detecção automática de níveis de Suporte e Resistência dinâmicos.
- **Linhas de Tendência**: Identificação algorítmica de tendências de alta e baixa com filtragem de ruído.
- **Zonas de Oferta e Demanda**: Mapeamento de áreas de liquidez e interesse institucional.
- **Lógica Peak-to-Trough**: Algoritmo avançado para identificação de extremos (Topos e Fundos) significativos.
- **Velocidade de Preço**: Análise da dinâmica e momentum do movimento dos preços.

---

## 📋 Sumário
- [Instalação](#-instalação)
- [Exemplo Rápido](#-exemplo-rápido)
- [Indicadores Técnicos](#-indicadores-técnicos)
- [Padrões de Candlestick](#-identificação-de-padrões-de-candlestick)
- [Visualização](#-visualização-integrada)
- [Estrutura do Projeto](#-estrutura-do-projeto)

---

## 🛠️ Instalação

Certifique-se de ter o Python 3.8+ instalado.

```bash
# Clone o repositório
git clone https://github.com/DanielVinciguerra/technical-analysis.git

# Instale as dependências
pip install pandas numpy scipy plotly
```

---

## ⚡ Exemplo Rápido

Aqui está como você pode identificar padrões de velas em seus dados utilizando o motor `PriceAction`:

```python
from technical_analysis import PriceAction
import pandas as pd

# 1. Carregue seus dados OHLCV (open, high, low, close)
df = pd.read_csv("prices.csv")

# 2. Inicialize o motor de Price Action
pa = PriceAction(df)

# 3. Detecte padrões específicos usando acesso via dicionário
# Retorna o DataFrame com a coluna do sinal adicionada
df = pa.candle_patterns['MORNINGSTAR']
df = pa.candle_patterns['SHOOTINGSTAR']

# 4. Verifique os sinais (1: Alta, -1: Baixa, 0: Nenhum)
print(df[['date', 'MORNING_STAR', 'SHOOTING_STAR']].tail())
```

---

## 📊 Indicadores Técnicos

O motor possui uma biblioteca modular de indicadores agrupados por categoria:

### 🔹 Indicadores de Volume
| Indicador | Descrição |
| :--- | :--- |
| **OBV** | On-Balance Volume para medir pressão de volume acumulada. |
| **A/D Line** | Linha de Acumulação/Distribuição baseada no range do candle. |
| **ADOSC** | Oscilador Chaikin para antecipar mudanças no fluxo de capital. |

### 🔹 Indicadores de Momento
| Indicador | Descrição |
| :--- | :--- |
| **RSI** | Índice de Força Relativa para condições de sobrecompra/sobrevenda. |
| **ADX** | Medição da força da tendência atual. |
| **Stochastic** | Relação do fechamento com o range de preço. |
| **MACD** | Convergência e divergência de médias móveis. |

---

## 🕯️ Identificação de Padrões de Candlestick

Suporte para reconhecimento automatizado de mais de 50 padrões fundamentais. Você pode acessar qualquer padrão através da interface `PriceAction(df).candle_patterns['NOME_DO_PADRAO']`.

### 📋 Lista de Chaves Disponíveis

| Categoria | Chaves Técnicas (String Key) |
| :--- | :--- |
| **Altistas (Bullish)** | `MORNINGSTAR`, `MORNINGDOJISTAR`, `HAMMER`, `INVERTEDHAMMER`, `PIERCING`, `THREEWHITESOLDIERS`, `THREEINSIDE`, `THREEOUTSIDE`, `ABANDONEDBABY`, `UNIQUETHREERIVER`, `LADDERBOTTOM`, `MATCHINGLOW`, `MATHOLD`, `RISEFALL3METHODS`, `SEPARATINGLINES`, `TASUKIGAP`, `BELTHOLD`, `HOMINGPIGEON`, `KICKING` |
| **Baixistas (Bearish)** | `SHOOTINGSTAR`, `HANGINGMAN`, `EVENINGSTAR`, `EVENINGDOJISTAR`, `DARKCLOUDCOVER`, `THREEBLACKCROWS`, `TWOCROWS`, `UPSIDEGAPTWOCROWS`, `ADVANCEBLOCK`, `IDENTICALTHREECROWS`, `GRAVESTONEDOJI`, `ONNECK`, `INNECK`, `THREELINESTRIKE`, `UPSIDEDOWNSIDEGAPTHREEMETHODS`, `THRUSTING` |
| **Indecisão/Outros** | `DOJI`, `LONGLEGGEDDOJI`, `RICKSHAWMAN`, `SPINNINGTOP`, `HIGHWAVE`, `MARUBOZU`, `CLOSINGMARUBOZU`, `LONGLINE`, `SHORTLINE`, `HIKKAKE`, `HIKKAKEMOD`, `KICKINGBYLENGTH`, `STICKSANDWICH`, `COUNTERATTACK`, `BREAKAWAY`, `TAKURI`, `TRISTAR` |

---

<details>
<summary>🟢 <b>Descrição: Padrões Altistas (Bullish)</b></summary>

- **Reversão**: `Hammer`, `Inverted Hammer`, `Morning Star`, `Morning Doji Star`, `Piercing Pattern`, `Three White Soldiers`, `Three Inside Up`, `Three Outside Up`, `Abandoned Baby`, `Unique 3 River`, `Ladder Bottom`, `Matching Low`.
- **Continuidade**: `Mat Hold`, `Rising Three Methods`, `Separating Lines`, `Tasuki Gap`, `Belt-hold`, `Homing Pigeon`.
</details>

<details>
<summary>🔴 <b>Descrição: Padrões Baixistas (Bearish)</b></summary>

- **Reversão**: `Shooting Star`, `Hanging Man`, `Evening Star`, `Evening Doji Star`, `Dark Cloud Cover`, `Three Black Crows`, `Two Crows`, `Upside Gap Two Crows`, `Advance Block`, `Identical Three Crows`, `Gravestone Doji`.
- **Continuidade**: `On-Neck Pattern`, `In-Neck Pattern`, `Falling Three Methods`, `Three-Line Strike`, `Upside/Downside Gap Three Methods`.
</details>

<details>
<summary>⚪ <b>Descrição: Padrões de Indecisão e Estrutura</b></summary>

- **Indecisão**: `Doji`, `Long Legged Doji`, `Rickshaw Man`, `Spinning Top`, `High-Wave Candle`.
- **Força**: `Marubozu`, `Closing Marubozu`, `Long Line`, `Short Line`.
- **Outros**: `Hikkake`, `Hikkake Modified`, `Kicking`, `Stick Sandwich`, `Counterattack`, `Breakaway`.
</details>

---

## 📈 Visualização Integrada

O projeto é totalmente compatível com **Plotly**, permitindo a geração de gráficos financeiros interativos de nível profissional:

- Canais dinâmicos de suporte e resistência.
- Plotagem automática de sinais de candlestick.
- Templates em Dark Mode para terminais de negociação.

---

## 📂 Estrutura do Projeto

```text
price-action-engine/
├── technical_analysis/     # Core da biblioteca
│   ├── price_action.py     # Lógica de padrões e estrutura
│   ├── indicators.py       # Indicadores técnicos matemáticos
│   └── __init__.py         # Exportação de módulos
├── examples.py             # Scripts de demonstração
├── prices.csv              # Dados de exemplo (OHLCV)
└── README.md               # Documentação principal
```

---

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir Issues ou enviar Pull Requests para novos indicadores ou melhorias algorítmicas.

## 📄 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

---
*Desenvolvido para traders e desenvolvedores que buscam precisão matemática no caos do mercado.*
