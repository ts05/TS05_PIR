from keras.utils import *
import tensorflow as tf
import numpy as np
from keras.models import model_from_json

#modelname = input("Type Model's name :: ")
modelname = "Model_notboth_lstm1_ep1000"
modelname_json = "Models/" + modelname + ".json"
modelname_weight = "Models/" + modelname + ".h5"
json_file = open(modelname_json,"r")

loaded_model_json = json_file.read()
json_file.close()

model = tf.keras.models.model_from_json(loaded_model_json)
model.load_weights(modelname_weight)
print("Model Loaded...! :: " + modelname)

# 0 ~ 2 : sunny human, 3 ~ 5 : sunny none  6 ~ 8 : rain none
test_data = np.array([[
1760.0,2100.0,2132.0,2188.0,2194.0,2159.0,2118.0,2082.0,2026.0,1964.0,1748.0,1856.0,2090.0,2232.0,2242.0,2188.0,2137.0,2089.0,2029.0,1959.0,1747.0,1923.0,2032.0,2154.0,2262.0,2256.0,2202.0,2156.0,2080.0,1998.0,1760.0,1846.0,2068.0,2208.0,2217.0,2160.0,2119.0,2068.0,2017.0,1950.0,1670.0,1838.0,2089.0,2254.0,2252.0,2202.0,2132.0,2090.0,2016.0,1949.0,1729.0,2081.0,2120.0,2168.0,2178.0,2140.0,2114.0,2033.0,2000.0,1972.0,1779.0,1896.0,2128.0,2277.0,2282.0,2225.0,2162.0,2128.0,2058.0,1967.0,1752.0,1848.0,2075.0,2228.0,2240.0,2188.0,2146.0,2098.0,2057.0,1980.0,1751.0,1923.0,2029.0,2164.0,2260.0,2255.0,2209.0,2145.0,2099.0,1995.0,1776.0,1862.0,2096.0,2241.0,2258.0,2208.0,2156.0,2091.0,2075.0,2000.0
],[2188.0,2137.0,2089.0,2029.0,1959.0,1747.0,1923.0,2032.0,2154.0,2262.0,2256.0,2202.0,2156.0,2080.0,1998.0,1760.0,1846.0,2068.0,2208.0,2217.0,2160.0,2119.0,2068.0,2017.0,1950.0,1670.0,1838.0,2089.0,2254.0,2252.0,2202.0,2132.0,2090.0,2016.0,1949.0,1729.0,2081.0,2120.0,2168.0,2178.0,2140.0,2114.0,2033.0,2000.0,1972.0,1779.0,1896.0,2128.0,2277.0,2282.0,2225.0,2162.0,2128.0,2058.0,1967.0,1752.0,1848.0,2075.0,2228.0,2240.0,2188.0,2146.0,2098.0,2057.0,1980.0,1751.0,1923.0,2029.0,2164.0,2260.0,2255.0,2209.0,2145.0,2099.0,1995.0,1776.0,1862.0,2096.0,2241.0,2258.0,2208.0,2156.0,2091.0,2075.0,2000.0,1774.0,2102.0,2145.0,2222.0,2225.0,2186.0,2160.0,2096.0,2097.0,2010.0,1798.0,1920.0,2129.0,2278.0,2290.0
],[1760.0,1846.0,2068.0,2208.0,2217.0,2160.0,2119.0,2068.0,2017.0,1950.0,1670.0,1838.0,2089.0,2254.0,2252.0,2202.0,2132.0,2090.0,2016.0,1949.0,1729.0,2081.0,2120.0,2168.0,2178.0,2140.0,2114.0,2033.0,2000.0,1972.0,1779.0,1896.0,2128.0,2277.0,2282.0,2225.0,2162.0,2128.0,2058.0,1967.0,1752.0,1848.0,2075.0,2228.0,2240.0,2188.0,2146.0,2098.0,2057.0,1980.0,1751.0,1923.0,2029.0,2164.0,2260.0,2255.0,2209.0,2145.0,2099.0,1995.0,1776.0,1862.0,2096.0,2241.0,2258.0,2208.0,2156.0,2091.0,2075.0,2000.0,1774.0,2102.0,2145.0,2222.0,2225.0,2186.0,2160.0,2096.0,2097.0,2010.0,1798.0,1920.0,2129.0,2278.0,2290.0,2244.0,2194.0,2127.0,2118.0,2035.0,1802.0,1900.0,2132.0,2276.0,2286.0,2233.0,2184.0,2114.0,2116.0,2026.0
],[2144.0,2223.0,2282.0,2248.0,2216.0,2192.0,2166.0,2192.0,1993.0,2051.0,2280.0,2359.0,2393.0,2333.0,2280.0,2246.0,2205.0,2188.0,2016.0,2143.0,2244.0,2364.0,2450.0,2400.0,2340.0,2285.0,2232.0,2185.0,2016.0,2067.0,2284.0,2366.0,2385.0,2314.0,2240.0,2194.0,2146.0,2130.0,1954.0,2014.0,2240.0,2316.0,2353.0,2274.0,2213.0,2168.0,2121.0,2088.0,1928.0,2153.0,2229.0,2268.0,2315.0,2248.0,2184.0,2148.0,2100.0,2072.0,1908.0,1960.0,2197.0,2272.0,2316.0,2236.0,2170.0,2116.0,2072.0,1978.0,1881.0,1980.0,2208.0,2289.0,2314.0,2230.0,2144.0,2093.0,2040.0,2000.0,1850.0,1976.0,2074.0,2192.0,2292.0,2244.0,2176.0,2120.0,2057.0,2020.0,1848.0,1902.0,2126.0,2216.0,2236.0,2180.0,2104.0,2058.0,2008.0,1967.0,1813.0,2026.0
],[2246.0,2205.0,2188.0,2016.0,2143.0,2244.0,2364.0,2450.0,2400.0,2340.0,2285.0,2232.0,2185.0,2016.0,2067.0,2284.0,2366.0,2385.0,2314.0,2240.0,2194.0,2146.0,2130.0,1954.0,2014.0,2240.0,2316.0,2353.0,2274.0,2213.0,2168.0,2121.0,2088.0,1928.0,2153.0,2229.0,2268.0,2315.0,2248.0,2184.0,2148.0,2100.0,2072.0,1908.0,1960.0,2197.0,2272.0,2316.0,2236.0,2170.0,2116.0,2072.0,1978.0,1881.0,1980.0,2208.0,2289.0,2314.0,2230.0,2144.0,2093.0,2040.0,2000.0,1850.0,1976.0,2074.0,2192.0,2292.0,2244.0,2176.0,2120.0,2057.0,2020.0,1848.0,1902.0,2126.0,2216.0,2236.0,2180.0,2104.0,2058.0,2008.0,1967.0,1813.0,2026.0,2128.0,2168.0,2183.0,2161.0,2096.0,2052.0,2002.0,1964.0,1818.0,1912.0,2122.0,2200.0,2212.0,2180.0,2110.0
],[2284.0,2366.0,2385.0,2314.0,2240.0,2194.0,2146.0,2130.0,1954.0,2014.0,2240.0,2316.0,2353.0,2274.0,2213.0,2168.0,2121.0,2088.0,1928.0,2153.0,2229.0,2268.0,2315.0,2248.0,2184.0,2148.0,2100.0,2072.0,1908.0,1960.0,2197.0,2272.0,2316.0,2236.0,2170.0,2116.0,2072.0,1978.0,1881.0,1980.0,2208.0,2289.0,2314.0,2230.0,2144.0,2093.0,2040.0,2000.0,1850.0,1976.0,2074.0,2192.0,2292.0,2244.0,2176.0,2120.0,2057.0,2020.0,1848.0,1902.0,2126.0,2216.0,2236.0,2180.0,2104.0,2058.0,2008.0,1967.0,1813.0,2026.0,2128.0,2168.0,2183.0,2161.0,2096.0,2052.0,2002.0,1964.0,1818.0,1912.0,2122.0,2200.0,2212.0,2180.0,2110.0,2053.0,2013.0,1970.0,1822.0,1901.0,2117.0,2197.0,2204.0,2178.0,2099.0,2048.0,2000.0,1968.0,1814.0,1878.0
],[1844.0,2020.0,2238.0,2308.0,2240.0,2145.0,2074.0,2028.0,1980.0,1880.0,1760.0,1957.0,2060.0,2218.0,2227.0,2158.0,2086.0,2037.0,1979.0,1873.0,1776.0,1930.0,2152.0,2224.0,2170.0,2097.0,2036.0,1990.0,1971.0,1879.0,1759.0,2072.0,2151.0,2194.0,2158.0,2104.0,2056.0,1992.0,1994.0,1890.0,1782.0,1955.0,2174.0,2248.0,2204.0,2117.0,2062.0,1995.0,1981.0,1885.0,1787.0,1952.0,2173.0,2257.0,2196.0,2124.0,2060.0,1992.0,1999.0,1892.0,1792.0,1964.0,2188.0,2264.0,2208.0,2128.0,2060.0,1992.0,1989.0,1893.0,1778.0,1977.0,2084.0,2240.0,2248.0,2179.0,2113.0,2028.0,2023.0,1907.0,1798.0,2072.0,2152.0,2200.0,2154.0,2096.0,2046.0,1990.0,2002.0,1895.0,1794.0,1950.0,2168.0,2245.0,2188.0,2101.0,2049.0,1980.0,2004.0,1894.0
],[2158.0,2086.0,2037.0,1979.0,1873.0,1776.0,1930.0,2152.0,2224.0,2170.0,2097.0,2036.0,1990.0,1971.0,1879.0,1759.0,2072.0,2151.0,2194.0,2158.0,2104.0,2056.0,1992.0,1994.0,1890.0,1782.0,1955.0,2174.0,2248.0,2204.0,2117.0,2062.0,1995.0,1981.0,1885.0,1787.0,1952.0,2173.0,2257.0,2196.0,2124.0,2060.0,1992.0,1999.0,1892.0,1792.0,1964.0,2188.0,2264.0,2208.0,2128.0,2060.0,1992.0,1989.0,1893.0,1778.0,1977.0,2084.0,2240.0,2248.0,2179.0,2113.0,2028.0,2023.0,1907.0,1798.0,2072.0,2152.0,2200.0,2154.0,2096.0,2046.0,1990.0,2002.0,1895.0,1794.0,1950.0,2168.0,2245.0,2188.0,2101.0,2049.0,1980.0,2004.0,1894.0,1792.0,1947.0,2151.0,2236.0,2181.0,2106.0,2048.0,1983.0,2004.0,1896.0,1797.0,1944.0,2169.0,2250.0,2199.0
],[1759.0,2072.0,2151.0,2194.0,2158.0,2104.0,2056.0,1992.0,1994.0,1890.0,1782.0,1955.0,2174.0,2248.0,2204.0,2117.0,2062.0,1995.0,1981.0,1885.0,1787.0,1952.0,2173.0,2257.0,2196.0,2124.0,2060.0,1992.0,1999.0,1892.0,1792.0,1964.0,2188.0,2264.0,2208.0,2128.0,2060.0,1992.0,1989.0,1893.0,1778.0,1977.0,2084.0,2240.0,2248.0,2179.0,2113.0,2028.0,2023.0,1907.0,1798.0,2072.0,2152.0,2200.0,2154.0,2096.0,2046.0,1990.0,2002.0,1895.0,1794.0,1950.0,2168.0,2245.0,2188.0,2101.0,2049.0,1980.0,2004.0,1894.0,1792.0,1947.0,2151.0,2236.0,2181.0,2106.0,2048.0,1983.0,2004.0,1896.0,1797.0,1944.0,2169.0,2250.0,2199.0,2116.0,2065.0,1993.0,2011.0,1905.0,1807.0,1967.0,2186.0,2272.0,2201.0,2130.0,2071.0,1997.0,1989.0,1891.0
]])


test_data = np.reshape(test_data, (test_data.shape[0], 1, test_data.shape[1]))

result = model.predict(test_data)
print(result)

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