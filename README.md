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
git clone https://github.com/DanielVinciguerra/Price-Action-Engine.git

# Instale as dependências
pip install -r requirements.txt
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

Suporte para reconhecimento automatizado de mais de 50 padrões fundamentais. Utilize através da interface: `PriceAction(df).candle_patterns['KEY']`.

### 🟢 Padrões Altistas (Bullish)

| Chave (Key) | Nome do Padrão | Explicação Breve |
| :--- | :--- | :--- |
| `MORNINGSTAR` | Morning Star | Reversão de alta em três candles no fundo de uma tendência. |
| `MORNINGDOJISTAR` | Morning Doji Star | Variante do Morning Star onde o candle central é um Doji. |
| `HAMMER` | Martelo | Reversão de alta; corpo pequeno no topo e sombra inferior longa. |
| `INVERTEDHAMMER` | Martelo Invertido | Reversão de alta; corpo pequeno no fundo e sombra superior longa. |
| `PIERCING` | Piercing Pattern | Candle de alta que abre abaixo da mínima e fecha acima do meio do candle anterior. |
| `THREEWHITESOLDIERS` | Três Soldados de Brancos | Três candles longos de alta em sequência, indicando reversão forte. |
| `THREEINSIDE` | Three Inside Up | Harami de alta seguido por um candle de rompimento de confirmação. |
| `THREEOUTSIDE` | Three Outside Up | Engolfo de alta seguido por um terceiro candle confirmando a tendência. |
| `ABANDONEDBABY` | Abandoned Baby | Padrão raro de reversão com um Doji isolado por gaps de ambos os lados. |
| `UNIQUETHREERIVER` | Unique 3 River | Padrão de reversão de alta com características específicas de corpo e sombra. |
| `LADDERBOTTOM` | Ladder Bottom | Reversão de alta rara que indica exaustão extrema do movimento vendedor. |
| `MATCHINGLOW` | Matching Low | Dois candles com fechos idênticos em uma mínima, indicando suporte forte. |
| `MATHOLD` | Mat Hold | Padrão de continuidade de alta extremamente confiável. |
| `RISEFALL3METHODS`| Rising/Falling Methods | Padrão de 5 candles indicando continuidade da tendência vigente. |
| `SEPARATINGLINES` | Separating Lines | Candles de cores opostas que compartilham o mesmo preço de abertura. |
| `TASUKIGAP` | Tasuki Gap | Continuidade; gap na tendência seguido por um candle que o fecha parcialmente. |
| `BELTHOLD` | Belt-hold | Candle único de força que pode indicar reversão ou continuidade. |
| `HOMINGPIGEON` | Homing Pigeon | Reversão; dois candles de baixa, onde o segundo está contido no primeiro. |
| `KICKING` | Kicking | Reversão poderosa; dois Marubozus com um gap entre eles. |
| `TAKURI` | Takuri | Doji libélula com sombra inferior extremamente longa; forte rejeição de preços. |

### 🔴 Padrões Baixistas (Bearish)

