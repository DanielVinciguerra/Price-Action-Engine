import pandas as pd
import plotly.graph_objects as go
from technical_analysis import PriceAction

# ------------------------------------------------------------------------------------
# 1. Load Data
# ------------------------------------------------------------------------------------
# OHLCV data loading from CSV The file uses ';' as separator
df = pd.read_csv("./files/prices.csv", sep=";")

# ------------------------------------------------------------------------------------
# 2. Initialize Price Action Engine
# ------------------------------------------------------------------------------------
pa = PriceAction(df)

# ------------------------------------------------------------------------------------
# 3. Support and Resistance
# ------------------------------------------------------------------------------------
# Calculating dynamic support and resistance levels (staircase style)
df = pa.resistance(window=20)
df = pa.support(window=20)

# ------------------------------------------------------------------------------------
# 4. Candlestick Patterns
# ------------------------------------------------------------------------------------
# All patterns can be called via dictionary access: pa.candle_patterns['KEY']
# Identifying specific patterns:
df = pa.candle_patterns['ENGULFING']
df = pa.candle_patterns['HARAMI']
df = pa.candle_patterns['DOJI']
df = pa.candle_patterns['MARUBOZU']


