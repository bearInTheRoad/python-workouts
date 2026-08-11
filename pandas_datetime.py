import pandas as pd
import datetime
# 1. 生成交易时间序列
# 场景： 生成 2026 年 8 月 1 日到 8 月 7 日（含）的 1 分钟时间索引，频率为 1min。
# 要求： 使用 pd.date_range，输出索引长度应为 10080。

idx = pd.date_range(start = datetime.datetime(2026, 8, 1), end = datetime.datetime(2026, 8, 7, 23, 59, 59), freq = datetime.timedelta(minutes = 1))
print(len(idx))

# 2. 批量解析时间字符串
# 场景： 从交易所 API 拿到一列时间字符串 ['2026-08-09 14:30:00', '2026-08-09 14:31:00', ...]，共 100 万行。
# 要求： 用最快的方式转成 datetime64[ns]。提示：指定 format 参数。
dates = ['2026-08-09 14:30:00'] * 1_000_000
dates = pd.to_datetime(dates, format = '%Y-%m-%d %H:%M:%S')
print(type(dates[0]))

#
# 3. 提取时间组件
# 场景： 给定 DataFrame 有一列 timestamp，需要新增列：hour（0-23）、day_of_week（0=周一）、is_weekend（布尔值）、week_of_year（ISO 周数）。

df = pd.DataFrame({'timestamp': pd.date_range('2026-08-01', periods=1000, freq='H')})
df['hour'] = df['timestamp'].dt.hour
df['day_of_week'] = df['timestamp'].dt.weekday
df['is_weekend'] = df['timestamp'].dt.dayofweek >= 5
df['week_of_year'] = df['timestamp'].dt.isocalendar().week
print(df.head)

# 4. 时区转换
# 场景： 交易所返回的 timestamp 是 naive UTC（无时区信息）。你需要：
# 先标记为 UTC
# 转成香港时间（Asia/Hong_Kong）
# 要求： 分别用 tz_localize 和 tz_convert。
# Python
print("---------------------")
print('Exercise 4')
df = pd.DataFrame({'ts': pd.date_range('2026-08-09', periods=5, freq='H')})
df['ts_utc'] = df['ts'].dt.tz_localize('UTC')
df['ts_hk'] = df['ts_utc'].dt.tz_convert('Asia/Hong_Kong')
print(df.head)


# 5. 缺失时间戳填充（前向填充）
# 场景： 某分钟没有成交，数据缺失。给定一个只有部分时间点的 DataFrame，填充为完整的 1 分钟序列，price 用前值填充，volume 填 0。
# Python
print("---------------------")
print('Exercise 5')
rng = pd.date_range('2026-08-09 09:00', '2026-08-09 09:10', freq='1min')
df = pd.DataFrame({
    'timestamp': rng[[0, 2, 3, 5, 7, 10]],
    'price': [100, 101, 102, 103, 104, 105],
    'volume': [10, 20, 15, 30, 25, 40]
})
full_time = pd.DataFrame({'timestamp': rng})
df = df.merge(full_time, on='timestamp', how  = 'right')
df['price'] = df['price'].ffill()
df['volume'] = df['volume'].fillna(0)
print(df)


rng = pd.date_range('2026-08-09 09:00', '2026-08-09 09:10', freq='1min')
df = pd.DataFrame({
    'timestamp': rng[[0, 2, 3, 5, 7, 10]],
    'price': [100, 101, 102, 103, 104, 105],
    'volume': [10, 20, 15, 30, 25, 40]
})
df = df.set_index('timestamp').reindex(rng)
df['price'] = df['price'].ffill()
df['volume'] = df['volume'].fillna(0)
print(df)

# 6. 5 分钟 K 线聚合（OHLCV）
# 场景： 将 1 分钟数据聚合成 5 分钟 OHLCV。
# Python
print('-------------------------------')
print('Exercise 6')
import numpy as np

rng = pd.date_range('2026-08-09 09:00', periods=20, freq='1min')
df = pd.DataFrame({
    'timestamp': rng,
    'price': [100, 101, 102, 101, 103, 104, 103, 105, 106, 107,
              108, 107, 109, 110, 111, 110, 112, 113, 114, 115],
    'volume': np.random.randint(1, 100, 20)
}).set_index('timestamp')

ohlc = df.resample('5min').agg({'price': ['first', 'last', 'max', 'min']})
ohlc.columns = ['open', 'close', 'high', 'low']
ohlc['volume'] = df['volume'].resample('5min').sum()
print(ohlc)


