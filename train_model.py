# # import os
# # import pandas as pd
# # from sklearn.model_selection import train_test_split
# # from sklearn.ensemble import RandomForestClassifier
# # from sklearn.metrics import accuracy_score
# # import joblib

# # def load_dataset(data_dir, labels_file):
# #     data = []
# #     labels = []
# #     df = pd.read_csv(labels_file)
# #     print(df)  # Add this line to print the DataFrame
# #     for index, row in df.iterrows():
# #         gesture = row['gesture']
# #         label = row['label']
# #         csv_file = os.path.join(data_dir, f'{gesture}.csv')
# #         if os.path.exists(csv_file):
# #             df_gesture = pd.read_csv(csv_file, header=None)
# #             data.extend(df_gesture.values)
# #             labels.extend([label] * len(df_gesture))
# #     return data, labels

# # def main():
# #     data_dir = 'data/train'
# #     labels_file = 'data/labels.csv'
# #     data, labels = load_dataset(data_dir, labels_file)
# #     X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
# #     model = RandomForestClassifier(n_estimators=100, random_state=42)
# #     model.fit(X_train, y_train)
# #     y_pred = model.predict(X_test)
# #     accuracy = accuracy_score(y_test, y_pred)
# #     print(f'Model Accuracy: {accuracy * 100:.2f}%')
# #     joblib.dump(model, 'models/isl_model.pkl')

# # if __name__ == '__main__':
# #     main()



# import os
# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score
# import joblib

# def load_dataset(data_dir, labels_file):
#     data = []
#     labels = []
#     df = pd.read_csv(labels_file)
#     for index, row in df.iterrows():
#         gesture = row['gesture']
#         label = row['label']
#         csv_file = os.path.join(data_dir, f'{gesture}.csv')
#         if os.path.exists(csv_file):
#             df_gesture = pd.read_csv(csv_file, header=None)
#             data.extend(df_gesture.values)
#             labels.extend([label] * len(df_gesture))
#     return data, labels

# def main():
#     data_dir = 'data/train'
#     labels_file = 'data/labels.csv'
#     data, labels = load_dataset(data_dir, labels_file)
#     X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
#     model = RandomForestClassifier(n_estimators=100, random_state=42)
#     model.fit(X_train, y_train)
#     y_pred = model.predict(X_test)
#     accuracy = accuracy_score(y_test, y_pred)
#     print(f'Model Accuracy: {accuracy * 100:.2f}%')
#     joblib.dump(model, 'models/isl_model.pkl')

# if __name__ == '__main__':
#     main()



import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

def load_dataset(data_dir, labels_file):
    data = []
    labels = []
    df = pd.read_csv(labels_file)
    print(df)  # Add this line to print the DataFrame
    print(f"Loading data for gesture: {gesture}")
    print(f"CSV file path: {csv_file}")
    for index, row in df.iterrows():
        gesture = row['gesture']
        label = row['label']
        csv_file = os.path.join(data_dir, f'{gesture}.csv')
        if os.path.exists(csv_file):
            df_gesture = pd.read_csv(csv_file, header=None)
            data.extend(df_gesture.values)
            labels.extend([label] * len(df_gesture))
    return data, labels

def main():
    data_dir = 'data/train'
    labels_file = 'data/labels.csv'
    data, labels = load_dataset(data_dir, labels_file)
    X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Model Accuracy: {accuracy * 100:.2f}%')
    joblib.dump(model, 'models/isl_model.pkl')

if __name__ == '__main__':
    main()