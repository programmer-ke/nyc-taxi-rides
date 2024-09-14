#!/usr/bin/env python
# coding: utf-8

import argparse
import subprocess
import time

import pandas as pd
from sqlalchemy import create_engine


parser = argparse.ArgumentParser(description="Ingest CSV data to postgresql")

parser.add_argument('user')
parser.add_argument('password')
parser.add_argument('host')
parser.add_argument('port')
parser.add_argument('db')
parser.add_argument('table_name')
parser.add_argument('url')
parser.add_argument('filename')


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    url = params.url
    filename = params.filename

    subprocess.run(['wget', url, '-O', filename])

    df = pd.read_csv(filename, nrows=100)
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)

    df.head(n=0).to_sql(name=table_name, con=engine, if_exists='replace')

    df_iter = pd.read_csv(filename, iterator=True, chunksize=100000)

    for df in df_iter:
        t_start = time.time()
        df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
        df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
        df.to_sql(name=table_name, con=engine, if_exists='append')
        t_end = time.time()
        print("insertion took %.3f seconds" % (t_end - t_start))


if __name__ == "__main__":
    params = parser.parse_args()
    main(params)
