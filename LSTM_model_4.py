from keras.utils import *
import tensorflow as tf
import numpy as np
from keras.models import model_from_json
import Data_load_4 as dl

#modelname = input("Type Model's name :: ")
#modelname = "Model4_lstm_drop_adam_ep1000"
#modelname = "Model4_I3d3_ep500_case3"
#modelname = "Model4_ep1500_cutdatafor2_lr0002"
modelname = "Model4_ep1500_lr0005_1drop"
modelname_json = "Models/" + modelname + ".json"
modelname_weight = "Models/" + modelname + ".h5"

json_file = open(modelname_json,"r")

loaded_model_json = json_file.read()
json_file.close()

model = tf.keras.models.model_from_json(loaded_model_json)
model.load_weights(modelname_weight)

print("Model Loaded...!")

def decision(predict):
    print(predict)
    if predict[0][0] > predict[0][1]:
        return "None"
    else:
        return "Exist"

#human [0,0,1]
data = np.array([[
2476.0,2408.0,2298.0,2146.0,2072.0,2132.0,2134.0,2182.0,2088.0,2125.0,2102.0,2024.0,1912.0,1760.0,1692.0,1760.0,1806.0,1872.0,1828.0,1868.0,1840.0,1782.0,1680.0,1544.0,1472.0,1529.0,1598.0,1576.0,1521.0,1724.0,1868.0,1787.0,1809.0,1736.0,1641.0,1688.0,1696.0,1712.0,1620.0,1614.0,1550.0,1465.0,1337.0,1192.0,1113.0,1144.0,1214.0,1307.0,1264.0,1312.0,1296.0,1232.0,1129.0,1000.0,937.0,1034.0,1092.0,1184.0,1129.0,1194.0,1195.0,1161.0,1080.0,972.0,934.0,1044.0,1124.0,1197.0,1200.0,1256.0,1245.0,1202.0,1112.0,1006.0,961.0,1076.0,1164.0,1253.0,1256.0,1241.0,1216.0,1298.0,1379.0,1392.0,1317.0,1539.0,1746.0,1704.0,1528.0,1433.0,1276.0,1101.0,896.0,740.0,650.0,707.0,728.0,761.0,717.0,791.0
],[3980.0,3980.0,3976.0,3980.0,3976.0,3980.0,3980.0,3980.0,3983.0,3984.0,3984.0,3986.0,3984.0,3984.0,3984.0,3980.0,3980.0,3980.0,3980.0,3992.0,3984.0,3984.0,3976.0,3980.0,3980.0,3983.0,3980.0,3984.0,3980.0,3987.0,3980.0,3984.0,3984.0,3984.0,3991.0,3980.0,3980.0,3984.0,3976.0,3984.0,3980.0,3984.0,3980.0,3976.0,3983.0,3980.0,3980.0,3984.0,3980.0,3984.0,3984.0,3980.0,3980.0,3980.0,3984.0,3984.0,3988.0,3986.0,3987.0,3989.0,3986.0,3984.0,3984.0,3985.0,3986.0,3986.0,3990.0,3986.0,3984.0,3985.0,3987.0,3984.0,3985.0,3986.0,3985.0,3991.0,3985.0,3984.0,3984.0,3988.0,3986.0,3986.0,3988.0,3976.0,3984.0,3986.0,3990.0,3984.0,3989.0,3985.0,3992.0,3976.0,3984.0,3986.0,3984.0,3984.0,3985.0,3987.0,3986.0,3985.0
],[25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0
],[31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0
]])

#human [0,1]
data2 = np.array([[
1992.0,1930.0,1945.0,2100.0,2152.0,2096.0,2028.0,2062.0,2041.0,2112.0,2076.0,2054.0,2068.0,2234.0,2284.0,2240.0,2188.0,2208.0,2192.0,2250.0,2214.0,2168.0,2193.0,2304.0,2402.0,2356.0,2280.0,2288.0,2210.0,2298.0,2264.0,2168.0,2304.0,2642.0,2781.0,2724.0,2592.0,2520.0,2408.0,2384.0,2290.0,2180.0,2176.0,2252.0,2265.0,2182.0,2094.0,2104.0,2070.0,2120.0,2080.0,2042.0,2089.0,2217.0,2237.0,2156.0,2082.0,2068.0,2012.0,2096.0,2100.0,2076.0,2130.0,2234.0,2232.0,2140.0,2036.0,2042.0,1993.0,2024.0,1984.0,1948.0,2020.0,2124.0,2123.0,2036.0,1930.0,1926.0,1873.0,1883.0,1794.0,1776.0,1831.0,1972.0,2010.0,1924.0,1804.0,1736.0,1048.0,263.0,14.0,13.0,177.0,471.0,452.0,562.0,367.0,569.0,418.0,549.0
],[4064.0,4064.0,4075.0,4060.0,4068.0,4064.0,4064.0,4064.0,4064.0,4064.0,4064.0,4064.0,4064.0,4064.0,4064.0,4064.0,4064.0,4060.0,4064.0,4064.0,4064.0,4064.0,4067.0,4064.0,4067.0,4064.0,4064.0,4064.0,4064.0,4064.0,4064.0,4064.0,4060.0,4064.0,4064.0,4064.0,4064.0,4064.0,4064.0,4064.0,4067.0,4070.0,4060.0,4068.0,4066.0,4064.0,4064.0,4064.0,4064.0,4064.0,4064.0,4064.0,4064.0,4064.0,4064.0,4064.0,4064.0,4064.0,4064.0,4064.0,4064.0,4064.0,4056.0,4064.0,4064.0,4068.0,4064.0,4060.0,4064.0,4071.0,4064.0,4064.0,4056.0,4064.0,4064.0,4064.0,4064.0,4067.0,4064.0,4064.0,4064.0,4064.0,4064.0,4064.0,4064.0,4066.0,4064.0,4064.0,4064.0,4064.0,4065.0,4064.0,4060.0,4064.0,4064.0,4064.0,4064.0,4067.0,4060.0,4064.0
],[31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0
],[31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0
]])

