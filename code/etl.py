import pandas as pd
import streamlit as st 


def top_locations(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    return pd.DataFrame()  # TODO implement this function


def top_locations_mappable(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    return pd.DataFrame()  # TODO implement this function


def tickets_in_top_locations(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    return pd.DataFrame()  # TODO implement this function

if __name__ == '__main__':
    '''
    Main ETL job. 
    '''
    pass # TODO implement this script

df = pd.read_csv('./cache/final_cuse_parking_violations.csv')

def top_locations(violations_df, threshold=1000):
    grouped = violations_df.groupby("location")["amount"].sum().reset_index()
    return grouped[grouped["amount"] >= threshold]

def top_locations_mappable(violations_df, threshold=1000):
    top_locs = top_locations(violations_df, threshold)
    merged = violations_df.merge(top_locs, on="location")[["location", "lat", "lon", "amount"]]
    return merged.drop_duplicates(subset="location")

def tickets_in_top_locations(violations_df, threshold=1000):
    top_locs = top_locations(violations_df, threshold)
    return violations_df[violations_df["location"].isin(top_locs["location"])]
