import pandas as pd
import os
from datetime import datetime, timedelta

# 📁 Volledig pad naar je Excel-bestand
excel_path = r"C:\Users\My PC\Documents\Dashboard_Klimatologie\data\Rainfall_Data_Suriname_2025.xlsx"

# 📁 Output CSV in de data folder
csv_output_path = r"C:\Users\My PC\Documents\Dashboard_Klimatologie\data\tijdreeks-neerslag-data.csv"

# 📅 Bereken cutoff datum
cutoff_date = datetime.today() - timedelta(days=10)

try:
    if not os.path.exists(excel_path):
        raise FileNotFoundError(f"Excel-bestand niet gevonden: {excel_path}")

    xls = pd.ExcelFile(excel_path)
    all_data = []

    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)

        required_columns = ["Date", "StationID", "Rainfall (mm)", "Rainfall Category"]
        missing = [col for col in required_columns if col not in df.columns]
        if missing:
            print(f"⚠️ Sheet '{sheet_name}' mist kolommen: {missing}")
            continue

        df = df[required_columns]
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df = df[df["Date"] >= cutoff_date]

        # Vul lege waarden op met ⛔ geen data
        for col in required_columns:
            df[col] = df[col].fillna("⛔ geen data")

        df["Sheet"] = sheet_name  # optioneel
        all_data.append(df)

    if not all_data:
        print("⚠️ Geen geldige data gevonden in de laatste 10 dagen.")
    else:
        final_df = pd.concat(all_data, ignore_index=True)
        os.makedirs(os.path.dirname(csv_output_path), exist_ok=True)
        final_df.to_csv(csv_output_path, index=False, encoding="utf-8")
        print(f"✅ CSV succesvol gegenereerd in data folder:\n{csv_output_path}")

except Exception as e:
    print(f"❌ Fout bij uitvoeren script: {e}")