#none [1,0]
data3 = np.array([[
2504.0,2660.0,2870.0,2944.0,2944.0,3056.0,3059.0,3076.0,3056.0,2996.0,3048.0,2968.0,3064.0,3072.0,3077.0,3072.0,3081.0,3076.0,3074.0,3064.0,3067.0,3072.0,3072.0,3079.0,3080.0,3078.0,3081.0,3080.0,3076.0,3054.0,3056.0,3074.0,3078.0,3072.0,3075.0,3082.0,3079.0,3080.0,3036.0,2976.0,2912.0,2952.0,3058.0,3042.0,3083.0,3039.0,2960.0,2849.0,2721.0,2557.0,2503.0,2561.0,2605.0,2570.0,2621.0,2608.0,2552.0,2478.0,2356.0,2272.0,2248.0,2297.0,2365.0,2309.0,2355.0,2343.0,2291.0,2223.0,2129.0,2039.0,2048.0,2060.0,2134.0,2110.0,2163.0,2164.0,2100.0,2016.0,1908.0,1815.0,1830.0,1890.0,1962.0,1898.0,1950.0,1958.0,1916.0,1854.0,1755.0,1685.0,1760.0,1774.0,1833.0,1780.0,1836.0,1843.0,1811.0,1746.0,1666.0,1632.0
],[4002.0,4006.0,4000.0,4003.0,4004.0,4001.0,4002.0,4003.0,4000.0,4003.0,4007.0,4004.0,4000.0,4002.0,4001.0,4002.0,4004.0,4000.0,4002.0,4003.0,4008.0,4005.0,4008.0,4004.0,4004.0,4009.0,4004.0,4000.0,4003.0,4002.0,4001.0,4007.0,4001.0,4002.0,4002.0,4006.0,4004.0,4004.0,4004.0,4002.0,4004.0,4011.0,4003.0,4016.0,4004.0,4004.0,4006.0,4004.0,4000.0,4003.0,4001.0,4002.0,4000.0,4004.0,4003.0,4005.0,4004.0,3996.0,4005.0,4000.0,4004.0,4012.0,4007.0,4004.0,4000.0,4004.0,4002.0,4004.0,4004.0,4005.0,4002.0,4006.0,4001.0,4003.0,4003.0,4003.0,4003.0,4004.0,4003.0,4002.0,4000.0,4002.0,4004.0,4007.0,4003.0,4004.0,4006.0,4003.0,4007.0,4002.0,4000.0,4002.0,4004.0,4007.0,4008.0,4016.0,4008.0,4008.0,4004.0,4000.0
],[31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0
],[31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0
]])

