# Import the necesaary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("pageviews.csv")
df = df.set_index("date")


def draw_line_plot():
    df = df[df["value"].between(df["value"].quantile(0.025), df["value"].quantile(0.975))]
    plt.figure(figsize=(15,10))
    plt.plot(df.index, df["value"])
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Dates")
    plt.ylabel("Pageviews")
    plt.show()


#Bar plot functions
def draw_bar_plot():
    df_bar = df.reset_index()
    # convert the date colum to datetime format
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    plt.figure(figsize=(15,10))
    df_bar["date"] = pd.to_datetime(df_bar["date"])    
    df_bar["month"] = df_bar["date"].dt.month
    df_bar["year"] = df_bar["date"].dt.year
    
    sns.barplot(data = df_bar, x="year", y="value",hue="month",hue_order=months, ci=None)
    plt.title("Average Daily Pageview Monthly and Yearly")
    plt.ylabel("Average Pageviews")
    plt.xlabel("Years")
    plt.legend(months)
    plt.show()

#Function for boxplot
def draw_box_plot():
    df_boxplot = df.reset_index()
    # convert the date colum to datetime format
    
    df_boxplot["date"] = pd.to_datetime(df_boxplot["date"])    
    df_boxplot["month"] = df_boxplot["date"].dt.month
    df_boxplot["year"] = df_boxplot["date"].dt.year 
    
    #Draw the boxplot
    fig, ax = plt.subplots(1,2, figsize=(16,6))
    sns.boxplot(y="value",x="year",data=df_boxplot, ax=ax[0],log_scale=True)
    ax[0].set(xlabel="Year", ylabel="Pageviews", title="Year-wise Box Plot (Trend)")
    
    
    sns.boxplot(y="value",x="month",data=df_boxplot, ax=ax[1], log_scale=True)
    ax[1].set(xlabel="Month", ylabel="Pageviews", title="Month-wise Box Plot (Seasonality)")
    
    plt.show()
