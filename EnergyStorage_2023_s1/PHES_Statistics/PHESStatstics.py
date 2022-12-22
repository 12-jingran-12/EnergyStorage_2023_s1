import os
import warnings
import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)


def get_sheet_names(path):
    xlsx = pd.ExcelFile(path)
    sheet_names = xlsx.sheet_names
    return sheet_names


def from_sheet_to_csv(path, sheet_name):
    df = pd.read_excel(path, sheet_name)
    filename = path[2:].split("_")[0]
    df = sheet_process(df)
    df.to_csv(path_or_buf="./" + filename + "_" + sheet_name + ".csv", header=True, index=False)


def sheet_process(df):
    df = df[15:]
    del df["Unnamed: 9"]
    del df["Unnamed: 20"]
    del df["Unnamed: 31"]
    del df["Unnamed: 34"]
    # del df[["Unnamed: 9", "Unnamed: 20", "Unnamed: 31", "Unnamed: 34"]]
    print(df.head())
    df.columns = ["Pair Identifier", "Class", "Head (m)", "Separation (km)",
                  "Slope (%)", "Volume (GL)", "Energy (GWh)", "Storage time (h)",
                  "Combined water to rock ratio", "Upper Identifier", "Upper elevation (m)", "Upper latitude",
                  "Upper longitude", "Upper reservoir area (ha)", "Upper reservoir volume (GL)", "Upper dam height (m)",
                  "Upper dam length (m)", "Upper dam volume (GL)", "Upper water to rock ratio", "Lower Identifier",
                  "Lower elevation (m)", "Lower latitude", "Lower longitude", "Lower reservoir area (ha)",
                  "Lower reservoir volume (GL)", "Lower dam height (m)", "Lower dam length (m)",
                  "Lower dam volume (GL)",
                  "Lower water to rock ratio", "Combined water area (ha)", "Energy storage MWh per ha"]
    # df.replace('', np.nan, inplace=True)
    # df.dropna(inplace=True)
    return df


def average_water_to_rock(country):
    files = os.listdir("./")
    means = []
    lens = []
    for f in files:
        if f.startswith(country) and f.endswith(".csv"):
            read_df = pd.read_csv(filepath_or_buffer="./" + f, header=0)
            df1 = read_df[["Upper Identifier", "Upper water to rock ratio"]]
            df1.drop_duplicates(keep="first", inplace=True)
            s1 = df1["Upper water to rock ratio"]
            s1.replace(["", " "], np.nan, inplace=True)
            s1.dropna(inplace=True)
            s1 = s1.astype(np.float64)
            m1 = s1.mean()
            if m1 != np.inf:
                means.append(s1.mean() * len(s1))
                lens.append(len(s1))

            df2 = read_df[["Lower Identifier", "Lower water to rock ratio"]]
            df2.drop_duplicates(keep="first", inplace=True)
            s2 = df1["Upper water to rock ratio"]
            s2.replace(["", " "], np.nan, inplace=True)
            s2.dropna(inplace=True)
            s2 = s2.astype(np.float64)
            m2 = s2.mean()
            if m2 != np.inf:
                means.append(s2.mean() * len(s2))
                lens.append(len(s2))

    means = np.array(means)
    return (means / np.sum(lens)).sum()


if __name__ == '__main__':
    """
    finished
    """
    path = "./Australia_162.8.xlsx"
    sheet_names = get_sheet_names(path)
    sheet_names.pop(0)
    for i in sheet_names:
        from_sheet_to_csv(path, i)
    print(average_water_to_rock("Australia"))  # 18.4828088151582