#none [1,0]
data4 = np.array([[
1662.0,1569.0,1562.0,1688.0,1865.0,1933.0,1928.0,1948.0,1912.0,1959.0,1899.0,1818.0,1832.0,1980.0,2104.0,2121.0,2072.0,2076.0,2038.0,2104.0,2051.0,1982.0,1991.0,2162.0,2228.0,2176.0,2122.0,2140.0,2110.0,2180.0,2128.0,2065.0,2083.0,2259.0,2321.0,2258.0,2209.0,2248.0,2196.0,2260.0,2215.0,2186.0,2198.0,2360.0,2410.0,2329.0,2279.0,2294.0,2252.0,2320.0,2275.0,2248.0,2254.0,2410.0,2480.0,2417.0,2360.0,2362.0,2321.0,2368.0,2340.0,2283.0,2314.0,2441.0,2541.0,2488.0,2410.0,2416.0,2348.0,2382.0,2334.0,2268.0,2296.0,2432.0,2464.0,2370.0,2296.0,2295.0,2242.0,2286.0,2240.0,2194.0,2262.0,2404.0,2432.0,2353.0,2278.0,2288.0,2236.0,2270.0,2232.0,2183.0,2269.0,2402.0,2432.0,2336.0,2264.0,2254.0,2233.0,2250.0
],[4054.0,4056.0,4056.0,4052.0,4052.0,4054.0,4052.0,4048.0,4051.0,4052.0,4056.0,4054.0,4052.0,4058.0,4054.0,4051.0,4052.0,4048.0,4052.0,4056.0,4056.0,4060.0,4052.0,4052.0,4056.0,4052.0,4056.0,4054.0,4056.0,4052.0,4053.0,4056.0,4056.0,4056.0,4052.0,4052.0,4052.0,4048.0,4052.0,4056.0,4056.0,4052.0,4052.0,4056.0,4056.0,4054.0,4052.0,4054.0,4052.0,4056.0,4055.0,4056.0,4056.0,4056.0,4056.0,4052.0,4052.0,4052.0,4052.0,4056.0,4054.0,4056.0,4050.0,4052.0,4056.0,4056.0,4052.0,4056.0,4052.0,4056.0,4054.0,4049.0,4052.0,4056.0,4056.0,4052.0,4052.0,4049.0,4052.0,4056.0,4057.0,4052.0,4050.0,4056.0,4056.0,4052.0,4054.0,4056.0,4050.0,4052.0,4052.0,4056.0,4048.0,4054.0,4054.0,4052.0,4048.0,4051.0,4052.0,4056.0
],[33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0,33.0
],[31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0
]])

#human [0,1]
data5 = np.array([[
1865.0,1752.0,1824.0,1904.0,2089.0,2149.0,2124.0,2046.0,1950.0,1853.0,1717.0,1604.0,1726.0,1814.0,2004.0,2121.0,2137.0,2099.0,2024.0,1947.0,1809.0,1725.0,1835.0,1921.0,2109.0,2180.0,2176.0,2142.0,2088.0,2024.0,1904.0,1872.0,2028.0,2118.0,2304.0,2361.0,2330.0,2264.0,2171.0,2074.0,1911.0,1874.0,2040.0,2106.0,2273.0,2317.0,2278.0,2208.0,2113.0,2007.0,1862.0,1696.0,1853.0,2168.0,2548.0,2746.0,2816.0,2810.0,2760.0,2644.0,2464.0,2488.0,2624.0,2520.0,2502.0,2364.0,2136.0,1904.0,1662.0,1416.0,1218.0,1123.0,1254.0,1270.0,1392.0,1412.0,1376.0,1313.0,1246.0,1120.0,1024.0,1017.0,1231.0,1299.0,1467.0,1542.0,1536.0,1492.0,1441.0,1337.0,1268.0,1272.0,1484.0,1553.0,1717.0,1788.0,1773.0,1724.0,1664.0,1572.0
],[2500.0,2499.0,2490.0,2476.0,2467.0,2463.0,2466.0,2468.0,2469.0,2476.0,2500.0,2496.0,2492.0,2484.0,2469.0,2464.0,2466.0,2467.0,2469.0,2480.0,2500.0,2496.0,2495.0,2472.0,2467.0,2465.0,2467.0,2467.0,2467.0,2476.0,2500.0,2496.0,2490.0,2469.0,2466.0,2465.0,2467.0,2470.0,2464.0,2479.0,2484.0,2497.0,2491.0,2467.0,2465.0,2468.0,2464.0,2466.0,2464.0,2476.0,2506.0,2484.0,2530.0,2482.0,2481.0,2482.0,2480.0,2480.0,2480.0,2492.0,2490.0,2469.0,2490.0,2470.0,2469.0,2467.0,2461.0,2468.0,2476.0,2472.0,2488.0,2480.0,2491.0,2471.0,2468.0,2466.0,2460.0,2465.0,2479.0,2472.0,2499.0,2476.0,2490.0,2468.0,2466.0,2464.0,2464.0,2472.0,2470.0,2474.0,2499.0,2483.0,2496.0,2470.0,2464.0,2467.0,2464.0,2466.0,2472.0,2480.0
],[25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0,25.0
],[31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0,31.0
]])

data = np.reshape(data, (int(data.__len__()/4), 4, 100))
data2 = np.reshape(data2, (int(data2.__len__()/4), 4, 100))
data3 = np.reshape(data3, (int(data3.__len__()/4), 4, 100))
data4 = np.reshape(data4, (int(data4.__len__()/4), 4, 100))
data5 = np.reshape(data5, (int(data5.__len__()/4), 4, 100))

result = decision(model.predict(data))
print(result)
result2 = decision(model.predict(data2))
print(result2)
result3 = decision(model.predict(data3))
print(result3)
result4 = decision(model.predict(data4))
print(result4)
result5 = decision(model.predict(data5))
print(result5)