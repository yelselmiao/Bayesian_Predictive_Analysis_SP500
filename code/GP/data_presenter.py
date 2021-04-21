import os
import data_fig

companies = []
plotters = {}
start_year = 2015


def main():
    __init_data()
    for company in companies:
        make_summary(company)
    print("Done!")


def make_summary(company_name):
    plotter = plotters[company_name]

    # general plot of prices
    plotter.show_whole_time_series()
    # time series plot of an interval
    ##plotter.show_time_series(start_year=start_year, end_year=2020)
    # normalized price change of each year in one plot
    ##plotter.show_preprocessed_prices(start_year=start_year, end_year=2020)
    # predict the price in one time interval
    plotter.show_gp_prediction(train_start=start_year, train_end=2018, pred_year=2019)
    plotter.show_gp_prediction(train_start=start_year, train_end=2019, pred_year=2020)
    ##plotter.show_gp_prediction(train_start=start_year, train_end=2019, pred_year=2020)
    # time series plot of an interval
    ## plotter.show_time_series(start_year=start_year, end_year=2021)
    # predict the specific quarters in one year
    ## plotter.show_gp_prediction(train_start=start_year, train_end=2017, pred_year=2021, pred_quarters=[2, 3])
    ## plotter.show_gp_prediction(train_start=start_year, train_end=2018, pred_year=2021, pred_quarters=[2, 3])
    ## plotter.show_gp_prediction(train_start=start_year, train_end=2020, pred_year=2021, pred_quarters=[1, 2])
    print(company_name + ' summary done!')


def __init_data():
    for company in os.listdir('H:/Project/520A/GPSP500/Data'):
        current_company = company.split('.')[0]
        companies.append(current_company)
        plotters[current_company] = (data_fig.Plotter(company_name=current_company))


if __name__ == "__main__":
    main()