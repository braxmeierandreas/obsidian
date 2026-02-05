import pandas as pd
import pyreadstat

try:
    df, meta = pyreadstat.read_sav('GEDA19.sav')
    print(f"Number of rows: {len(df)}")
    print(f"Number of columns: {len(df.columns)}")
    print("\nVariable Labels (First 20):")
    for col in list(df.columns)[:20]:
        print(f"{col}: {meta.column_names_to_labels.get(col, 'No Label')}")
    
    # Save a full list of variables to a text file for further planning
    with open('variables_list.txt', 'w', encoding='utf-8') as f:
        for col in df.columns:
            label = meta.column_names_to_labels.get(col, 'No Label')
            f.write(f"{col}: {label}\n")
            
except Exception as e:
    print(f"Error reading file: {e}")
