# import pandas as pd
# import matplotlib.pyplot as plt
# from statsmodels.tsa.arima.model import ARIMA
# import warnings

# # 경고 메시지 무시
# warnings.filterwarnings("ignore")

# # CSV 파일 경로 설정
# file_path = 'C:\\Users\\SSAFY\\Desktop\\0726\\pjt\\pjt02\\버전1_금융\\archive\\NFLX.csv'

# # CSV 파일 읽어오기 (잘못된 줄 무시)
# df = pd.read_csv(file_path, on_bad_lines='skip')

# # 'Date' 열을 datetime 형식으로 변환
# df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# # 'Date' 열을 인덱스로 설정
# df.set_index('Date', inplace=True)

# # 2022년 1월 이후의 종가 데이터만 사용
# df_2022_onwards = df[df.index >= '2022-01-01']['Close']

# # ARIMA 모델 학습
# model = ARIMA(df_2022_onwards, order=(5, 1, 0))  # order 파라미터는 (p, d, q)를 의미
# model_fit = model.fit()

# # 미래 30일 예측
# forecast = model_fit.forecast(steps=30)

# # 예측 결과 시각화
# plt.figure(figsize=(14, 8))
# plt.plot(df_2022_onwards, label='실제 종가')
# plt.plot(forecast, label='예측 종가', color='red')
# plt.title('넷플릭스 주가 예측')
# plt.xlabel('날짜')
# plt.ylabel('종가')
# plt.legend()
# plt.grid(True)
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

# import pandas as pd

# # CSV 파일 경로 설정
# file_path = 'C:\\Users\\SSAFY\\Desktop\\0726\\pjt\\pjt02\\버전1_금융\\archive\\NFLX.csv'

# # CSV 파일 읽어오기
# df = pd.read_csv(file_path)

# # DataFrame 출력
# print(df.head())

# import pandas as pd
# import matplotlib.pyplot as plt
# from statsmodels.tsa.arima.model import ARIMA
# import warnings

# # 경고 메시지 무시
# warnings.filterwarnings("ignore")

# # CSV 파일 경로 설정
# file_path = 'C:\\Users\\SSAFY\\Desktop\\0726\\pjt\\pjt02\\버전1_금융\\archive\\NFLX.csv'

# # CSV 파일 읽어오기 (특정 열만)
# df = pd.read_csv(file_path, usecols=['Date', 'Open', 'High', 'Low', 'Close'], on_bad_lines='skip')

# # 'Date' 열을 datetime 형식으로 변환
# df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# # 2022년 1월 이후의 데이터 필터링
# df_2022_onwards = df[df['Date'] >= '2022-01-01']

# # 'Date' 열을 월별로 그룹화
# monthly_data = df_2022_onwards.resample('M', on='Date').agg({
#     'High': 'max',
#     'Low': 'min',
#     'Close': 'last'
# })

# # 시각화
# plt.figure(figsize=(14, 8))

# plt.plot(monthly_data.index, monthly_data['High'], label='월별 최고가', marker='o')
# plt.plot(monthly_data.index, monthly_data['Low'], label='월별 최저가', marker='o')
# plt.plot(monthly_data.index, monthly_data['Close'], label='월별 종가', marker='o')

# plt.title('2022년 1월 이후 월별 넷플릭스 주식 가격')
# plt.xlabel('날짜')
# plt.ylabel('가격')
# plt.legend()
# plt.grid(True)
# plt.xticks(rotation=45)
# plt.tight_layout()

# # 그래프 출력
# plt.show()

# import pandas as pd

# # CSV 파일 경로 설정
# file_path = 'C:\\Users\\SSAFY\\Desktop\\0726\\pjt\\pjt02\\버전1_금융\\archive\\NFLX.csv'

# # CSV 파일 읽어오기 (특정 열만)
# df = pd.read_csv(file_path, usecols=['Date', 'Open', 'High', 'Low', 'Close'], on_bad_lines='skip')

