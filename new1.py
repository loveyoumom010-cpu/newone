# %%
# 4. Unzip the training archive
train_root = '/kaggle/working/train_data'
os.makedirs(train_root, exist_ok=True)
with zipfile.ZipFile(f"{zip_download_dir}/train.zip", 'r') as z:
    z.extractall(train_root)
print(f"Extracted training data to: {train_root}")