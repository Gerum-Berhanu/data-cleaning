import kagglehub
import os
import shutil
import pandas as pd
import argparse

def download_datasets(datasets, quick_check=False):
    """
    Downloads multiple datasets from Kaggle.
    :param datasets: List of dictionaries with keys: 'link' (Kaggle handle) and 'target_folder'.
    """
    base_dir = "./projects"
    
    for dataset in datasets:
        link = dataset['link']
        target_folder = dataset['target_folder']
        
        target_dir = os.path.join(base_dir, target_folder, "data").replace("\\", "/")
        target_file = os.path.join(target_dir, "raw.csv").replace("\\", "/")
        
        print(f"Targeting file: {target_file}")

        # Check if the file already exists locally
        if os.path.exists(target_file):
            print(f"Dataset already exists at {target_file}. Skipping download...")
        else:
            print(f"Dataset not found locally. Starting download for {link}...")
            
            # Download to the default cache
            cache_path = kagglehub.dataset_download(link)

            # Create the directory if it doesn't exist
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

            # Locate the downloaded file and move it
            if os.path.isdir(cache_path): # if what kaggle returns is the directory path
                # Auto-detect the first CSV file in the directory
                csv_files = [f for f in os.listdir(cache_path) if f.endswith('.csv')]
                if csv_files:
                    downloaded_file = os.path.join(cache_path, csv_files[0])
                else:
                    downloaded_file = None
            else: # if what kaggle returns is the file path
                downloaded_file = cache_path

            if downloaded_file and os.path.exists(downloaded_file):
                shutil.move(downloaded_file, target_file)
                print(f"File successfully moved to: {target_file}")
            else:
                print(f"Could not find any .csv file in the downloaded cache from {cache_path}.")

        # Quick check after possible download
        if quick_check:
            if os.path.exists(target_file):
                df = pd.read_csv(target_file)
                print(f"\nQuick check for {target_folder} (raw.csv) - First 5 rows:")
                print(df.head())
            else:
                print(f"\nError: Could not load data because the file {target_file} is missing.")
        print("-" * 50)

def main():
    parser = argparse.ArgumentParser(description="Download Kaggle datasets for portfolio projects.")
    parser.add_argument("--check", action="store_true", help="Print the first 5 rows of each dataset after downloading/checking.")
    args = parser.parse_args()

    datasets_to_download = [
        {
            "link": "ahmedmohamed2003/cafe-sales-dirty-data-for-cleaning-training",
            "target_folder": "01_cafe_sales"
        },
        {
            "link": "desolution01/messy-employee-dataset",
            "target_folder": "03_employee_metrics"
        },
        {
            "link": "yagunnersya/fifa-21-messy-raw-dataset-for-cleaning-exploring",
            "target_folder": "04_fifa_21"
        },
    ]
    
    download_datasets(datasets_to_download, quick_check=args.check)

if __name__ == "__main__":
    main()