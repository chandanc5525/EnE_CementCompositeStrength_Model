from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
import pandas as pd
import numpy as np

def apply_pca(df, target_col, variance_threshold=0.90):
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(df.drop(columns=[target_col]))

    for i in range(1, df.shape[1]):
        pca = PCA(n_components=i)
        pca.fit(X_scaled)
        evr = np.cumsum(pca.explained_variance_ratio_)
        if evr[i - 1] >= variance_threshold:
            pcs = i
            break

    pca = PCA(n_components=pcs)
    pca_data = pca.fit_transform(X_scaled)
    pca_columns = [f'PC{j+1}' for j in range(pcs)]
    pca_df = pd.DataFrame(pca_data, columns=pca_columns)
    pca_df[target_col] = df[target_col].values
    return pca_df