# # 'Date' 열을 datetime 형식으로 변환
# df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# # 2021년 이후의 데이터 필터링
# df_2021_onwards = df[df['Date'] >= '2021-01-01']

# # 필터링된 데이터 출력
# print(df_2021_onwards.head())

# import pandas as pd
# import matplotlib.pyplot as plt

# # CSV 파일 경로 설정
# file_path = 'C:\\Users\\SSAFY\\Desktop\\0726\\pjt\\pjt02\\버전1_금융\\archive\\NFLX.csv'

# # CSV 파일 읽어오기 (특정 열만)
# df = pd.read_csv(file_path, usecols=['Date', 'Open', 'High', 'Low', 'Close'], on_bad_lines='skip')

# # 'Date' 열을 datetime 형식으로 변환
# df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# # 2021년 이후의 데이터 필터링
# df_2021_onwards = df[df['Date'] >= '2021-01-01']

# # 필터링된 데이터의 종가 시각화
# plt.figure(figsize=(14, 8))
# plt.plot(df_2021_onwards['Date'], df_2021_onwards['Close'], label='종가', color='blue', marker='o')
# plt.title('2021년 이후 넷플릭스 주식 종가')
# plt.xlabel('날짜')
# plt.ylabel('종가')
# plt.legend()
# plt.grid(True)
# plt.xticks(rotation=45)
# plt.tight_layout()

# # 그래프 출력
# # plt.show()

# import pandas as pd

# # CSV 파일 경로 설정
# file_path = 'C:\\Users\\SSAFY\\Desktop\\0726\\pjt\\pjt02\\버전1_금융\\archive\\NFLX.csv'

# # CSV 파일 읽어오기 (특정 열만)
# df = pd.read_csv(file_path, usecols=['Date', 'Open', 'High', 'Low', 'Close'], on_bad_lines='skip')

# # 'Date' 열을 datetime 형식으로 변환
# df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# # 2021년 이후의 데이터 필터링
# df_2021_onwards = df[df['Date'] >= '2021-01-01']

# # 필터링된 데이터 출력
# print(df_2021_onwards)

# import pandas as pd

# # CSV 파일 경로 설정
# file_path = 'C:\\Users\\SSAFY\\Desktop\\0726\\pjt\\pjt02\\버전1_금융\\archive\\NFLX.csv'

# # CSV 파일 읽어오기 (특정 열만)
# df = pd.read_csv(file_path, usecols=['Date', 'Open', 'High', 'Low', 'Close'], on_bad_lines='skip')

# # 'Date' 열을 datetime 형식으로 변환
# df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# # 2021년 이후의 데이터 필터링
# df_2021_onwards = df[df['Date'] >= '2021-01-01']

# # 가장 높은 종가와 가장 낮은 종가 찾기
# highest_close = df_2021_onwards['Close'].max()
# lowest_close = df_2021_onwards['Close'].min()

# # 결과 출력
# print(f"2021년 이후 가장 높은 종가: {highest_close}")
# print(f"2021년 이후 가장 낮은 종가: {lowest_close}")

# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib import font_manager, rc

# # 한글 글꼴 설정 (선택사항)
# font_path = "C:\\Windows\\Fonts\\malgun.ttf"  # Windows의 'Malgun Gothic' 글꼴 경로
# font = font_manager.FontProperties(fname=font_path).get_name()
# rc('font', family=font)

# # CSV 파일 경로 설정
# file_path = 'C:\\Users\\SSAFY\\Desktop\\0726\\pjt\\pjt02\\버전1_금융\\archive\\NFLX.csv'

# # CSV 파일 읽어오기 (특정 열만)
# df = pd.read_csv(file_path, usecols=['Date', 'Open', 'High', 'Low', 'Close'], on_bad_lines='skip')

# # 'Date' 열을 datetime 형식으로 변환
# df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# # 2021년 이후의 데이터 필터링
# df_2021_onwards = df[df['Date'] >= '2021-01-01']

