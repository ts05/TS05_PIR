from keras.utils import *
import tensorflow as tf
import numpy as np
import matplotlib.pylab as plt
from keras.models import model_from_json
import seaborn as sns
import Data_load as dl
import os
import random

#modelname = input("Type Model's name :: ")
modelname = "Model_activef"
modelname_json = "Models/" + modelname + ".json"
modelname_weight = "Models/" + modelname + ".h5"
json_file = open(modelname_json,"r")

loaded_model_json = json_file.read()
json_file.close()

model = tf.keras.models.model_from_json(loaded_model_json)
model.load_weights(modelname_weight)
print("Model Loaded...!")

current_path = os.getcwd()

DataX = list()
DataY = list()

Data_Animal_X = list()
Data_Animal_Y = list()

Data_Both_X = list()
Data_Both_Y = list()

Data_sun_human = list()
Data_sun_human_Y = list()
Data_rain_human = list()
Data_rain_human_Y = list()
Data_sun_none = list()
Data_sun_none_Y = list()
Data_rain_none = list()
Data_rain_none_Y = list()

dl.Data_load("Sunny", "Animal", 3, Data_Animal_X, Data_Animal_Y)

dl.Data_load("Sunny", "Human", 3, DataX, DataY)

#dl.Data_load("Sunny", "Both", 3, Data_Both_X, Data_Both_Y)

dl.Data_load("Sunny", "Human", 3, Data_sun_human, Data_sun_human_Y)

dl.Data_load("Rain", "Human", 3, Data_rain_human, Data_rain_human_Y)

dl.Data_load("Sunny", "None", 3, Data_sun_none, Data_sun_none_Y)

dl.Data_load("Rain", "None", 3, Data_rain_none, Data_rain_none_Y)

sun = list()
rain = list()
sun_ani = list()
sun_none = list()
rain_none = list()

for i in range(0,3000):
    j = random.randrange(0, Data_sun_human.__len__())
    sun.append(Data_sun_human[j])
    j = random.randrange(0, Data_rain_human.__len__())
    rain.append(Data_rain_human[j])
    j = random.randrange(0, Data_Animal_X.__len__())
    sun_ani.append(Data_Animal_X[j])
    j = random.randrange(0, Data_sun_none.__len__())
    sun_none.append(Data_sun_none[j])
    j = random.randrange(0, Data_rain_none.__len__())
    rain_none.append(Data_rain_none[j])
    print(j)

