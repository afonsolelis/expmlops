import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Carregar o dataset Iris
iris = sns.load_dataset('iris')

# Análise exploratória
def exploratory_analysis(data):
    print("Primeiras linhas do dataset:")
    print(data.head())
    print("\nResumo estatístico:")
    print(data.describe())
    print("\nInformações gerais:")
    print(data.info())

    # Visualizações
    sns.pairplot(data, hue="species", palette="viridis")
    plt.title("Pairplot das Variáveis do Dataset Iris")
    plt.show()

    sns.heatmap(data.corr(numeric_only=True), annot=True, cmap="coolwarm")
    plt.title("Mapa de Calor das Correlações")
    plt.show()

# Treinamento de um modelo de Machine Learning
def train_model(data):
    # Dividir os dados em X (features) e y (label)
    X = data.drop(columns='species')
    y = data['species']

    # Divisão em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Modelo: Random Forest
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Predição
    y_pred = model.predict(X_test)

    # Avaliação do modelo
    print("\nMatriz de Confusão:")
    print(confusion_matrix(y_test, y_pred))
    print("\nRelatório de Classificação:")
    print(classification_report(y_test, y_pred))
    print(f"Acurácia: {accuracy_score(y_test, y_pred):.2f}")

# Main
if __name__ == "__main__":
    print("### Análise Exploratória ###")
    exploratory_analysis(iris)
    print("### Treinamento do Modelo ###")
    train_model(iris)