| Chave (Key) | Nome do Padrão | Explicação Breve |
| :--- | :--- | :--- |
| `SHOOTINGSTAR` | Estrela Cadente | Reversão de baixa; corpo pequeno no fundo e sombra superior longa. |
| `HANGINGMAN` | Enforcado | Forma de martelo no topo de uma tendência, indicando reversão para baixa. |
| `EVENINGSTAR` | Evening Star | Reversão de baixa em três candles no topo de uma tendência de alta. |
| `EVENINGDOJISTAR` | Evening Doji Star | Variante do Evening Star onde o candle central é um Doji. |
| `DARKCLOUDCOVER` | Nuvem Negra | Candle de baixa que abre acima da máxima e fecha fundo no corpo do anterior. |
| `THREEBLACKCROWS` | Três Corvos Negros | Três candles longos de baixa em sequência, indicando tendência forte de queda. |
| `TWOCROWS` | Dois Corvos | Dois candles de baixa após um longo candle de alta, com gap entre eles. |
| `UPSIDEGAPTWOCROWS`| Upside Gap Two Crows | Padrão de reversão que se forma após um gap de alta em tendência de subida. |
| `ADVANCEBLOCK` | Advance Block | Reversão de baixa; candles de alta com corpos decrescentes e sombras longas. |
| `IDENTICALTHREECROWS`| Corvos Idênticos | Variante dos três corvos onde as aberturas coincidem com os fechos. |
| `GRAVESTONEDOJI` | Doji Lápide | Doji de reversão de baixa; corpo na mínima com sombra superior longa. |
| `ONNECK` | On-Neck Pattern | Continuidade de baixa; candle de alta que fecha na mínima do candle anterior. |
| `INNECK` | In-Neck Pattern | Continuidade; similar ao On-Neck, mas fecha levemente dentro do corpo anterior. |
| `THREELINESTRIKE` | Three-Line Strike | Padrão de 4 candles onde três de alta são "atropelados" por um grande de baixa. |
| `THRUSTING` | Thrusting Pattern | Continuidade de baixa; candle de alta que fecha abaixo do meio do candle anterior. |
| `STALLEDPATTERN` | Stalled Pattern | Reversão de baixa indicando perda de momentum em tendência de alta. |
| `UPSIDEDOWNSIDEGAP` | Gap 3 Methods | Continuidade; gap seguido por um candle de cor oposta que preenche o gap. |

### ⚪ Indecisão e Estrutura

| Chave (Key) | Nome do Padrão | Explicação Breve |
| :--- | :--- | :--- |
| `DOJI` | Doji | Indecisão total do mercado; preços de abertura e fechamento iguais. |
| `LONGLEGGEDDOJI` | Doji de Pernas Longas | Alta indecisão; sombras longas para ambos os lados e corpo nulo. |
| `RICKSHAWMAN` | Rickshaw Man | Doji onde a abertura e fecho estão no centro exato do range do candle. |
| `SPINNINGTOP` | Pião (Spinning Top) | Indecisão; corpo real pequeno com sombras superior e inferior longas. |
| `HIGHWAVE` | High-Wave Candle | Indecisão extrema; sombras muito longas e corpo real minúsculo. |
| `MARUBOZU` | Marubozu | Força extrema; candle com sombras nulas ou mínimas em ambas as extremidades. |
| `CLOSINGMARUBOZU` | Closing Marubozu | Força; Marubozu onde o fecho coincide com a máxima ou mínima da barra. |
| `LONGLINE` | Long Line | Momentum forte; corpo real muito longo em relação às sombras. |
| `SHORTLINE` | Short Line | Perda de momentum; corpo real muito curto em relação às sombras. |
| `TRISTAR` | Tristar Pattern | Padrão de reversão raro composto por três Dojis consecutivos. |
| `HIKKAKE` | Hikkake Pattern | Usado para identificar falsos rompimentos (Bullish/Bearish). |
| `HIKKAKEMOD` | Hikkake Modificado | Variante avançada do Hikkake com critérios de confirmação adicionais. |
| `STICKSANDWICH` | Stick Sandwich | Reversão; dois candles com fechos iguais "ensanduichando" um oposto. |
| `BREAKAWAY` | Breakaway | Padrão de 5 candles que indica reversão após o rompimento de uma micro-tendência. |
| `COUNTERATTACK` | Contra-Ataque | Reversão; dois candles opostos que terminam com o mesmo preço de fechamento. |

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
├── files/                  # Diretório de dados
│   └── prices.csv          # Dados de exemplo (OHLCV)
├── technical_analysis/     # Core da biblioteca
│   ├── price_action.py     # Lógica de padrões e estrutura
│   ├── indicators.py       # Indicadores técnicos matemáticos
│   └── __init__.py         # Exportação de módulos
├── examples.py             # Scripts de demonstração
├── requirements.txt        # Dependências do projeto
├── LICENSE                 # Licença MIT
└── README.md               # Documentação principal
```

---

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir Issues ou enviar Pull Requests para novos indicadores ou melhorias algorítmicas.

## 📄 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

---
*Desenvolvido para traders e desenvolvedores que buscam precisão matemática no caos do mercado.*
