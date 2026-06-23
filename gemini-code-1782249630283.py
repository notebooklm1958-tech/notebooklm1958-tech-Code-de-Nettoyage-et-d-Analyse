import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# On suppose que votre DataFrame s'appelle déjà 'df'
# (Décommentez la ligne ci-dessous si vous devez d'abord le charger)
# df = pd.read_csv("votre_fichier.csv")

# =====================================================================
# ETAPE 1 : Exploration Initiale
# =====================================================================
print("--- APERÇU DES DONNÉES ---")
print(df.head())

print("\n--- INFORMATIONS GÉNÉRALES ---")
print(df.info())

print("\n--- VALEURS MANQUANTES (AVANT) ---")
print(df.isnull().sum())

# =====================================================================
# ETAPE 2 : Nettoyage des Données
# =====================================================================

# 1. Suppression des doublons
df = df.drop_duplicates()

# 2. Gestion des valeurs manquantes (Options au choix)
# Option A : Supprimer les lignes contenant des valeurs manquantes
# df = df.dropna()

# Option B : Remplacer par la moyenne/médiane (pour les colonnes numériques)
num_cols = df.select_dtypes(include=[np.number]).columns
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

# Option C : Remplacer par une valeur fixe ou le mode (pour le texte)
cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else "Inconnu")

# 3. Correction des types de données (Exemple si vous avez une colonne 'date')
# if 'date' in df.columns:
#     df['date'] = pd.to_datetime(df['date'])

print("\n--- VALEURS MANQUANTES (APRÈS NETTOYAGE) ---")
print(df.isnull().sum())

# =====================================================================
# ETAPE 3 : Analyse Statistique
# =====================================================================
print("\n--- STATISTIQUES DESCRIPTIVES ---")
print(df.describe(include='all'))

# =====================================================================
# ETAPE 4 : Visualisation (Analyse Graphique)
# =====================================================================

# 1. Distribution des variables numériques (Histogrammes)
if len(num_cols) > 0:
    df[num_cols].hist(bins=15, figsize=(15, 10))
    plt.suptitle("Distribution des variables numériques")
    plt.show()

# 2. Matrice de corrélation (uniquement s'il y a plusieurs variables numériques)
if len(num_cols) > 1:
    plt.figure(figsize=(10, 8))
    sns.heatmap(df[num_cols].corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Matrice de corrélation")
    plt.show()