# 7. 计算 1 分钟收益率
# 场景： 用 pct_change 计算价格收益率。
# Python
# # 接上一题 df

ohlc['pct_change'] = (ohlc['close'] - ohlc['open']) / ohlc['open']
print(ohlc)

df['returns'] = df['price'].pct_change()
print(df)


# 8. 1 小时滚动平均价
# 场景： 计算 60 分钟滚动平均价格，要求前 59 分钟也有值（用已有数据计算）

df['avg_60_min'] = df['price'].rolling(60, min_periods=1).agg('mean')
print(df)

# 9. 月初/月末日期
# 场景： 给定一列 timestamp，生成对应的月初和月末日期（如 2026-08-01 和 2026-08-31）。
# Python
df = pd.DataFrame({'ts': pd.date_range('2026-08-09', periods=10, freq='D')})
df['month_start'] = df['ts'].dt.to_period('M').dt.start_time
df['month_end'] = df['ts'].dt.to_period('M').dt.end_time
print(df)


# 10. 月份加减（不能用 timedelta）
# 场景： 给每个日期加 3 个月，自动处理月末（如 1月31日 → 4月30日）。

df['ts_plus_3m'] = df['ts'] + pd.DateOffset(months = 3)
print(df)

# 11. 只保留工作日
# 场景： 从时间序列中过滤掉周末。
# Python
df = pd.DataFrame({'ts': pd.date_range('2026-08-01', periods=14, freq='D')})
print(df[df['ts'].dt.weekday < 5])


# 12. 日内 VWAP（成交量加权平均价）
# 场景： 按天分组，计算每天的 VWAP = Σ(price × volume) / Σ(volume)。
# Python
rng = pd.date_range('2026-08-09', periods=48, freq='30min')
df = pd.DataFrame({
    'timestamp': rng,
    'price': np.random.randint(100, 110, 48),
    'volume': np.random.randint(100, 1000, 48)
})

df['day'] = df['timestamp'].dt.date
df['volume_usd'] = df['price'] * df['volume']
daily_df = df.groupby('day').agg({'volume_usd': sum, 'volume': sum})
daily_df['vwap'] = daily_df['volume_usd'] / daily_df['volume']
print(daily_df)


# 13. 检测连续 N 分钟价格冻结
# 场景： 找出价格连续 5 分钟没有变化的时段（流动性枯竭检测）。
# Python
print('----------------------')
print('Exercise 13')
rng = pd.date_range('2026-08-09 09:00', periods=20, freq='1min')
df = pd.DataFrame({
    'timestamp': rng,
    'price': [100, 100, 100, 101, 101, 101, 101, 101, 102, 103,
              103, 103, 103, 103, 103, 104, 105, 105, 105, 106]
}).set_index('timestamp')

price_change = df['price'] != df['price'].shift()
groups = price_change.cumsum()

out = (
    df.assign(run=groups)
        .reset_index()
        .groupby('run', as_index=False)
        .agg(
            start=('timestamp', 'first'),
            end=('timestamp', 'last'),
            price=('price', 'first'),
            minutes=('price', 'size'),
        )
        .query('minutes >= 5')
)
print(out)

df = df.reset_index()
df['run_id'] = (df['price'] != df['price'].shift()).cumsum()
size_df = df.groupby('run_id').size().reset_index()
size_df.columns = ['run_id', 'run_count']
final_df = df.merge(size_df, on = 'run_id', how = 'left')
print(final_df[final_df['run_count'] >= 5])


print(df.groupby('run_id')['price'].transform('size'))

# 14. 24 小时前同时间价格对比
# 场景： 计算每个时间戳 24 小时前的价格（严格时间对齐，1440 分钟 shift）。
# Python
rng = pd.date_range('2026-08-01', periods=2880, freq='1min')  # 2天
df = pd.DataFrame({'timestamp': rng, 'price': np.random.randn(2880).cumsum() + 100})
df.set_index('timestamp', inplace=True)

df['prev_day_price'] = df['price'].shift(1440)
print(df)


# 15. 90 分钟非标准频率聚合
# 场景： 交易所需要 90 分钟 K 线，不是标准 1H 或 2H。

print(df.resample('90min').agg('ohlc'))


# 16. 处理夏令时歧义时间
# 场景： 2026 年 3 月 8 日美国进入夏令时，2:00 AM 直接跳到 3:00 AM。生成纽约时间序列时，如何处理这个"丢失"的小时？
rng = pd.date_range(start='2026-03-08 01:00', periods=5, freq='1H', tz='America/New_York')
print(rng)

