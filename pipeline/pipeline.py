import sys
import pandas as pd



month = sys.argv[1] if len(sys.argv) > 1 else "NaN"
df = pd.DataFrame({
    "day": [1, 2, 3],
    "num_passengers": [100, 150, 200]
})

df["month"] = month

print(df.head())


df.to_parquet(f"passengers_{month}.parquet", index=False)

#print(f"Command line arguments: {sys.argv}")
#print(f"Month argument: {month}")

