from scipy import signal
import pandas as pd
import numpy as np
from enum import Enum



class CandlePatterns:
    """
    A class containing various candlestick pattern recognition methods.

    This class provides methods to identify common candlestick patterns in financial
    time series data using pandas DataFrames.
    """
    def __init__(self, data: pd.DataFrame):
        self._data = data

    @property
    def dataframe(self) -> pd.DataFrame:
        return self._data
    
    @dataframe.setter
    def dataframe(self, data: pd.DataFrame):
        self._data = data

    def __getitem__(self, key: str) -> pd.DataFrame:
        """
        Calls a candlestick pattern method by name.

        Args:
            key (str): The name of the pattern method (e.g., 'two_crows').

        Returns:
            pd.DataFrame: The DataFrame with the pattern signal column.
        """
        pattern_method = getattr(self, key, None)
        if pattern_method and callable(pattern_method):
            return pattern_method(self.dataframe)
        
        raise KeyError(f"Pattern '{key}' not found.")

    # ------------------------------------------------------------------------------------------ #
    # CDL2CROWS - Two Crows
    # ------------------------------------------------------------------------------------------ #
    def TWOCROWS(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Two Crows (CDL2CROWS).
        A bearish reversal pattern that consists of two black (bearish) candles after 
        a long white (bullish) candle, with a gap between the first and second candles.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'TWO_CROWS' column (-1: bearish, 0: no pattern).
        """
        data['TWO_CROWS'] = np.where((data['open'] > data['close'].shift()) &
                    (data['close'].shift() > data['open'].shift()) &
                    (data['open'].shift() > data['close'].shift(2)) &
                    (data['close'] < data['open']), -1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDL3BLACKCROWS - Three Black Crows
    # ------------------------------------------------------------------------------------------ #
    def THREEBLACKCROWS(self, data: pd.DataFrame ) -> pd.DataFrame:
        """
        Three Black Crows (CDL3BLACKCROWS).
        A bearish reversal pattern consisting of three long, bearish candles that 
        close near their lows and trend downward.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'THREE_BLACK_CROWS' column (-1: bearish, 0: no pattern).
        """
        data['THREE_BLACK_CROWS'] = np.where((data['close'].shift(2) > data['open'].shift(2)) &
                    (data['close'].shift(1) > data['open'].shift(1)) &
                    (data['close'] > data['open']) &
                    (data['close'].shift(2) > data['close'].shift(1)) &
                    (data['close'].shift(1) > data['close']), -1, 0)
        return data
    
    # ------------------------------------------------------------------------------------------ #
    # CDL3INSIDE - Three Inside Up/Down
    # ------------------------------------------------------------------------------------------ #
    def THREEINSIDE(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Three Inside Up/Down (CDL3INSIDE).
        A reversal pattern that indicates a trend change, consisting of a harami 
        followed by a breakout candle. This implementation focuses on the bullish variant.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'THREE_INSIDE' column (1: bullish reversal, 0: no pattern).
        """
        data['THREE_INSIDE'] = np.where((data['close'].shift(2) > data['open'].shift(2)) &
                    (data['open'].shift(1) > data['high'].shift(2)) &
                    (data['low'].shift(1) < data['low'].shift(2)) &
                    (data['close'].shift(1) > data['high'].shift(1)) &
                    (data['low'] < data['low'].shift(1)) &
                    (data['close'] > data['open']), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDL3LINESTRIKE - Three-Line Strike
    # ------------------------------------------------------------------------------------------ #
    def THREELINESTRIKE(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Three-Line Strike (CDL3LINESTRIKE).
        A four-candle continuation pattern. This implementation detects a bearish strike 
        where three bullish candles are "struck" by a large bearish candle.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'THREE_LINE_STRIKE' column (-1: bearish, 0: no pattern).
        """
        data['THREE_LINE_STRIKE'] = np.where((data['close'].shift(3) > data['open'].shift(3)) &
                    (data['close'].shift(2) > data['open'].shift(2)) &
                    (data['close'].shift(1) > data['open'].shift(1)) &
                    (data['close'] < data['open']) &
                    (data['close'].shift(3) < data['low'].shift(2)) &
                    (data['close'].shift(2) < data['low'].shift(1)) &
                    (data['close'].shift(1) < data['low']), -1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDL3OUTSIDE - Three Outside Up/Down
    # ------------------------------------------------------------------------------------------ #
    def THREEOUTSIDE(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Three Outside Up/Down (CDL3OUTSIDE).
        A reversal pattern consisting of a two-candle engulfing pattern followed 
        by a third confirming candle. This implementation identifies the bullish variant.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'THREE_OUTSIDE' column (1: bullish reversal, 0: no pattern).
        """
        data['THREE_OUTSIDE'] = np.where((data['close'].shift(2) > data['open'].shift(2)) &
                    (data['close'].shift(1) > data['open'].shift(1)) &
                    (data['close'] > data['open']) &
                    (data['close'].shift(2) < data['open'].shift(1)) &
                    (data['close'].shift(1) < data['open']), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDL3STARSINSOUTH - Three Stars In The South
    # ------------------------------------------------------------------------------------------ #
    def THREESTARSINSOUTH(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Three Stars in the South (CDL3STARSINSOUTH).
        A bullish reversal pattern that appears during a downtrend, showing weakening bearish momentum.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: Original DataFrame with 'THREE_STARS_IN_SOUTH' column (1 for bullish, 0 otherwise).
        """
        data['THREE_STARS_IN_SOUTH'] = np.where((data['close'].shift(2) > data['open'].shift(2)) &
                    (data['close'].shift(1) > data['open'].shift(1)) &
                    (data['close'] > data['open']) &
                    (data['close'].shift(2) < data['close'].shift(1)) &
                    (data['close'].shift(1) < data['close']) &
                    (data['close'] < data['close'].shift(1)), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDL3WHITESOLDIERS - Three Advancing White Soldiers
    # ------------------------------------------------------------------------------------------ #
    def THREEWHITESOLDIERS(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Three Advancing White Soldiers (CDL3WHITESOLDIERS).
        A bullish reversal pattern consisting of three long, bullish candles that trend upward.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: Original DataFrame with 'THREE_WHITE_SOLDIERS' column (1 for bullish, 0 otherwise).
        """
        data['THREE_WHITE_SOLDIERS'] = np.where((data['close'].shift(2) < data['open'].shift(2)) &
                    (data['close'].shift(1) < data['open'].shift(1)) &
                    (data['close'] < data['open']) &
                    (data['close'].shift(2) < data['close'].shift(1)) &
                    (data['close'].shift(1) < data['close']) &
                    (data['close'] > data['close'].shift(1)), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLABANDONEDBABY - Abandoned Baby
    # ------------------------------------------------------------------------------------------ #
    def ABANDONEDBABY(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Abandoned Baby (CDLABANDONEDBABY).
        A rare reversal pattern characterized by a doji preceded and followed by gaps.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: Original DataFrame with 'ABANDONED_BABY' column (1 for signal, 0 otherwise).
        """
        data['ABANDONED_BABY'] = np.where((data['close'].shift(2) > data['open'].shift(2)) &
                    (data['low'].shift(2) > data['high'].shift(1)) &
                    (data['low'].shift(1) < data['high'].shift(1)) &
                    (data['close'] < data['open']) &
                    (data['low'] < data['low'].shift(1)), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLADVANCEBLOCK - Advance Block
    # ------------------------------------------------------------------------------------------ #
    def ADVANCEBLOCK(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Advance Block (CDLADVANCEBLOCK).
        A bearish reversal pattern that appears in an uptrend, characterized by 
        consecutive bullish candles with shortening real bodies and long upper wicks.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'ADVANCE_BLOCK' column (-1: bearish reversal, 0: no pattern).
        """
        data['ADVANCE_BLOCK'] = np.where((data['close'].shift(2) < data['open'].shift(2)) &
                    (data['close'].shift(1) < data['open'].shift(1)) &
                    (data['close'] < data['open']) &
                    ((data['close'].shift(2) - data['open'].shift(2)) / (data['high'].shift(2) - data['low'].shift(2)) < 0.3) &
                    ((data['close'].shift(1) - data['open'].shift(1)) / (data['high'].shift(1) - data['low'].shift(1)) < 0.3) &
                    ((data['close'] - data['open']) / (data['high'] - data['low']) < 0.3), -1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLBELTHOLD - Belt-hold
    # ------------------------------------------------------------------------------------------ #
    def BELTHOLD(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Belt-hold (CDLBELTHOLD).
        A single candle pattern that can indicate a reversal or continuation.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: Original DataFrame with 'BELT_HOLD' column (1 for signal, 0 otherwise).
        """
        data['BELT_HOLD'] = np.where((data['close'].shift() < data['open'].shift()) &
                    ((data['high'].shift() - data['low'].shift()) / data['low'].shift() < 0.01) &
                    (data['close'] > data['open']), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLBREAKAWAY - Breakaway
    # ------------------------------------------------------------------------------------------ #
    def BREAKAWAY(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Breakaway (CDLBREAKAWAY).
        A five-candle reversal pattern that breaks out of a small trend.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: Original DataFrame with 'BREAKAWAY' column (1 for signal, 0 otherwise).
        """
        data['BREAKAWAY'] = np.where((data['close'].shift(4) < data['open'].shift(4)) &
                    (data['close'].shift(3) < data['open'].shift(3)) &
                    (data['close'].shift(2) < data['open'].shift(2)) &
                    (data['close'].shift(1) < data['open'].shift(1)) &
                    (data['close'] > data['open']), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLCLOSINGMARUBOZU - Closing Marubozu
    # ------------------------------------------------------------------------------------------ #
    def CLOSINGMARUBOZU(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Closing Marubozu (CDLCLOSINGMARUBOZU).
        A marubozu candle where either the high or the low is the closing price.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: Original DataFrame with 'CLOSING_MARUBOZU' column (1 for signal, 0 otherwise).
        """
        data['CLOSING_MARUBOZU'] = np.where((data['open'] == data['high']) &
                    (data['close'] == data['low']), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLCONCEALBABYSWALL - Concealing Baby Swallow
    # ------------------------------------------------------------------------------------------ #
    def CONCEALINGBABYSWALL(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Concealing Baby Swallow (CDLCONCEALBABYSWALL).
        A bullish reversal pattern consisting of four candles in a downtrend.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: Original DataFrame with 'CONCEALING_BABY_SWALLOW' column (1 for bullish, 0 otherwise).
        """
        data['CONCEALING_BABY_SWALLOW'] = np.where((data['close'].shift(4) > data['open'].shift(4)) &
                    (data['close'].shift(3) > data['open'].shift(3)) &
                    (data['close'].shift(2) > data['open'].shift(2)) &
                    (data['close'].shift(1) > data['open'].shift(1)) &
                    (data['close'] < data['open']) &
                    (data['high'] < data['open']) &
                    (data['low'] > data['close'].shift(4)) &
                    (data['high'] > data['close'].shift(4)), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLCOUNTERATTACK - Counterattack
    # ------------------------------------------------------------------------------------------ #
    def COUNTERATTACK(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Counterattack (CDLCOUNTERATTACK).
        A reversal pattern where two candles of opposite color have the same closing price.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: Original DataFrame with 'COUNTERATTACK' column (1 for signal, 0 otherwise).
        """
        data['COUNTERATTACK'] = np.where((data['close'].shift(1) > data['open'].shift(1)) &
                    (data['close'] < data['open']) &
                    (data['high'] > data['high'].shift(1)) &
                    (data['low'] < data['low'].shift(1)), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLDARKCLOUDCOVER - Dark Cloud Cover
    # ------------------------------------------------------------------------------------------ #
    def DARKCLOUDCOVER(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Dark Cloud Cover (CDLDARKCLOUDCOVER).
        A bearish reversal pattern where a bearish candle opens above the previous 
        period's high but closes well into the body of the previous bullish candle.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'DARK_CLOUD_COVER' column (-1: bearish reversal, 0: no pattern).
        """
        data['DARK_CLOUD_COVER'] = np.where((data['close'].shift(1) > data['open'].shift(1)) &
                    (data['close'] < data['open']) &
                    (data['close'] > data['open'].shift(1)) &
                    (data['close'] - data['open'] > (data['open'].shift(1) - data['close'].shift(1)) * 0.5) &
                    (data['close'] < (data['open'].shift(1) + data['close'].shift(1)) * 0.5), -1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLDOJI - Doji
    # ------------------------------------------------------------------------------------------ #
    def DOJI(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Doji (CDLDOJI).
        A single candle pattern where the opening and closing prices are virtually equal, 
        signifying market indecision and a potential reversal point.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'DOJI' column (1: doji found, 0: no pattern).
        """
        data['DOJI'] = np.where((np.abs(data['open'] - data['close']) <= (data['high'] - data['low']) * 0.1) &
                    ((data['high'] - np.maximum(data['open'], data['close'])) > (data['high'] - data['low']) * 0.1) &
                    ((np.minimum(data['open'], data['close']) - data['low']) > (data['high'] - data['low']) * 0.1), 1, 0)
        return data


    # ------------------------------------------------------------------------------------------ #
    # CDLENGULFING - Engulfing Pattern
    # ------------------------------------------------------------------------------------------ #
    def ENGULFING(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Engulfing Pattern (CDLENGULFING).
        A two-candle reversal pattern. This implementation detects the Bullish Engulfing 
        variant where a large bullish candle completely overlaps the previous bearish candle's body.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'ENGULFING' column (1: bullish reversal, 0: no pattern).
        """
        data['ENGULFING'] = np.where((data['close'].shift(1) < data['open'].shift(1)) &
                    (data['close'] > data['open']) &
                    (data['close'] > data['open'].shift(1)) &
                    (data['close'].shift(1) < data['open']), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLEVENINGDOJISTAR - Evening Doji Star
    # ------------------------------------------------------------------------------------------ #
    def EVENINGDOJISTAR(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Evening Doji Star (CDLEVENINGDOJISTAR).
        A bearish reversal pattern consisting of a large bullish candle, a doji 
        that gaps up, and a large bearish candle.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'EVENING_DOJI_STAR' column (-1: bearish reversal, 0: no pattern).
        """
        data['EVENING_DOJI_STAR'] = np.where((data['close'].shift(2) > data['open'].shift(2)) &
                    (np.abs(data['open'].shift(1) - data['close'].shift(1)) <= (data['high'].shift(1) - data['low'].shift(1)) * 0.1) &
                    (data['close'] < data['open']) &
                    (data['close'] < data['open'].shift(2)) &
                    (data['close'].shift(1) > data['open'].shift(2)) &
                    (data['open'] < data['close'].shift(1)), -1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLEVENINGSTAR - Evening Star
    # ------------------------------------------------------------------------------------------ #
    def EVENINGSTAR(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Evening Star (CDLEVENINGSTAR).
        A three-candle bearish reversal pattern that forms at the peak of an uptrend, 
        consisting of a large bullish candle, a small-bodied candle, and a large bearish candle.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'EVENING_STAR' column (-1: bearish reversal, 0: no pattern).
        """
        data['EVENING_STAR'] = np.where((data['close'].shift(2) > data['open'].shift(2)) &
                    (data['close'].shift(1) > data['open'].shift(1)) &
                    (data['close'] < data['open']) &
                    (data['close'] < data['open'].shift(2)) &
                    (data['close'].shift(1) > data['open'].shift(2)) &
                    (data['open'] < data['close'].shift(1)), -1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLGAPSIDESIDEWHITE - Up/Down-gap side-by-side white lines
    # ------------------------------------------------------------------------------------------ #
    def GAPSIDESIDEWHITE(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Up/Down-gap side-by-side white lines (CDLGAPSIDESIDEWHITE).
        A continuation pattern where multiple candles gap in the direction of the trend. 
        This implementation seeks the bullish variant.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'GAP_SIDE_BY_SIDE_WHITE' column (1: bullish continuation, 0: no pattern).
        """
        data['GAP_SIDE_BY_SIDE_WHITE'] = np.where((data['close'].shift(1) > data['open'].shift(1)) &
                    (data['close'] < data['open']) &
                    (np.abs(data['close'] - data['open']) <= (data['high'] - data['low']) * 0.1) &
                    (np.abs(data['close'].shift(1) - data['open'].shift(1)) <= (data['high'].shift(1) - data['low'].shift(1)) * 0.1) &
                    (np.abs(data['close'] - data['close'].shift(1)) <= (data['high'].shift(1) - data['low'].shift(1)) * 0.1), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLGRAVESTONEDOJI - Gravestone Doji
    # ------------------------------------------------------------------------------------------ #
    def GRAVESTONEDOJI(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Gravestone Doji (CDLGRAVESTONEDOJI).
        A bearish reversal doji where the open, low, and close are at the same price, 
        located at the bottom of a long upper wick.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'GRAVESTONE_DOJI' column (-1: bearish reversal, 0: no pattern).
        """
        data['GRAVESTONE_DOJI'] = np.where((np.abs(data['open'] - data['close']) <= (data['high'] - data['low']) * 0.1) &
                    ((data['high'] - np.maximum(data['open'], data['close'])) > (data['high'] - data['low']) * 0.1) &
                    ((np.minimum(data['open'], data['close']) - data['low']) > (data['high'] - data['low']) * 0.1), -1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLHAMMER - Hammer
    # ------------------------------------------------------------------------------------------ #
    def HAMMER(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Hammer (CDLHAMMER).
        A bullish reversal pattern consisting of a single candle with a small body 
        at the top and a long lower shadow, appearing after a downtrend.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'HAMMER' column (1: bullish reversal, 0: no pattern).
        """
        data['HAMMER'] = np.where((data['open'] > data['close']) &
                    (data['open'] - data['close'] <= (data['high'] - data['low']) * 0.1) &
                    ((data['high'] - data['open']) > (data['high'] - data['low']) * 0.1) &
                    ((data['close'] - data['low']) > (data['high'] - data['low']) * 0.1), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLHANGINGMAN - Hanging Man
    # ------------------------------------------------------------------------------------------ #
    def HANGINGMAN(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Hanging Man (CDLHANGINGMAN).
        A bearish reversal pattern with the same shape as a hammer, but occurring 
        at the top of an uptrend.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'HANGING_MAN' column (-1: bearish reversal, 0: no pattern).
        """
        data['HANGING_MAN'] = np.where((data['open'] > data['close']) &
                    (data['open'] - data['close'] <= (data['high'] - data['low']) * 0.1) &
                    ((data['high'] - data['open']) > (data['high'] - data['low']) * 0.1) &
                    ((data['close'] - data['low']) > (data['high'] - data['low']) * 0.1), -1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLHARAMI - Harami Pattern
    # ------------------------------------------------------------------------------------------ #
    def HARAMI(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Harami Pattern (CDLHARAMI).
        A two-candle reversal/warning pattern where the second candle's body is 
        entirely contained within the first candle's body. This implementation detects the bullish variant.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'HARAMI' column (1: bullish reversal, 0: no pattern).
        """
        data['HARAMI'] = np.where((data['close'].shift(1) > data['open'].shift(1)) &
                    (data['close'] < data['open']) &
                    (data['close'] > data['open'].shift(1)) &
                    (data['close'].shift(1) < data['open']), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLHARAMICROSS - Harami Cross Pattern
    # ------------------------------------------------------------------------------------------ #
    def HARAMICROSS(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Harami Cross Pattern (CDLHARAMICROSS).
        A variant of the Harami where the second candle is a doji. This implementation 
        detects the bullish variant.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'HARAMI_CROSS' column (1: bullish reversal, 0: no pattern).
        """
        data['HARAMI_CROSS'] = np.where((data['close'].shift(1) > data['open'].shift(1)) &
                    (data['close'] < data['open']) &
                    (data['close'] > data['open'].shift(1)) &
                    (data['close'].shift(1) < data['open']) &
                    (np.abs(data['open'] - data['close']) <= (data['high'] - data['low']) * 0.1) &
                    ((data['high'] - np.maximum(data['open'], data['close'])) > (data['high'] - data['low']) * 0.1) &
                    ((np.minimum(data['open'], data['close']) - data['low']) > (data['high'] - data['low']) * 0.1), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLHIGHWAVE - High-Wave Candle
    # ------------------------------------------------------------------------------------------ #
    def HIGHWAVE(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        High-Wave Candle (CDLHIGHWAVE).
        A candle with a very long upper or lower shadow and a small body, showing extreme indecision.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'HIGH_WAVE' column (currently a placeholder).
        """
        data['HIGH_WAVE'] = np.where((data['high'] - np.maximum(data['open'], data['close'])) > (data['high'] - data['low']) * 0.6, 0, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLHIKKAKE - Hikkake Pattern
    # ------------------------------------------------------------------------------------------ #
    def HIKKAKE(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Hikkake Pattern (CDLHIKKAKE).
        A multi-candle signal used to identify a false breakout. This implementation 
        heads toward bullish detection.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'HIKKAKE' column (1: bullish signal, 0: no pattern).
        """
        data['HIKKAKE'] = np.where((data['close'].shift(3) > data['open'].shift(3)) &
                    (data['close'].shift(2) > data['open'].shift(2)) &
                    (data['close'].shift(1) > data['open'].shift(1)) &
                    (data['close'] < data['open'].shift(3)) &
                    (data['low'] > data['open'].shift(2)) &
                    (data['low'] < data['close'].shift(2)) &
                    (data['close'] < data['open'].shift(1)) &
                    (data['low'] > data['open']) &
                    (data['close'] > data['open']), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLHIKKAKEMOD - Modified Hikkake Pattern
    # ------------------------------------------------------------------------------------------ #
    def HIKKAKEMOD(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Modified Hikkake Pattern (CDLHIKKAKEMOD).
        An advanced variant of the Hikkake pattern used to identify false breakouts 
        with additional confirmation criteria.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'HIKKAKE_MOD' column (1: bullish signal, 0: no pattern).
        """
        data['HIKKAKE_MOD'] = np.where((data['close'].shift(3) > data['open'].shift(3)) &
                    (data['close'].shift(2) > data['open'].shift(2)) &
                    (data['close'].shift(1) > data['open'].shift(1)) &
                    (data['close'] < data['open'].shift(3)) &
                    (data['low'] > data['open'].shift(2)) &
                    (data['low'] < data['close'].shift(2)) &
                    (data['close'] < data['open'].shift(1)) &
                    (data['low'] > data['open']) &
                    (data['close'] > data['open']), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLHOMINGPIGEON - Homing Pigeon
    # ------------------------------------------------------------------------------------------ #
    def HOMINGPIGEON(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Homing Pigeon (CDLHOMINGPIGEON).
        A bullish reversal pattern where both candles are bearish, but the second 
        candle's body is entirely contained within the first.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'HOMING_PIGEON' column (1: bullish reversal, 0: no pattern).
        """
        data['HOMING_PIGEON'] = np.where((data['close'].shift(1) > data['open'].shift(1)) &
                    (data['close'] < data['open']) &
                    (data['close'] > data['close'].shift(1)) &
                    (data['close'].shift(1) < data['open']) &
                    (np.abs(data['open'] - data['close']) <= (data['high'] - data['low']) * 0.1) &
                    ((data['high'] - np.maximum(data['open'], data['close'])) > (data['high'] - data['low']) * 0.1) &
                    ((np.minimum(data['open'], data['close']) - data['low']) > (data['high'] - data['low']) * 0.1), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLIDENTICAL3CROWS - Identical Three Crows
    # ------------------------------------------------------------------------------------------ #
    def IDENTICALTHREECROWS(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Identical Three Crows (CDLIDENTICAL3CROWS).
        A bearish reversal pattern similar to Three Black Crows, but where each candle's 
        open is at or very near the previous candle's close.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'IDENTICAL_THREE_CROWS' column (-1: bearish reversal, 0: no pattern).
        """
        data['IDENTICAL_THREE_CROWS'] = np.where((data['close'].shift(2) < data['open'].shift(2)) &
                    (data['close'].shift(1) < data['open'].shift(1)) &
                    (data['close'] < data['open']) &
                    (data['close'] < data['close'].shift(2)) &
                    (data['close'].shift(1) < data['open'].shift(2)) &
                    (data['open'] > data['close'].shift(1)), -1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLINNECK - In-Neck Pattern
    # ------------------------------------------------------------------------------------------ #
    def INNECK(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        In-Neck Pattern (CDLINNECK).
        A bearish continuation pattern in a downtrend where a bullish candle closes 
        just inside the previous candle's body or at its close.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'IN_NECK' column (1: detected, 0: no pattern).
        """
        data['IN_NECK'] = np.where((data['close'].shift(1) < data['open'].shift(1)) &
                    (data['close'] > data['open']) &
                    (data['close'] > data['open'].shift(1)) &
                    (data['close'].shift(1) < data['open']) &
                    (data['close'] - data['open'] < (data['open'].shift(1) - data['close'].shift(1)) * 0.1) &
                    (data['close'] > (data['open'].shift(1) + data['close'].shift(1)) * 0.5), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLINVERTEDHAMMER - Inverted Hammer
    # ------------------------------------------------------------------------------------------ #
    def INVERTEDHAMMER(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Inverted Hammer (CDLINVERTEDHAMMER).
        A bullish reversal pattern consisting of a single candle with a small body 
        at the bottom and a long upper shadow, appearing after a downtrend.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'INVERTED_HAMMER' column (1: bullish reversal, 0: no pattern).
        """
        data['INVERTED_HAMMER'] = np.where((data['open'] < data['close']) &
                    (data['open'] - data['close'] <= (data['high'] - data['low']) * 0.1) &
                    ((data['high'] - data['close']) > (data['high'] - data['low']) * 0.1) &
                    ((data['open'] - data['low']) > (data['high'] - data['low']) * 0.1), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLKICKING - Kicking
    # ------------------------------------------------------------------------------------------ #
    def KICKING(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Kicking Pattern (CDLKICKING).
        A powerful two-candle reversal pattern consisting of two marubozu candles 
        with a gap between them. This implementation focuses on the bullish variant.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'KICKING' column (1: bullish reversal, 0: no pattern).
        """
        data['KICKING'] = np.where((data['close'].shift(1) > data['open'].shift(1)) &
                    (data['close'] > data['open']) &
                    (data['close'] > data['high'].shift(1)) &
                    (data['close'].shift(1) < data['low']) &
                    (data['close'].shift(1) > data['open']) &
                    (data['close'] < data['open'].shift(1)), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLKICKINGBYLENGTH - Kicking - bull/bear determined by the longer marubozu
    # ------------------------------------------------------------------------------------------ #
    def KICKINGBYLENGTH(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Kicking - bull/bear determined by the longer marubozu (CDLKICKINGBYLENGTH).
        A variant of the Kicking pattern where the strength is determined by the 
        relative lengths of the candles.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'KICKING_BY_LENGTH' column (1: bullish signal, 0: no pattern).
        """
        data['KICKING_BY_LENGTH'] = np.where((data['close'].shift(1) > data['open'].shift(1)) &
                    (data['close'] > data['open']) &
                    (data['close'] > data['high'].shift(1)) &
                    (data['close'].shift(1) < data['low']) &
                    (data['close'].shift(1) > data['open']) &
                    (data['close'] < data['open'].shift(1)), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLLADDERBOTTOM - Ladder Bottom
    # ------------------------------------------------------------------------------------------ #
    def LADDERBOTTOM(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Ladder Bottom (CDLLADDERBOTTOM).
        A rare five-candle bullish reversal pattern appearing during a downtrend, 
        indicating exhaustion of bearish momentum.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'LADDER_BOTTOM' column (1: bullish reversal, 0: no pattern).
        """
        data['LADDER_BOTTOM'] = np.where((data['close'].shift(4) > data['open'].shift(4)) &
                    (data['close'].shift(3) > data['open'].shift(3)) &
                    (data['close'].shift(2) > data['open'].shift(2)) &
                    (data['close'].shift(1) > data['open'].shift(1)) &
                    (data['close'] < data['open'].shift(4)) &
                    (data['low'] > data['open'].shift(3)) &
                    (data['low'] > data['open'].shift(2)) &
                    (data['low'] > data['open'].shift(1)) &
                    (data['close'] > data['open']), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLLONGLEGGEDDOJI - Long Legged Doji
    # ------------------------------------------------------------------------------------------ #
    def LONGLEGGEDDOJI(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Long Legged Doji (CDLLONGLEGGEDDOJI).
        A doji candle with long upper and lower shadows, indicating high indecision.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'LONG_LEGGED_DOJI' column (1: doji found, 0: no pattern).
        """
        data['LONG_LEGGED_DOJI'] = np.where((np.abs(data['open'] - data['close']) <= (data['high'] - data['low']) * 0.1) &
                    (np.abs(data['high'] - np.maximum(data['open'], data['close'])) > (data['high'] - data['low']) * 0.1) &
                    (np.abs(np.minimum(data['open'], data['close']) - data['low']) > (data['high'] - data['low']) * 0.1), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLLONGLINE - Long Line Candle
    # ------------------------------------------------------------------------------------------ #
    def LONGLINE(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Long Line Candle (CDLLONGLINE).
        A candle with a long real body compared to its shadows.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'LONG_LINE' column (1: pattern found, 0: no pattern).
        """
        data['LONG_LINE'] = np.where((np.abs(data['open'] - data['close']) > (data['high'] - data['low']) * 0.75), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLMARUBOZU - Marubozu
    # ------------------------------------------------------------------------------------------ #
    def MARUBOZU(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Marubozu (CDLMARUBOZU).
        A candle with no or very small shadows, indicating strong buying or selling pressure.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'MARUBOZU' column (1: pattern found, 0: no pattern).
        """
        data['MARUBOZU'] = np.where((np.abs(data['open'] - data['close']) > (data['high'] - data['low']) * 0.9) &
                    (np.abs(data['open'] - data['low']) <= (data['high'] - data['low']) * 0.1) &
                    (np.abs(data['close'] - data['high']) <= (data['high'] - data['low']) * 0.1), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLMATCHINGLOW - Matching Low
    # ------------------------------------------------------------------------------------------ #
    def MATCHINGLOW(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Matching Low (CDLMATCHINGLOW).
        A bullish reversal pattern where two candles have the same closing price at a low.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'MATCHING_LOW' column (1: bullish reversal, 0: no pattern).
        """
        data['MATCHING_LOW'] = np.where((data['close'].shift(1) > data['open'].shift(1)) &
                    (data['close'] < data['open']) &
                    (data['close'] < data['close'].shift(1)) &
                    (data['close'].shift(1) < data['open']) &
                    (data['low'] < data['low'].shift(1)) &
                    (data['low'] == data['low'].shift(1)), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLMATHOLD - Mat Hold
    # ------------------------------------------------------------------------------------------ #
    def MATHOLD(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Mat Hold (CDLMATHOLD).
        A bullish continuation pattern.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'MATH_HOLD' column (1: bullish continuation, 0: no pattern).
        """
        data['MATH_HOLD'] = np.where((data['close'].shift(4) > data['open'].shift(4)) &
                    (data['close'].shift(3) > data['open'].shift(3)) &
                    (data['close'].shift(2) > data['open'].shift(2)) &
                    (data['close'].shift(1) > data['open'].shift(1)) &
                    (data['close'] > data['open']) &
                    (data['close'] > data['close'].shift(4)) &
                    (data['close'] < data['open'].shift(1)) &
                    ((data['close'] - data['open']) / (data['high'] - data['low']) > 0.6) &
                    ((data['close'] - data['open']) / (data['high'] - data['low']) < 0.9), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLMORNINGDOJISTAR - Morning Doji Star
    # ------------------------------------------------------------------------------------------ #
    def MORNINGDOJISTAR(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Morning Doji Star (CDLMORNINGDOJISTAR).
        A bullish reversal pattern consisting of a large bearish candle, a doji that gaps down, and a large bullish candle.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'MORNING_DOJI_STAR' column (1: bullish reversal, 0: no pattern).
        """
        data['MORNING_DOJI_STAR'] = np.where((data['close'].shift(2) < data['open'].shift(2)) &
                    (data['close'].shift(2) < data['close'].shift(1)) &
                    (data['close'].shift(1) > data['open'].shift(1)) &
                    (data['close'] > data['open']) &
                    (np.abs(data['open'] - data['close']) <= (data['high'] - data['low']) * 0.1) &
                    (np.abs(data['open'] - data['low']) > (data['high'] - data['low']) * 0.1) &
                    (np.abs(data['close'] - data['high']) > (data['high'] - data['low']) * 0.1), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLMORNINGSTAR - Morning Star
    # ------------------------------------------------------------------------------------------ #
    def MORNINGSTAR(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Morning Star (CDLMORNINGSTAR).
        A three-candle bullish reversal pattern consisting of a large bearish candle, a small-bodied candle, and a large bullish candle.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'MORNING_STAR' column (1: bullish reversal, 0: no pattern).
        """
        data['MORNING_STAR'] = np.where((data['close'].shift(2) < data['open'].shift(2)) &
                    (data['close'].shift(2) < data['close'].shift(1)) &
                    (data['close'].shift(1) > data['open'].shift(1)) &
                    (data['close'] > data['open']) &
                    (np.abs(data['open'] - data['close']) <= (data['high'] - data['low']) * 0.1) &
                    (np.abs(data['open'] - data['low']) > (data['high'] - data['low']) * 0.1) &
                    (np.abs(data['close'] - data['high']) > (data['high'] - data['low']) * 0.1), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLONNECK - On-Neck Pattern
    # ------------------------------------------------------------------------------------------ #
    def ONNECK(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        On-Neck Pattern (CDLONNECK).
        A bearish continuation pattern where a bullish candle closes at the same price as the previous bearish candle's low.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'ON_NECK' column (-1: bearish continuation, 0: no pattern).
        """
        data['ON_NECK'] = np.where((data['close'].shift(1) < data['open'].shift(1)) &
                    (data['close'] > data['open']) &
                    (data['close'] > data['open'].shift(1)) &
                    (data['close'].shift(1) < data['open']) &
                    (data['close'] - data['open'] < (data['close'].shift(1) - data['open'].shift(1)) * 0.1) &
                    (data['close'] < (data['open'].shift(1) + data['close'].shift(1)) * 0.5), -1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLPIERCING - Piercing Pattern
    # ------------------------------------------------------------------------------------------ #
    def PIERCING(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Piercing Pattern (CDLPIERCING).
        A bullish reversal pattern where a bullish candle opens below the previous candle's low and closes above the midpoint of its body.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'PIERCING' column (1: bullish reversal, 0: no pattern).
        """
        data['PIERCING'] = np.where((data['close'].shift(1) < data['open'].shift(1)) &
                    (data['close'] > data['open']) &
                    (data['close'] < data['open'].shift(1)) &
                    (data['close'] + (data['open'] - data['close']) * 0.5 > data['close'].shift(1)) &
                    (data['close'] + (data['open'] - data['close']) * 0.5 < data['open'].shift(1)), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLRICKSHAWMAN - Rickshaw Man
    # ------------------------------------------------------------------------------------------ #
    def RICKSHAWMAN(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Rickshaw Man (CDLRICKSHAWMAN).
        A long-legged doji where the open and close are at or near the middle of the candle's range.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'RICKSHAW_MAN' column (1: pattern found, 0: no pattern).
        """
        data['RICKSHAW_MAN'] = np.where((np.abs(data['open'] - data['close']) <= (data['high'] - data['low']) * 0.1) &
                    (np.abs(data['high'] - np.maximum(data['open'], data['close'])) > (data['high'] - data['low']) * 0.1) &
                    (np.abs(np.minimum(data['open'], data['close']) - data['low']) > (data['high'] - data['low']) * 0.1), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLRISEFALL3METHODS - Rising/Falling Three Methods
    # ------------------------------------------------------------------------------------------ #
    def RISEFALL3METHODS(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Rising/Falling Three Methods (CDLRISEFALL3METHODS).
        A five-candle continuation pattern.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'RISE_FALL_THREE_METHODS' column (1: continuation signal, 0: no pattern).
        """
        data['RISE_FALL_THREE_METHODS'] = np.where((data['close'].shift(4) > data['open'].shift(4)) &
                    (data['close'].shift(3) > data['open'].shift(3)) &
                    (data['close'].shift(2) > data['open'].shift(2)) &
                    (data['close'].shift(1) > data['open'].shift(1)) &
                    (data['close'] > data['open']) &
                    (data['close'] < data['close'].shift(4)) &
                    (data['close'] > data['open'].shift(1)) &
                    ((data['close'] - data['open']) / (data['high'] - data['low']) > 0.6) &
                    ((data['close'] - data['open']) / (data['high'] - data['low']) < 0.9), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLSEPARATINGLINES - Separating Lines
    # ------------------------------------------------------------------------------------------ #
    def SEPARATINGLINES(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Separating Lines (CDLSEPARATINGLINES).
        A continuation pattern where two candles of opposite color have the same opening price.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'SEPARATING_LINES' column (1: pattern found, 0: no pattern).
        """
        data['SEPARATING_LINES'] = np.where((data['close'].shift(1) < data['open'].shift(1)) &
                    (data['close'] > data['open']) &
                    (data['close'].shift(1) == data['open'].shift(1)) &
                    (data['close'] == data['open']), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLSHOOTINGSTAR - Shooting Star
    # ------------------------------------------------------------------------------------------ #
    def SHOOTINGSTAR(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Shooting Star (CDLSHOOTINGSTAR).
        A bearish reversal pattern consisting of a single candle with a small body at the bottom and a long upper shadow, appearing after an uptrend.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'SHOOTING_STAR' column (1: bearish reversal, 0: no pattern).
        """
        data['SHOOTING_STAR'] = np.where((data['open'] > data['close']) &
                    (data['open'] - data['close'] > (data['high'] - data['low']) * 0.75) &
                    (data['close'] - data['low'] <= (data['high'] - data['low']) * 0.1) &
                    (data['open'] - data['low'] <= (data['high'] - data['low']) * 0.1), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLSHORTLINE - Short Line Candle
    # ------------------------------------------------------------------------------------------ #
    def SHORTLINE(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Short Line Candle (CDLSHORTLINE).
        A candle with a small real body compared to its shadows.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'SHORT_LINE' column (1: pattern found, 0: no pattern).
        """
        data['SHORT_LINE'] = np.where((np.abs(data['open'] - data['close']) <= (data['high'] - data['low']) * 0.1) &
                    (np.abs(data['high'] - np.maximum(data['open'], data['close'])) > (data['high'] - data['low']) * 0.1) &
                    (np.abs(np.minimum(data['open'], data['close']) - data['low']) > (data['high'] - data['low']) * 0.1), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLSPINNINGTOP - Spinning Top
    # ------------------------------------------------------------------------------------------ #
    def SPINNINGTOP(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Spinning Top (CDLSPINNINGTOP).
        A single candle pattern with a small real body and long upper and lower shadows, indicating market indecision.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'SPINNING_TOP' column (1: pattern found, 0: no pattern).
        """
        data['SPINNING_TOP'] = np.where((np.abs(data['open'] - data['close']) <= (data['high'] - data['low']) * 0.1) &
                    (np.abs(data['high'] - np.maximum(data['open'], data['close'])) > (data['high'] - data['low']) * 0.1) &
                    (np.abs(np.minimum(data['open'], data['close']) - data['low']) > (data['high'] - data['low']) * 0.1), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLSTALLEDPATTERN - Stalled Pattern
    # ------------------------------------------------------------------------------------------ #
    def STALLEDPATTERN(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Stalled Pattern (CDLSTALLEDPATTERN).
        A bearish reversal pattern in an uptrend, showing weakening bullish momentum.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'STALLED_PATTERN' column (1: pattern found, 0: no pattern).
        """
        data['STALLED_PATTERN'] = np.where((data['close'].shift(1) > data['open'].shift(1)) &
                    (data['close'] < data['open']) &
                    (data['close'] < data['close'].shift(1)) &
                    (data['close'].shift(1) < data['open']) &
                    (data['high'].shift(1) > data['high'].shift(2)) &
                    (data['high'].shift(1) > data['high']) &
                    (data['low'] < data['low'].shift(1)) &
                    (data['low'] < data['low'].shift(2)), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLSTICKSANDWICH - Stick Sandwich
    # ------------------------------------------------------------------------------------------ #
    def STICKSANDWICH(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Stick Sandwich (CDLSTICKSANDWICH).
        A reversal pattern where two candles with the same close "sandwich" a candle of the opposite color.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'STICK_SANDWICH' column (1: reversal signal, 0: no pattern).
        """
        data['STICK_SANDWICH'] = np.where((data['close'].shift(2) > data['open'].shift(2)) &
                    (data['close'].shift(2) > data['close'].shift(1)) &
                    (data['close'].shift(1) < data['open'].shift(1)) &
                    (data['close'] < data['open']) &
                    (data['close'].shift(1) > data['close'].shift(2)) &
                    (data['close'] < data['open'].shift(1)) &
                    (data['open'] < data['close']) &
                    (data['open'] == data['open'].shift(2)) &
                    (data['close'] == data['close'].shift(2)), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLTAKURI - Takuri (Dragonfly Doji with very long lower shadow)
    # ------------------------------------------------------------------------------------------ #
    def TAKURI(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Takuri (CDLTAKURI).
        A Dragonfly Doji with a very long lower shadow, indicating strong rejection of lower prices.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'TAKURI' column (1: pattern found, 0: no pattern).
        """
        data['TAKURI'] = np.where((np.abs(data['open'] - data['close']) <= (data['high'] - data['low']) * 0.1) &
                    (np.abs(data['high'] - np.maximum(data['open'], data['close'])) > (data['high'] - data['low']) * 0.1) &
                    (np.abs(np.minimum(data['open'], data['close']) - data['low']) > (data['high'] - data['low']) * 0.1), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLTASUKIGAP - Tasuki Gap
    # ------------------------------------------------------------------------------------------ #
    def TASUKIGAP(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Tasuki Gap (CDLTASUKIGAP).
        A continuation pattern where a candle gaps in the trend direction followed by a candle that partially fills the gap.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'TASUKI_GAP' column (1: continuation signal, 0: no pattern).
        """
        data['TASUKI_GAP'] = np.where((data['close'].shift(1) > data['open'].shift(1)) &
                    (data['close'] < data['open']) &
                    (data['close'] > data['close'].shift(1)) &
                    (data['close'].shift(1) < data['open']) &
                    (data['high'].shift(1) < data['low']) &
                    (data['low'] > data['high'].shift(1)) &
                    (data['low'] < data['open'].shift(1)) &
                    (data['close'] > data['open'].shift(1)), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLTHRUSTING - Thrusting Pattern
    # ------------------------------------------------------------------------------------------ #
    def THRUSTING(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Thrusting Pattern (CDLTHRUSTING).
        A bearish continuation pattern where a bullish candle closes within the body of the previous bearish candle but below its midpoint.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'THRUSTING' column (1: pattern found, 0: no pattern).
        """
        data['THRUSTING'] = np.where((data['close'].shift(1) < data['open'].shift(1)) &
                    (data['close'] < data['open']) &
                    (data['close'] + (data['open'] - data['close']) * 0.5 > data['close'].shift(1)) &
                    (data['close'] + (data['open'] - data['close']) * 0.5 < data['open'].shift(1)) &
                    (data['close'] > data['open'].shift(1)) &
                    (np.abs(data['close'] - data['open']) <= (data['high'] - data['low']) * 0.1) &
                    (np.abs(data['open'] - data['close']) > (data['high'] - data['low']) * 0.1), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLTRISTAR - Tristar Pattern
    # ------------------------------------------------------------------------------------------ #
    def TRISTAR(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Tristar Pattern (CDLTRISTAR).
        A reversal pattern consisting of three dojis.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'TRISTAR' column (1: reversal signal, 0: no pattern).
        """
        data['TRISTAR'] = np.where((data['close'].shift(2) > data['open'].shift(2)) &
                    (data['close'].shift(2) > data['close'].shift(1)) &
                    (data['close'].shift(1) < data['open'].shift(1)) &
                    (data['close'] < data['open']) &
                    (data['close'].shift(1) > data['close'].shift(2)) &
                    (data['close'] > data['open'].shift(1)) &
                    (data['close'] == data['open']), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLUNIQUE3RIVER - Unique 3 River
    # ------------------------------------------------------------------------------------------ #
    def UNIQUETHREERIVER(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Unique 3 River (CDLUNIQUE3RIVER).
        A bullish reversal pattern consisting of three candles with specific body and shadow characteristics.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'UNIQUE_3_RIVER' column (1: bullish reversal, 0: no pattern).
        """
        data['UNIQUE_3_RIVER'] = np.where((data['close'].shift(2) > data['open'].shift(2)) &
                    (data['close'].shift(2) > data['close'].shift(1)) &
                    (data['close'].shift(1) > data['open'].shift(1)) &
                    (data['close'] < data['open']) &
                    (data['close'].shift(1) < data['close'].shift(2)) &
                    (data['close'] > data['open'].shift(1)) &
                    (data['open'] == data['close']), 1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLUPSIDEGAP2CROWS - Upside Gap Two Crows
    # ------------------------------------------------------------------------------------------ #
    def UPSIDEGAPTWOCROWS(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Upside Gap Two Crows (CDLUPSIDEGAP2CROWS).
        A bearish reversal pattern that forms after a gap up in an uptrend.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'UPSIDE_GAP_2_CROWS' column (-1: bearish reversal, 0: no pattern).
        """
        data['UPSIDE_GAP_2_CROWS'] = np.where((data['close'].shift(2) > data['open'].shift(2)) &
                    (data['close'].shift(2) > data['close'].shift(1)) &
                    (data['close'].shift(1) < data['open'].shift(1)) &
                    (data['close'] < data['open']) &
                    (data['close'] > data['open'].shift(1)) &
                    (data['open'] > data['close'].shift(1)) &
                    (data['close'] > data['open'].shift(2)), -1, 0)
        return data

    # ------------------------------------------------------------------------------------------ #
    # CDLXSIDEGAP3METHODS - Upside/Downside Gap Three Methods
    # ------------------------------------------------------------------------------------------ #
    def UPSIDEDOWNSIDEGAPTHREEMETHODS(self,data: pd.DataFrame) -> pd.DataFrame:
        """
        Upside/Downside Gap Three Methods (CDLXSIDEGAP3METHODS).
        A continuation pattern consisting of a gap followed by a candle that fills the gap.

        Args:
            data (pd.DataFrame): DataFrame with 'open', 'high', 'low', 'close' columns.

        Returns:
            pd.DataFrame: DataFrame with 'UPSIDE_DOWNSIDE_GAP_3_METHODS' column (-1: pattern found, 0: no pattern).
        """
        data['UPSIDE_DOWNSIDE_GAP_3_METHODS'] = np.where((data['close'].shift(3) > data['open'].shift(3)) &
                    (data['close'].shift(2) > data['open'].shift(2)) &
                    (data['close'].shift(1) > data['open'].shift(1)) &
                    (data['close'] < data['open']) &
                    (data['close'] > data['close'].shift(3)) &
                    (data['close'] > data['open'].shift(2)) &
                    (data['close'] > data['open'].shift(1)) &
                    (data['open'] < data['close'].shift(3)) &
                    (data['open'] < data['close'].shift(2)) &
                    (data['open'] < data['close'].shift(1)), -1, 0)
        return data


class PriceAction():
    def __init__(self, data: pd.DataFrame):
        self.candle_patterns = CandlePatterns(data)
        self.dataframe = data

    def resistance(self, window: int = 30, n: int = 3) -> pd.DataFrame:
        self.dataframe['resistance'] = self.dataframe['high'].rolling(window=window, center=True,).apply(lambda x: x.nlargest(n).iloc[0])
        self.dataframe['resistance'] = self.dataframe['resistance'].ffill()
        return self.dataframe

    def support(self, window: int = 30, n: int = 3) -> pd.DataFrame:
        self.dataframe['support'] = self.dataframe['low'].rolling(window=window, center=True).apply(lambda x: x.nsmallest(n).iloc[0])
        self.dataframe['support'] = self.dataframe['support'].ffill()
        return self.dataframe

    