# 17. 日内波动率（滚动标准差）
# 场景： 计算每 30 分钟窗口的收益率标准差，作为实时波动率指标。
# Python
rng = pd.date_range('2026-08-09', periods=1000, freq='1min')
df = pd.DataFrame({'timestamp': rng, 'price': np.random.randn(1000).cumsum() + 100})
df.set_index('timestamp', inplace=True)

print(df.resample('30min').agg({'price': 'std'}))
print(df.rolling(30, min_periods = 1).agg({'price': 'std'}).rename({'price': 'std_price'}))

# 18. 交易时段筛选
# 场景： 只保留 UTC 时间 00:00-08:00 的数据（亚洲交易时段），且必须是工作日。



# 19. 多表时间对齐（merge_asof）
# 场景： 有两张表：trades（精确到微秒）和 quotes（精确到秒）。用 merge_asof 把每个 trade 对齐到它之前最近的一条 quote。
# Python
trades = pd.DataFrame({
    'timestamp': pd.to_datetime(['2026-08-09 09:00:00.123', '2026-08-09 09:00:00.456', '2026-08-09 09:00:01.789']),
    'trade_price': [100.1, 100.2, 100.3]
})

quotes = pd.DataFrame({
    'timestamp': pd.to_datetime(['2026-08-09 09:00:00.000', '2026-08-09 09:00:01.000']),
    'bid': [100.0, 100.15],
    'ask': [100.2, 100.25]
})

print(pd.merge_asof(right = quotes,left = trades, on='timestamp', direction = 'nearest'))

result = pd.merge_asof(
    trades.sort_values('timestamp'),
    quotes.sort_values('timestamp'),
    on='timestamp',
    direction='backward'
)
print(result)

# 20. 综合：从 Raw Trades 到完整 OHLCV
# 场景： 给定不规则的 trade 数据（时间戳不连续），生成完整的 1 分钟 OHLCV
# 缺失分钟用前收盘价填充 close、volume 填 0，并添加一列 trade_count（该分钟内有几条原始 trade）。
# Python
np.random.seed(42)
n = 300
rng = pd.date_range('2026-08-09 09:00', '2026-08-09 17:00', freq='1min')
timestamps = np.sort(np.random.choice(rng, size=n, replace=False))
df = pd.DataFrame({
    'timestamp': timestamps,
    'price': np.random.randn(n).cumsum() + 50000,
    'volume': np.random.randint(1, 100, n)
})

df = df.set_index('timestamp').reindex(rng)
df['price'] = df['price'].ffill()
df['volume'] = df['volume'].fillna(0)
print(df)




import pandas as pd
import numpy as np

# 模拟交易所原始成交数据（时间不规则，有缺失分钟）
timestamps = pd.to_datetime([
    '2026-08-09 09:00:00', '2026-08-09 09:00:15', '2026-08-09 09:00:45',
    '2026-08-09 09:01:10', '2026-08-09 09:02:05', '2026-08-09 09:04:30',
    '2026-08-09 09:05:00', '2026-08-09 09:05:20', '2026-08-09 09:07:00'
])
df = pd.DataFrame({
    'trade_time': timestamps,
    'price': [100.0, 100.1, 100.2, 100.15, 100.3, 100.25, 100.4, 100.35, 100.5],
    'volume': [10, 5, 8, 12, 20, 15, 10, 8, 25]
})

# 要求（按顺序）：
# 1. trade_time 设为 datetime 索引
# 2. 重采样为 1 分钟 OHLCV（Open=first, High=max, Low=min, Close=last, Volume=sum）
# 3. 补齐缺失的分钟（如 09:03, 09:06），Close 前向填充，Volume 填 0
# 4. 计算对数收益率：log(close / close_prev)
# 5. 计算 3 分钟滚动波动率（对数收益率的 3 分钟标准差）
# 6. 将索引从 UTC naive 转为 Asia/Hong_Kong 时区
print('-----------------------')
print('last Exercise')
df = df.set_index('trade_time').resample('1min').agg({'price': 'ohlc', 'volume': 'sum'})
df.columns = df.columns.droplevel(0)
df['close'] = df['close'].ffill()
df['volume'] = df['volume'].fillna(0)
df['prev_close'] = df['close'].shift(1)
df['return'] = np.log(df['close'] / df['prev_close'])
df['rolling_return'] = df['return'].rolling(3, min_periods = 1).std()
df = df.tz_localize('UTC').tz_convert('Asia/Hong_Kong')
print(df)
