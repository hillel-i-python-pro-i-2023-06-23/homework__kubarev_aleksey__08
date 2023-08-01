import pandas as pd


def read_google_sheets_pd_data(url):
    df = pd.read_csv(url)
    return df


def get_average_value(column_name, df):
    return df[column_name].mean()


def convert_inches_in_cm(inches):
    return inches * 2.54


def convert_pounds_in_kg(pounds):
    return pounds * 0.45359237


def print_info(df):
    height_mean = get_average_value("Height(Inches)", df)
    weight_mean = get_average_value("Weight(Pounds)", df)

    avg_height_cm = convert_inches_in_cm(height_mean)
    avg_weight_kg = convert_pounds_in_kg(weight_mean)

    return avg_weight_kg, avg_height_cm


def get_string_info(df):
    height_mean = get_average_value("Height(Inches)", df)
    weight_mean = get_average_value("Weight(Pounds)", df)

    avg_height_cm = convert_inches_in_cm(height_mean)
    avg_weight_kg = convert_pounds_in_kg(weight_mean)

    return f"Average height is {avg_height_cm:.2f} cm and average weight is {avg_weight_kg:.2f} kg"
