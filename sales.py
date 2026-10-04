import pandas as pd

data = {
    "Rep":    ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"],
    "Region": ["North", "South", "North",  "East",  "South", "East"],
    "Sales":  [87000,   64000,  92000,    78000,   55000,   101000],
    "Quota":  [81000,   70000,  85000,    80000,   60000,   95000]
}

df = pd.DataFrame(data)
df["Achievement"] = (df["Sales"] / df["Quota"] * 100).round(1)

print(f"Total reps: {len(df)}")
print(f"Total sales: ${df['Sales'].sum():,}")
print(f"Average sales: ${df['Sales'].mean():,.0f}")
print(f"Top performer: {df.loc[df['Sales'].idxmax(), 'Rep']}")

met_quota = df[df["Sales"] >= df["Quota"]]
print("Reps who met quota:")
for _, row in met_quota.iterrows():
    print(f"  {row['Rep']}: {row['Achievement']}%")
print(f"Quota attainment rate: {len(met_quota)}/6")

regional = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
print("Regional Sales Totals:")
for region, total in regional.items():
    print(f"  {region}: ${total:,}")

top_idx = df.groupby("Region")["Sales"].idxmax()
top_per_region = df.loc[top_idx].sort_values("Region")
print("Top performer per region:")
for _, row in top_per_region.iterrows():
    print(f"  {row['Region']}: {row['Rep']} (${row['Sales']:,})")