# # 월별 평균 종가 계산
# df_2021_onwards.set_index('Date', inplace=True)
# monthly_avg_close = df_2021_onwards['Close'].resample('M').mean()

# # 그래프 시각화
# plt.figure(figsize=(14, 8))
# plt.plot(monthly_avg_close.index, monthly_avg_close, label='월별 평균 종가', color='blue', marker='o')
# plt.title('2021년 이후 월별 넷플릭스 주식 평균 종가')
# plt.xlabel('날짜')
# plt.ylabel('평균 종가')
# plt.legend()
# plt.grid(True)
# plt.xticks(rotation=45)
# plt.tight_layout()

# # 그래프 출력
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib import font_manager, rc

# # 한글 글꼴 설정 (선택사항)
# font_path = "C:\\Windows\\Fonts\\malgun.ttf"  # Windows의 'Malgun Gothic' 글꼴 경로
# font = font_manager.FontProperties(fname=font_path).get_name()
# rc('font', family=font)

# # CSV 파일 경로 설정
# file_path = 'C:\\Users\\SSAFY\\Desktop\\0726\\pjt\\pjt02\\버전1_금융\\archive\\NFLX.csv'

# # CSV 파일 읽어오기 (특정 열만)
# df = pd.read_csv(file_path, usecols=['Date', 'Open', 'High', 'Low', 'Close'], on_bad_lines='skip')

# # 'Date' 열을 datetime 형식으로 변환
# df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# # 2021년 이후의 데이터 필터링
# df_2021_onwards = df[df['Date'] >= '2021-01-01']

# # 월별 평균 종가, 최고가, 최저가 계산
# df_2021_onwards.set_index('Date', inplace=True)
# monthly_data = df_2021_onwards.resample('ME').agg({
#     'Close': 'mean',
#     'High': 'max',
#     'Low': 'min'
# })

# # 그래프 시각화
# plt.figure(figsize=(14, 8))

# plt.plot(monthly_data.index, monthly_data['Close'], label='월별 평균 종가', marker='o', color='blue')
# plt.plot(monthly_data.index, monthly_data['High'], label='월별 최고가', marker='o', color='red')
# plt.plot(monthly_data.index, monthly_data['Low'], label='월별 최저가', marker='o', color='green')

# plt.title('2021년 이후 월별 넷플릭스 주식 분석')
# plt.xlabel('날짜')
# plt.ylabel('가격')
# plt.legend()
# plt.grid(True)
# plt.xticks(rotation=45)
# plt.tight_layout()

# # 그래프 출력
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import warnings

# 경고 메시지 무시
warnings.filterwarnings("ignore")

# CSV 파일 경로 설정
file_path = 'C:\\Users\\SSAFY\\Desktop\\0726\\pjt\\pjt02\\버전1_금융\\archive\\NFLX.csv'

# CSV 파일 읽어오기 (특정 열만)
df = pd.read_csv(file_path, usecols=['Date', 'Close'], on_bad_lines='skip')

# 'Date' 열을 datetime 형식으로 변환
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# 2021년 이후의 데이터 필터링
df_2021_onwards = df[df['Date'] >= '2021-01-01']

# 'Date' 열을 인덱스로 설정
df_2021_onwards.set_index('Date', inplace=True)

# ARIMA 모델 학습
model = ARIMA(df_2021_onwards['Close'], order=(5, 1, 0))  # order 파라미터는 (p, d, q)를 의미
model_fit = model.fit()

# 미래 30일 예측
forecast = model_fit.forecast(steps=30)

# 예측 결과 시각화
plt.figure(figsize=(14, 8))
plt.plot(df_2021_onwards.index, df_2021_onwards['Close'], label='실제 종가')
plt.plot(forecast.index, forecast, label='예측 종가', color='red')
plt.title('넷플릭스 주가 예측')
plt.xlabel('날짜')
plt.ylabel('종가')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# 그래프 출력
plt.show()

