# 1 ~ 3 : sunny human, 4, 5 : rain none
test_data = np.array([[
2100.0,2065.0,2028.0,1990.0,1940.0,1831.0,1952.0,2156.0,2216.0,2211.0,2139.0,2088.0,2040.0,2001.0,1940.0,1834.0,1973.0,2151.0,2200.0,2184.0,2121.0,2080.0,2031.0,1936.0,1943.0,1858.0,1957.0,2180.0,2215.0,2198.0,2125.0,2074.0,2028.0,1982.0,1926.0,1814.0,1920.0,2157.0,2200.0,2179.0,2120.0,2063.0,2024.0,1977.0,1920.0,1815.0,2076.0,2121.0,2100.0,2178.0,2156.0,2123.0,2080.0,2018.0,1953.0,1839.0,1936.0,2171.0,2210.0,2188.0,2127.0,2072.0,2025.0,1986.0,1930.0,1829.0,1932.0,2175.0,2220.0,2203.0,2136.0,2081.0,2040.0,2007.0,1952.0,1846.0,1963.0,2188.0,2228.0,2212.0,2139.0,2096.0,2051.0,2022.0,1965.0,1870.0,1962.0,2212.0,2251.0,2233.0,2167.0,2111.0,2080.0,2034.0,1976.0,1874.0,2083.0,2201.0,2221.0,2208.0
],[1834.0,1973.0,2151.0,2200.0,2184.0,2121.0,2080.0,2031.0,1936.0,1943.0,1858.0,1957.0,2180.0,2215.0,2198.0,2125.0,2074.0,2028.0,1982.0,1926.0,1814.0,1920.0,2157.0,2200.0,2179.0,2120.0,2063.0,2024.0,1977.0,1920.0,1815.0,2076.0,2121.0,2100.0,2178.0,2156.0,2123.0,2080.0,2018.0,1953.0,1839.0,1936.0,2171.0,2210.0,2188.0,2127.0,2072.0,2025.0,1986.0,1930.0,1829.0,1932.0,2175.0,2220.0,2203.0,2136.0,2081.0,2040.0,2007.0,1952.0,1846.0,1963.0,2188.0,2228.0,2212.0,2139.0,2096.0,2051.0,2022.0,1965.0,1870.0,1962.0,2212.0,2251.0,2233.0,2167.0,2111.0,2080.0,2034.0,1976.0,1874.0,2083.0,2201.0,2221.0,2208.0,2145.0,2108.0,2067.0,2032.0,1968.0,1868.0,1999.0,2121.0,2244.0,2267.0,2220.0,2152.0,2096.0,2033.0,1966.0
],[2125.0,2074.0,2028.0,1982.0,1926.0,1814.0,1920.0,2157.0,2200.0,2179.0,2120.0,2063.0,2024.0,1977.0,1920.0,1815.0,2076.0,2121.0,2100.0,2178.0,2156.0,2123.0,2080.0,2018.0,1953.0,1839.0,1936.0,2171.0,2210.0,2188.0,2127.0,2072.0,2025.0,1986.0,1930.0,1829.0,1932.0,2175.0,2220.0,2203.0,2136.0,2081.0,2040.0,2007.0,1952.0,1846.0,1963.0,2188.0,2228.0,2212.0,2139.0,2096.0,2051.0,2022.0,1965.0,1870.0,1962.0,2212.0,2251.0,2233.0,2167.0,2111.0,2080.0,2034.0,1976.0,1874.0,2083.0,2201.0,2221.0,2208.0,2145.0,2108.0,2067.0,2032.0,1968.0,1868.0,1999.0,2121.0,2244.0,2267.0,2220.0,2152.0,2096.0,2033.0,1966.0,1853.0,1935.0,2149.0,2219.0,2185.0,2102.0,2050.0,2004.0,1960.0,1909.0,1795.0,1897.0,2105.0,2191.0,2152.0
],[1815.0,2076.0,2121.0,2100.0,2178.0,2156.0,2123.0,2080.0,2018.0,1953.0,1839.0,1936.0,2171.0,2210.0,2188.0,2127.0,2072.0,2025.0,1986.0,1930.0,1829.0,1932.0,2175.0,2220.0,2203.0,2136.0,2081.0,2040.0,2007.0,1952.0,1846.0,1963.0,2188.0,2228.0,2212.0,2139.0,2096.0,2051.0,2022.0,1965.0,1870.0,1962.0,2212.0,2251.0,2233.0,2167.0,2111.0,2080.0,2034.0,1976.0,1874.0,2083.0,2201.0,2221.0,2208.0,2145.0,2108.0,2067.0,2032.0,1968.0,1868.0,1999.0,2121.0,2244.0,2267.0,2220.0,2152.0,2096.0,2033.0,1966.0,1853.0,1935.0,2149.0,2219.0,2185.0,2102.0,2050.0,2004.0,1960.0,1909.0,1795.0,1897.0,2105.0,2191.0,2152.0,2082.0,2024.0,1977.0,1940.0,1888.0,1781.0,1889.0,2089.0,2160.0,2137.0,2062.0,2016.0,1976.0,1929.0,1875.0
],[2127.0,2072.0,2025.0,1986.0,1930.0,1829.0,1932.0,2175.0,2220.0,2203.0,2136.0,2081.0,2040.0,2007.0,1952.0,1846.0,1963.0,2188.0,2228.0,2212.0,2139.0,2096.0,2051.0,2022.0,1965.0,1870.0,1962.0,2212.0,2251.0,2233.0,2167.0,2111.0,2080.0,2034.0,1976.0,1874.0,2083.0,2201.0,2221.0,2208.0,2145.0,2108.0,2067.0,2032.0,1968.0,1868.0,1999.0,2121.0,2244.0,2267.0,2220.0,2152.0,2096.0,2033.0,1966.0,1853.0,1935.0,2149.0,2219.0,2185.0,2102.0,2050.0,2004.0,1960.0,1909.0,1795.0,1897.0,2105.0,2191.0,2152.0,2082.0,2024.0,1977.0,1940.0,1888.0,1781.0,1889.0,2089.0,2160.0,2137.0,2062.0,2016.0,1976.0,1929.0,1875.0,1768.0,1983.0,2081.0,2136.0,2111.0,2049.0,2003.0,1961.0,1935.0,1879.0,1776.0,1878.0,2098.0,2182.0,2156.0
],[1846.0,1963.0,2188.0,2228.0,2212.0,2139.0,2096.0,2051.0,2022.0,1965.0,1870.0,1962.0,2212.0,2251.0,2233.0,2167.0,2111.0,2080.0,2034.0,1976.0,1874.0,2083.0,2201.0,2221.0,2208.0,2145.0,2108.0,2067.0,2032.0,1968.0,1868.0,1999.0,2121.0,2244.0,2267.0,2220.0,2152.0,2096.0,2033.0,1966.0,1853.0,1935.0,2149.0,2219.0,2185.0,2102.0,2050.0,2004.0,1960.0,1909.0,1795.0,1897.0,2105.0,2191.0,2152.0,2082.0,2024.0,1977.0,1940.0,1888.0,1781.0,1889.0,2089.0,2160.0,2137.0,2062.0,2016.0,1976.0,1929.0,1875.0,1768.0,1983.0,2081.0,2136.0,2111.0,2049.0,2003.0,1961.0,1935.0,1879.0,1776.0,1878.0,2098.0,2182.0,2156.0,2079.0,2020.0,1984.0,1947.0,1902.0,1793.0,1933.0,2024.0,2194.0,2228.0,2166.0,2115.0,2051.0,1940.0,1933.0
],[2167.0,2111.0,2080.0,2034.0,1976.0,1874.0,2083.0,2201.0,2221.0,2208.0,2145.0,2108.0,2067.0,2032.0,1968.0,1868.0,1999.0,2121.0,2244.0,2267.0,2220.0,2152.0,2096.0,2033.0,1966.0,1853.0,1935.0,2149.0,2219.0,2185.0,2102.0,2050.0,2004.0,1960.0,1909.0,1795.0,1897.0,2105.0,2191.0,2152.0,2082.0,2024.0,1977.0,1940.0,1888.0,1781.0,1889.0,2089.0,2160.0,2137.0,2062.0,2016.0,1976.0,1929.0,1875.0,1768.0,1983.0,2081.0,2136.0,2111.0,2049.0,2003.0,1961.0,1935.0,1879.0,1776.0,1878.0,2098.0,2182.0,2156.0,2079.0,2020.0,1984.0,1947.0,1902.0,1793.0,1933.0,2024.0,2194.0,2228.0,2166.0,2115.0,2051.0,1940.0,1933.0,1855.0,1953.0,2168.0,2241.0,2199.0,2120.0,2058.0,2021.0,1985.0,1928.0,1824.0,1924.0,2145.0,2240.0,2217.0
],[1868.0,1999.0,2121.0,2244.0,2267.0,2220.0,2152.0,2096.0,2033.0,1966.0,1853.0,1935.0,2149.0,2219.0,2185.0,2102.0,2050.0,2004.0,1960.0,1909.0,1795.0,1897.0,2105.0,2191.0,2152.0,2082.0,2024.0,1977.0,1940.0,1888.0,1781.0,1889.0,2089.0,2160.0,2137.0,2062.0,2016.0,1976.0,1929.0,1875.0,1768.0,1983.0,2081.0,2136.0,2111.0,2049.0,2003.0,1961.0,1935.0,1879.0,1776.0,1878.0,2098.0,2182.0,2156.0,2079.0,2020.0,1984.0,1947.0,1902.0,1793.0,1933.0,2024.0,2194.0,2228.0,2166.0,2115.0,2051.0,1940.0,1933.0,1855.0,1953.0,2168.0,2241.0,2199.0,2120.0,2058.0,2021.0,1985.0,1928.0,1824.0,1924.0,2145.0,2240.0,2217.0,2131.0,2083.0,2036.0,2012.0,1947.0,1852.0,2075.0,2164.0,2219.0,2208.0,2139.0,2089.0,2054.0,2023.0,2006.0
],[2102.0,2050.0,2004.0,1960.0,1909.0,1795.0,1897.0,2105.0,2191.0,2152.0,2082.0,2024.0,1977.0,1940.0,1888.0,1781.0,1889.0,2089.0,2160.0,2137.0,2062.0,2016.0,1976.0,1929.0,1875.0,1768.0,1983.0,2081.0,2136.0,2111.0,2049.0,2003.0,1961.0,1935.0,1879.0,1776.0,1878.0,2098.0,2182.0,2156.0,2079.0,2020.0,1984.0,1947.0,1902.0,1793.0,1933.0,2024.0,2194.0,2228.0,2166.0,2115.0,2051.0,1940.0,1933.0,1855.0,1953.0,2168.0,2241.0,2199.0,2120.0,2058.0,2021.0,1985.0,1928.0,1824.0,1924.0,2145.0,2240.0,2217.0,2131.0,2083.0,2036.0,2012.0,1947.0,1852.0,2075.0,2164.0,2219.0,2208.0,2139.0,2089.0,2054.0,2023.0,2006.0,1861.0,1937.0,2160.0,2242.0,2241.0,2158.0,2110.0,2076.0,2029.0,1993.0,1879.0,1973.0,2208.0,2274.0,2262.0
],[1781.0,1889.0,2089.0,2160.0,2137.0,2062.0,2016.0,1976.0,1929.0,1875.0,1768.0,1983.0,2081.0,2136.0,2111.0,2049.0,2003.0,1961.0,1935.0,1879.0,1776.0,1878.0,2098.0,2182.0,2156.0,2079.0,2020.0,1984.0,1947.0,1902.0,1793.0,1933.0,2024.0,2194.0,2228.0,2166.0,2115.0,2051.0,1940.0,1933.0,1855.0,1953.0,2168.0,2241.0,2199.0,2120.0,2058.0,2021.0,1985.0,1928.0,1824.0,1924.0,2145.0,2240.0,2217.0,2131.0,2083.0,2036.0,2012.0,1947.0,1852.0,2075.0,2164.0,2219.0,2208.0,2139.0,2089.0,2054.0,2023.0,2006.0,1861.0,1937.0,2160.0,2242.0,2241.0,2158.0,2110.0,2076.0,2029.0,1993.0,1879.0,1973.0,2208.0,2274.0,2262.0,2186.0,2125.0,2085.0,2041.0,1981.0,1881.0,2011.0,2040.0,2229.0,2346.0,2296.0,2228.0,2170.0,2109.0,2031.0
],[2049.0,2003.0,1961.0,1935.0,1879.0,1776.0,1878.0,2098.0,2182.0,2156.0,2079.0,2020.0,1984.0,1947.0,1902.0,1793.0,1933.0,2024.0,2194.0,2228.0,2166.0,2115.0,2051.0,1940.0,1933.0,1855.0,1953.0,2168.0,2241.0,2199.0,2120.0,2058.0,2021.0,1985.0,1928.0,1824.0,1924.0,2145.0,2240.0,2217.0,2131.0,2083.0,2036.0,2012.0,1947.0,1852.0,2075.0,2164.0,2219.0,2208.0,2139.0,2089.0,2054.0,2023.0,2006.0,1861.0,1937.0,2160.0,2242.0,2241.0,2158.0,2110.0,2076.0,2029.0,1993.0,1879.0,1973.0,2208.0,2274.0,2262.0,2186.0,2125.0,2085.0,2041.0,1981.0,1881.0,2011.0,2040.0,2229.0,2346.0,2296.0,2228.0,2170.0,2109.0,2031.0,1905.0,1988.0,2193.0,2244.0,2254.0,2162.0,2089.0,2040.0,2001.0,1940.0,1846.0,2052.0,2162.0,2194.0,2228.0
],[1793.0,1933.0,2024.0,2194.0,2228.0,2166.0,2115.0,2051.0,1940.0,1933.0,1855.0,1953.0,2168.0,2241.0,2199.0,2120.0,2058.0,2021.0,1985.0,1928.0,1824.0,1924.0,2145.0,2240.0,2217.0,2131.0,2083.0,2036.0,2012.0,1947.0,1852.0,2075.0,2164.0,2219.0,2208.0,2139.0,2089.0,2054.0,2023.0,2006.0,1861.0,1937.0,2160.0,2242.0,2241.0,2158.0,2110.0,2076.0,2029.0,1993.0,1879.0,1973.0,2208.0,2274.0,2262.0,2186.0,2125.0,2085.0,2041.0,1981.0,1881.0,2011.0,2040.0,2229.0,2346.0,2296.0,2228.0,2170.0,2109.0,2031.0,1905.0,1988.0,2193.0,2244.0,2254.0,2162.0,2089.0,2040.0,2001.0,1940.0,1846.0,2052.0,2162.0,2194.0,2228.0,2152.0,2099.0,2068.0,2028.0,1985.0,1884.0,2002.0,2211.0,2270.0,2284.0,2196.0,2135.0,2090.0,2051.0,2001.0
],[2120.0,2058.0,2021.0,1985.0,1928.0,1824.0,1924.0,2145.0,2240.0,2217.0,2131.0,2083.0,2036.0,2012.0,1947.0,1852.0,2075.0,2164.0,2219.0,2208.0,2139.0,2089.0,2054.0,2023.0,2006.0,1861.0,1937.0,2160.0,2242.0,2241.0,2158.0,2110.0,2076.0,2029.0,1993.0,1879.0,1973.0,2208.0,2274.0,2262.0,2186.0,2125.0,2085.0,2041.0,1981.0,1881.0,2011.0,2040.0,2229.0,2346.0,2296.0,2228.0,2170.0,2109.0,2031.0,1905.0,1988.0,2193.0,2244.0,2254.0,2162.0,2089.0,2040.0,2001.0,1940.0,1846.0,2052.0,2162.0,2194.0,2228.0,2152.0,2099.0,2068.0,2028.0,1985.0,1884.0,2002.0,2211.0,2270.0,2284.0,2196.0,2135.0,2090.0,2051.0,2001.0,1894.0,1983.0,2218.0,2272.0,2289.0,2205.0,2141.0,2091.0,2045.0,1992.0,1891.0,1992.0,2224.0,2280.0,2304.0
],[1852.0,2075.0,2164.0,2219.0,2208.0,2139.0,2089.0,2054.0,2023.0,2006.0,1861.0,1937.0,2160.0,2242.0,2241.0,2158.0,2110.0,2076.0,2029.0,1993.0,1879.0,1973.0,2208.0,2274.0,2262.0,2186.0,2125.0,2085.0,2041.0,1981.0,1881.0,2011.0,2040.0,2229.0,2346.0,2296.0,2228.0,2170.0,2109.0,2031.0,1905.0,1988.0,2193.0,2244.0,2254.0,2162.0,2089.0,2040.0,2001.0,1940.0,1846.0,2052.0,2162.0,2194.0,2228.0,2152.0,2099.0,2068.0,2028.0,1985.0,1884.0,2002.0,2211.0,2270.0,2284.0,2196.0,2135.0,2090.0,2051.0,2001.0,1894.0,1983.0,2218.0,2272.0,2289.0,2205.0,2141.0,2091.0,2045.0,1992.0,1891.0,1992.0,2224.0,2280.0,2304.0,2211.0,2140.0,2096.0,2051.0,1994.0,1892.0,2048.0,2112.0,2260.0,2331.0,2261.0,2176.0,2120.0,2055.0,1988.0
],[2158.0,2110.0,2076.0,2029.0,1993.0,1879.0,1973.0,2208.0,2274.0,2262.0,2186.0,2125.0,2085.0,2041.0,1981.0,1881.0,2011.0,2040.0,2229.0,2346.0,2296.0,2228.0,2170.0,2109.0,2031.0,1905.0,1988.0,2193.0,2244.0,2254.0,2162.0,2089.0,2040.0,2001.0,1940.0,1846.0,2052.0,2162.0,2194.0,2228.0,2152.0,2099.0,2068.0,2028.0,1985.0,1884.0,2002.0,2211.0,2270.0,2284.0,2196.0,2135.0,2090.0,2051.0,2001.0,1894.0,1983.0,2218.0,2272.0,2289.0,2205.0,2141.0,2091.0,2045.0,1992.0,1891.0,1992.0,2224.0,2280.0,2304.0,2211.0,2140.0,2096.0,2051.0,1994.0,1892.0,2048.0,2112.0,2260.0,2331.0,2261.0,2176.0,2120.0,2055.0,1988.0,1874.0,2086.0,2195.0,2205.0,2237.0,2160.0,2090.0,2050.0,2007.0,1957.0,1857.0,1964.0,2185.0,2248.0,2255.0
],[1881.0,2011.0,2040.0,2229.0,2346.0,2296.0,2228.0,2170.0,2109.0,2031.0,1905.0,1988.0,2193.0,2244.0,2254.0,2162.0,2089.0,2040.0,2001.0,1940.0,1846.0,2052.0,2162.0,2194.0,2228.0,2152.0,2099.0,2068.0,2028.0,1985.0,1884.0,2002.0,2211.0,2270.0,2284.0,2196.0,2135.0,2090.0,2051.0,2001.0,1894.0,1983.0,2218.0,2272.0,2289.0,2205.0,2141.0,2091.0,2045.0,1992.0,1891.0,1992.0,2224.0,2280.0,2304.0,2211.0,2140.0,2096.0,2051.0,1994.0,1892.0,2048.0,2112.0,2260.0,2331.0,2261.0,2176.0,2120.0,2055.0,1988.0,1874.0,2086.0,2195.0,2205.0,2237.0,2160.0,2090.0,2050.0,2007.0,1957.0,1857.0,1964.0,2185.0,2248.0,2255.0,2186.0,2108.0,2052.0,2001.0,1957.0,1855.0,1968.0,2183.0,2227.0,2227.0,2168.0,2092.0,2048.0,1932.0,1949.0
],[2162.0,2089.0,2040.0,2001.0,1940.0,1846.0,2052.0,2162.0,2194.0,2228.0,2152.0,2099.0,2068.0,2028.0,1985.0,1884.0,2002.0,2211.0,2270.0,2284.0,2196.0,2135.0,2090.0,2051.0,2001.0,1894.0,1983.0,2218.0,2272.0,2289.0,2205.0,2141.0,2091.0,2045.0,1992.0,1891.0,1992.0,2224.0,2280.0,2304.0,2211.0,2140.0,2096.0,2051.0,1994.0,1892.0,2048.0,2112.0,2260.0,2331.0,2261.0,2176.0,2120.0,2055.0,1988.0,1874.0,2086.0,2195.0,2205.0,2237.0,2160.0,2090.0,2050.0,2007.0,1957.0,1857.0,1964.0,2185.0,2248.0,2255.0,2186.0,2108.0,2052.0,2001.0,1957.0,1855.0,1968.0,2183.0,2227.0,2227.0,2168.0,2092.0,2048.0,1932.0,1949.0,1881.0,1989.0,2205.0,2249.0,2227.0,2169.0,2073.0,2012.0,1955.0,1891.0,1796.0,1889.0,2110.0,2162.0,2156.0
],[1884.0,2002.0,2211.0,2270.0,2284.0,2196.0,2135.0,2090.0,2051.0,2001.0,1894.0,1983.0,2218.0,2272.0,2289.0,2205.0,2141.0,2091.0,2045.0,1992.0,1891.0,1992.0,2224.0,2280.0,2304.0,2211.0,2140.0,2096.0,2051.0,1994.0,1892.0,2048.0,2112.0,2260.0,2331.0,2261.0,2176.0,2120.0,2055.0,1988.0,1874.0,2086.0,2195.0,2205.0,2237.0,2160.0,2090.0,2050.0,2007.0,1957.0,1857.0,1964.0,2185.0,2248.0,2255.0,2186.0,2108.0,2052.0,2001.0,1957.0,1855.0,1968.0,2183.0,2227.0,2227.0,2168.0,2092.0,2048.0,1932.0,1949.0,1881.0,1989.0,2205.0,2249.0,2227.0,2169.0,2073.0,2012.0,1955.0,1891.0,1796.0,1889.0,2110.0,2162.0,2156.0,2108.0,2008.0,1955.0,1897.0,1842.0,1739.0,1999.0,1995.0,2031.0,2087.0,2072.0,1990.0,1924.0,1848.0,1776.0
],[2205.0,2141.0,2091.0,2045.0,1992.0,1891.0,1992.0,2224.0,2280.0,2304.0,2211.0,2140.0,2096.0,2051.0,1994.0,1892.0,2048.0,2112.0,2260.0,2331.0,2261.0,2176.0,2120.0,2055.0,1988.0,1874.0,2086.0,2195.0,2205.0,2237.0,2160.0,2090.0,2050.0,2007.0,1957.0,1857.0,1964.0,2185.0,2248.0,2255.0,2186.0,2108.0,2052.0,2001.0,1957.0,1855.0,1968.0,2183.0,2227.0,2227.0,2168.0,2092.0,2048.0,1932.0,1949.0,1881.0,1989.0,2205.0,2249.0,2227.0,2169.0,2073.0,2012.0,1955.0,1891.0,1796.0,1889.0,2110.0,2162.0,2156.0,2108.0,2008.0,1955.0,1897.0,1842.0,1739.0,1999.0,1995.0,2031.0,2087.0,2072.0,1990.0,1924.0,1848.0,1776.0,1664.0,1755.0,1960.0,2000.0,1976.0,1933.0,1843.0,1789.0,1736.0,1677.0,1574.0,1686.0,1888.0,1937.0,1928.0
],[1892.0,2048.0,2112.0,2260.0,2331.0,2261.0,2176.0,2120.0,2055.0,1988.0,1874.0,2086.0,2195.0,2205.0,2237.0,2160.0,2090.0,2050.0,2007.0,1957.0,1857.0,1964.0,2185.0,2248.0,2255.0,2186.0,2108.0,2052.0,2001.0,1957.0,1855.0,1968.0,2183.0,2227.0,2227.0,2168.0,2092.0,2048.0,1932.0,1949.0,1881.0,1989.0,2205.0,2249.0,2227.0,2169.0,2073.0,2012.0,1955.0,1891.0,1796.0,1889.0,2110.0,2162.0,2156.0,2108.0,2008.0,1955.0,1897.0,1842.0,1739.0,1999.0,1995.0,2031.0,2087.0,2072.0,1990.0,1924.0,1848.0,1776.0,1664.0,1755.0,1960.0,2000.0,1976.0,1933.0,1843.0,1789.0,1736.0,1677.0,1574.0,1686.0,1888.0,1937.0,1928.0,1893.0,1811.0,1756.0,1702.0,1650.0,1552.0,1662.0,1864.0,1917.0,1906.0,1887.0,1802.0,1752.0,1704.0,1654.0
],[2160.0,2090.0,2050.0,2007.0,1957.0,1857.0,1964.0,2185.0,2248.0,2255.0,2186.0,2108.0,2052.0,2001.0,1957.0,1855.0,1968.0,2183.0,2227.0,2227.0,2168.0,2092.0,2048.0,1932.0,1949.0,1881.0,1989.0,2205.0,2249.0,2227.0,2169.0,2073.0,2012.0,1955.0,1891.0,1796.0,1889.0,2110.0,2162.0,2156.0,2108.0,2008.0,1955.0,1897.0,1842.0,1739.0,1999.0,1995.0,2031.0,2087.0,2072.0,1990.0,1924.0,1848.0,1776.0,1664.0,1755.0,1960.0,2000.0,1976.0,1933.0,1843.0,1789.0,1736.0,1677.0,1574.0,1686.0,1888.0,1937.0,1928.0,1893.0,1811.0,1756.0,1702.0,1650.0,1552.0,1662.0,1864.0,1917.0,1906.0,1887.0,1802.0,1752.0,1704.0,1654.0,1554.0,1676.0,1888.0,1940.0,1944.0,1915.0,1845.0,1794.0,1752.0,1707.0,1612.0,1839.0,1949.0,1992.0,2002.0
],[1855.0,1968.0,2183.0,2227.0,2227.0,2168.0,2092.0,2048.0,1932.0,1949.0,1881.0,1989.0,2205.0,2249.0,2227.0,2169.0,2073.0,2012.0,1955.0,1891.0,1796.0,1889.0,2110.0,2162.0,2156.0,2108.0,2008.0,1955.0,1897.0,1842.0,1739.0,1999.0,1995.0,2031.0,2087.0,2072.0,1990.0,1924.0,1848.0,1776.0,1664.0,1755.0,1960.0,2000.0,1976.0,1933.0,1843.0,1789.0,1736.0,1677.0,1574.0,1686.0,1888.0,1937.0,1928.0,1893.0,1811.0,1756.0,1702.0,1650.0,1552.0,1662.0,1864.0,1917.0,1906.0,1887.0,1802.0,1752.0,1704.0,1654.0,1554.0,1676.0,1888.0,1940.0,1944.0,1915.0,1845.0,1794.0,1752.0,1707.0,1612.0,1839.0,1949.0,1992.0,2002.0,2001.0,1937.0,1898.0,1847.0,1802.0,1721.0,1880.0,1976.0,2120.0,2178.0,2160.0,2104.0,2054.0,1984.0,1930.0
]])

test_data = np.reshape(test_data, (test_data.shape[0], 1, test_data.shape[1]))

plt.title("Exist Human(Blue:Sun, Red:Rain)")
testhuman = sns.tsplot(data = sun, color = "blue")
testnone = sns.tsplot(data = rain, color = "red")

print(type(testhuman))
print(testhuman)
testhuman = np.asarray(testhuman, (1,100))
testnone = np.asarray(testnone, (1, 100))
plt.legend()
plt.show()


result = model.predict(test_data)
result_hu = model.predict(testhuman)
result_no = model.predict(testnone)

print(result)
print(result_hu)
print(result_no)

"""
weather = result.index(max(result[:2]))

if weather == 0 :
    print("Sunny")
else :
    print("Rain")

exist = result.index(max(result[2:6]))

if exist == 2:
    print("None")
elif exist == 3:
    print("Animal")
elif exist == 4:
    print("Both")
elif exist == 5:
    print("Human")

"""