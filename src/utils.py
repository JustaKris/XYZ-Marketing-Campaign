import os


def save_dataframe(df, filename="file.csv", directory="../data", sep=",", index=False):
    """
    Saves a Pandas dataframe to a CSV file.

    Parameters:
    df (pd.DataFrame): Dataset to save.
    filename (str): The name of the output CSV file (default: 'file.csv').
    directory (str): The folder where the file should be saved (default: '../data').
    sep (str): The separator for the CSV file (default: ',').
    index (bool): Whether to include the index in the saved file (default: False).
    
    Returns:
    None
    """
    try:
        # Ensure the directory exists
        os.makedirs(directory, exist_ok=True)

        # Full file path
        filepath = os.path.join(directory, filename)

        # Save DataFrame
        df.to_csv(filepath, sep=sep, index=index)
        print(f"✅ Data successfully saved to {filepath} with separator '{sep}'")
    
    except Exception as e:
        print(f"❌ Error saving file: {e}")

