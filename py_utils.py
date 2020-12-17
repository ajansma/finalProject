import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_data(filename):
    return pd.read_csv(filename)

def load_weather(data_object):
    weather_df = pd.DataFrame()
    tavg_ser = pd.Series(dtype=float)
    prec_ser = pd.Series(dtype=float)

    # load in the data 
    for date_object in data_object:
        date = date_object["date"]
        tavg = date_object["tavg"] * (9 / 5) + 32 #convert to F
        prec = date_object["prcp"]
        snow = date_object["snow"]
        daily_prec = float(prec) + float(snow)
        tavg_ser[date] = tavg
        prec_ser[date] = daily_prec

    # put the data into the dataframe
    weather_df["tavg"] = tavg_ser
    weather_df["prec"] = prec_ser
    weather_df["Date"] = prec_ser.index
    weather_df.set_index("Date", inplace = True)
    return weather_df

def graph_bar(merged_netflix_weather_df):
    prec = merged_netflix_weather_df["prec"]
    time = merged_netflix_weather_df["Viewing Time"]
    prec_ser = pd.Series(dtype=float)
    no_prec_ser = pd.Series(dtype=float)
    for i in range(len(merged_netflix_weather_df["prec"])):
        if prec[i] == 1.0:
            prec_ser = prec_ser.append(pd.Series(time[i]))
        elif prec[i] == 0.0:
            no_prec_ser = no_prec_ser.append(pd.Series(time[i]))
    plt.bar(0,no_prec_ser.mean())
    plt.bar(1, prec_ser.mean())
    plt.xticks((0, 1), ('Prec', 'No Prec'))
    plt.ylabel("Mean Minutes Watched")
    plt.title("Viewing Time With Precipitation")
    plt.show()
    return prec_ser, no_prec_ser

def scatter_plot(merged_netflix_weather_df):
    plt.title("Viewing Time vs. Temperature")
    plt.scatter(merged_netflix_weather_df["tavg"], merged_netflix_weather_df["Viewing Time"], s=20)
    plt.xlabel("Temperature (F)")
    plt.ylabel("Minutes watched")
    plt.show()
    
def confidence_interval_graph(conf_interval_low_temp, Xbar_low, conf_interval_high_temp, Xbar_high):
    ## graph them
    plt.figure()
    plt.title("Low and High Temp Watching Confidence Intervals")

    plt.plot([.8, .8], conf_interval_low_temp, marker="_", color="blue")
    plt.plot([.8], [Xbar_low], marker="o", color="blue", label="Low Temp Viewing Time Mean")

    plt.plot([1.2, 1.2], conf_interval_high_temp, marker="_", color="red")
    plt.plot([1.2], [Xbar_high], marker="o", color="red", label="High Temp Viewing Time Mean")

    #set x and y limits
    plt.ylim([10, 30])
    plt.xlim([0.5, 1.5])
    plt.legend(loc='upper right')
    plt.show()
    
def clean_dates():
    dates_no_repeats = pd.Series(dtype=int)
    for i in range (8, 11):
        for j in range(1,32):
            if i == 8 and j >= 29:
                date_str = "2020-0" + str(i) + "-" + str(j)
                dates_no_repeats = dates_no_repeats.append(pd.Series(date_str))
            elif i == 9:
                if j < 31: 
                    if j < 10:
                        date_str = "2020-0" + str(i) + "-0" + str(j)
                    else: 
                        date_str = "2020-0" + str(i) + "-" + str(j)
                    dates_no_repeats = dates_no_repeats.append(pd.Series(date_str))
            elif i == 10:
                if j < 31: 
                    if j < 10:
                        date_str = "2020-" + str(i) + "-0" + str(j)
                    else: 
                        date_str = "2020-" + str(i) + "-" + str(j)
                    dates_no_repeats = dates_no_repeats.append(pd.Series(date_str))
    return dates_no_repeats