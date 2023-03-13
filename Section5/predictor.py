import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

from mlxtend.plotting import plot_confusion_matrix
from sklearn.preprocessing import OrdinalEncoder
buying_price_category = ['low', 'med', 'high', 'vhigh']
maint_cost_category = ['low', 'med', 'high', 'vhigh']
doors_category = ['2', '3', '4', '5more']
person_capacity_category = ['2', '4', 'more']
lug_boot_category = ['small', 'med', 'big']
safety_category = ['low', 'med', 'high']
class_catergory =['unacc', 'acc', 'good', 'vgood']
all_categories = [maint_cost_category,doors_category,lug_boot_category,safety_category, class_catergory]
oe = OrdinalEncoder(categories= all_categories)


def prep_data():
    """
    This function reads data from a file named "car.data", removes the "persons" column and writes the remaining columns
    (i.e., 'buying_price', 'maint_cost', 'doors', 'lug_boot', 'safety', 'class') to a new file named "car.csv".

    Parameters:
        None

    Returns:
        None
    """
    # Open the input file in read mode
    file = open("car.data", "r")

    # Open the output file in write mode
    csvfile = open("car.csv", "w", newline='')

    # Create a csv writer object
    csvwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)

    # Write the header row to the output file
    csvwriter.writerow(['buying_price', 'maint_cost', 'doors', 'lug_boot', 'safety', 'class'])

    # Loop through each line in the input file
    for lines in file.readlines():
        # Remove the newline character from each line
        if "\n" in lines:
            lines = lines.replace("\n", "")

        # Split each line by comma
        s = lines.split(",")

        # Create a list to store the required columns
        out = []

        # Loop through each column in the line
        for i in range(len(s)):
            # Exclude the third column ('persons') as per the problem statement
            if i != 3:
                out.append(s[i])

        # Write the required columns to the output file
        csvwriter.writerow(out)

def train():
    """
    Trains a decision tree classifier on the car evaluation dataset after preprocessing the data.

    Returns:

    DT_classifier: a trained decision tree classifier.
    """

    global oe

    # Load the preprocessed data from the CSV file
    data = pd.read_csv("car.csv")

    # Separate the feature columns from the target column
    X = data.drop(['buying_price'], axis=1)
    X = X.astype(str)
    y = data['buying_price']

    # One-hot encode the feature columns
    X = oe.fit_transform(data[['maint_cost', 'doors', 'lug_boot', 'safety', 'class']])

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=2)

    # Create a decision tree classifier object and fit it to the training data
    DT_classifier = DecisionTreeClassifier(criterion='gini', max_depth=2, min_samples_split=500)
    DT_classifier.fit(X_train, y_train)

    # Use the classifier to make predictions on the test data and calculate the accuracy
    y_pred = DT_classifier.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    sum = 0
    total = 0
    for i in range(0, len(cm)):
        for j in range(0, len(cm[0])):
            if i == j:
                sum = sum + cm[i][j]
            total = total + cm[i][j]
    acc = sum / total

    # Print the accuracy and return the trained classifier
    print("acc: " + str(acc))
    return DT_classifier


def predict(classifier):
    """
    predict(classifier)
    A function that takes a trained classifier as input and predicts the buying price based on the input data in the
    'input.csv' file.

    Args:
    classifier: A trained decision tree classifier object

    Returns:
    None - The function only prints the predicted buying price for the input data
    """
    sample = pd.read_csv("input.csv")
    sample = sample.astype(str)
    sample = oe.fit_transform(sample[['maint_cost', 'doors', 'lug_boot', 'safety', 'class']])
    y_pred = classifier.predict(sample)
    print(y_pred)


if __name__ == '__main__':
    prep_data()
    predict(train())








