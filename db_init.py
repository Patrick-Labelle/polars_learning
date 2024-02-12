import polars as pl
import sqlite3 as sql


nbsa = pl.read_csv("/data/nbsa.csv")
nbsa_meta = pl.read_csv("/data/nbsa_meta.csv")

print(nbsa.head(2))
print(nbsa_meta.head(2))

