import pandas as pd

# Load the ZIP-to-FIPS mapping file
zip_fips_df = pd.read_csv("ZIP to FIPS.csv")  

# Display the first few rows
print(zip_fips_df.head())


# Load the COVID-19 dataset (Make sure this dataset contains FIPS codes)
covid_df = pd.read_csv("covid-19-2023.csv")  

# Display the first few rows
print(covid_df.head())

covid_df.columns = covid_df.columns.str.upper()
zip_fips_df.columns = zip_fips_df.columns.str.upper()


# Merge COVID-19 data with ZIP-to-FIPS mapping based on FIPS code
covid_zip_df = covid_df.merge(zip_fips_df, on="FIPS", how="left")

# Display the merged dataset
print(covid_zip_df.head())

covid_zip_df = covid_zip_df.dropna(subset=["ZIP"])


# Check for missing ZIP codes
missing_zip = covid_zip_df[covid_zip_df["ZIP"].isna()]
print(missing_zip)



print("covid_df columns:", covid_df.columns)
print("zip_fips_df columns:", zip_fips_df.columns)





import pandas as pd

# Load the ZIP-to-DMA mapping file
zip_dma_df = pd.read_csv("ZipToDMA_Mapping.csv")  # Adjust filename as needed


zip_dma_df.rename(columns={"zip_code": "ZIP"}, inplace=True)

# Display the first few rows
print(zip_dma_df.head())


print("covid_zip_df columns:", covid_zip_df.columns)



# Merge COVID-19 data (which now has ZIP codes) with ZIP-to-DMA mapping
covid_dma_df = covid_zip_df.merge(zip_dma_df, on="ZIP", how="left")

# Display the merged dataset
print(covid_dma_df.head())


# Find missing DMA codes
missing_dma = covid_dma_df[covid_dma_df["dma_code"].isna()]
print(missing_dma)

covid_dma_df = covid_dma_df.dropna(subset=["dma_code"])



# Convert Date to a Month-Year format
covid_dma_df["DATE"] = pd.to_datetime(covid_dma_df["DATE"])
covid_dma_df["MONTH"] = covid_dma_df["DATE"].dt.to_period("M")


# Aggregate Cases and Deaths at DMA-Month level
dma_summary = covid_dma_df.groupby(["dma_code", "dma_description","COUNTY", "ZIP"])[["CASES", "DEATHS"]].sum().reset_index()

# Display the final summarized data
print(dma_summary.head())



dma_summary.sort_values(by="CASES", ascending=False).head(10)




covid_dma_df.to_csv("aggregated_dma_data.csv", index=False)

df_check = pd.read_csv("aggregated_dma_data.csv")
print(df_check.head())  # To verify the first few rows


covid_dma_df.to_csv("/Users/nikkibanda/Desktop/aggregated_dma_data.csv", index=False)



