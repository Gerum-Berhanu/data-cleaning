import kagglehub
import os
import shutil
import pandas as pd

def download_datasets(datasets):
    """
    Downloads multiple datasets from Kaggle.
    :param datasets: List of dictionaries with keys: 'link' (Kaggle handle), 'filename', and 'target_folder'.
    """
    base_dir = "./datasets"
    notebooks_base_dir = "./notebooks"
    
    for dataset in datasets:
        link = dataset['link']
        filename = dataset['filename']
        target_folder = dataset['target_folder']
        
        target_dir = os.path.join(base_dir, target_folder)
        target_file = os.path.join(target_dir, filename)
        
        # Create corresponding notebooks directory
        notebooks_dir = os.path.join(notebooks_base_dir, target_folder)
        if not os.path.exists(notebooks_dir):
            os.makedirs(notebooks_dir)
            print(f"Created corresponding notebook directory at {notebooks_dir}")

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
            if os.path.isdir(cache_path):
                downloaded_file = os.path.join(cache_path, filename)
            else:
                downloaded_file = cache_path

            if os.path.exists(downloaded_file):
                shutil.move(downloaded_file, target_file)
                print(f"File successfully moved to: {target_file}")
            else:
                print(f"Could not find {filename} in the downloaded cache from {cache_path}.")

        # Quick check after possible download
        if os.path.exists(target_file):
            df = pd.read_csv(target_file)
            print(f"\nQuick check for {filename} - First 5 rows:")
            print(df.head())
        else:
            print(f"\nError: Could not load data because the file {target_file} is missing.")
        print("-" * 50)

def main():
    datasets_to_download = [
        {
            "link": "ahmedmohamed2003/cafe-sales-dirty-data-for-cleaning-training",
            "filename": "dirty_cafe_sales.csv",
            "target_folder": "dirty_cafe_sales"
        },
        {
            "link": "desolution01/messy-employee-dataset",
            "filename": "Messy_Employee_dataset.csv",
            "target_folder": "messy_employee_dataset"
        },
    ]
    
    download_datasets(datasets_to_download)

if __name__ == "__main__":
    main()