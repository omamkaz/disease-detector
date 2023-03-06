# Website source: https://www.geeksforgeeks.org/disease-prediction-using-machine-learning/

# Importing libraries
import numpy as np
import pandas as pd

from scipy.stats import mode
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier

from .base_dir import Assets

DATA_PATH = Assets.data("Training.csv")


class DiseasePrediction:
    def __init__(self):
        # Reading the train.csv by removing the
        # last column since it's an empty column
        data = pd.read_csv(DATA_PATH).dropna(axis=1)

        # Encoding the target value into numerical
        # value using LabelEncoder
        encoder = LabelEncoder()
        data["prognosis"] = encoder.fit_transform(data["prognosis"])

        x = data.iloc[:, :-1]
        y = data.iloc[:, -1]

        # Training the models on whole data
        self.final_svm_model = SVC()
        self.final_nb_model = GaussianNB()
        self.final_rf_model = RandomForestClassifier(random_state=18)

        self.final_svm_model.fit(x, y)
        self.final_nb_model.fit(x, y)
        self.final_rf_model.fit(x, y)

        # Creating a symptom index dictionary to encode the
        # input symptoms into numerical form
        symptom_index = {}
        for index, value in enumerate(x.columns.values):  # symptoms
            symptom = " ".join(
                [i.lower() for i in value.split("_")]
            )  # convert  " " spacs between word to word
            symptom_index[symptom] = index  # storg index in symptom = Detials

        self.data_dict = {
            "symptom_index": symptom_index,
            "predictions_classes": encoder.classes_,
        }  # disease + symptom => map

    # Defining the Function
    # Input: string containing symptoms
    # Output: Generated predictions by models
    def predictDisease(self, symptoms: list):
        # creating input data for the models
        input_data = [0] * len(self.data_dict["symptom_index"])
        for symptom in symptoms:
            try:
                index = self.data_dict["symptom_index"][symptom.lower().strip()]
                input_data[index] = 1
            except Exception as err:
                print("Error: ", err)
                continue

        # reshaping the input data and converting it
        # into suitable format for model predictions
        input_data = np.array(input_data).reshape(1, -1)

        # generating individual outputs
        rf_prediction = self.data_dict["predictions_classes"][
            self.final_rf_model.predict(input_data)[0]
        ]
        nb_prediction = self.data_dict["predictions_classes"][
            self.final_nb_model.predict(input_data)[0]
        ]
        svm_prediction = self.data_dict["predictions_classes"][
            self.final_svm_model.predict(input_data)[0]
        ]

        # making final prediction by taking mode of all predictions
        final_prediction = mode([rf_prediction, nb_prediction, svm_prediction])[0][0]

        predictions = {
            "rf_model_prediction": rf_prediction,
            "naive_bayes_prediction": nb_prediction,
            "svm_model_prediction": nb_prediction,
            "final_prediction": final_prediction,
        }
        return predictions
