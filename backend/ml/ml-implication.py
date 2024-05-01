# implementing a multi-layered ANN from scratch and to get a better sense about backwards propagation

import helpers
import numpy as np

if __name__ == '__main__':

    try:

        def train_ml_ann(DATA, LABELS, LAYERS, iterations, TEST):
            for x in range(len(DATA[0])):
                print("Data entry " + str(DATA[0][x]) + "&" + str(DATA[1][x]) + " with label " + str(LABELS[0][x]))

            result = None
            found = iterations
            parameters = helpers.initialize_parameters(LAYERS)

            for i in range(0, iterations):

                predict, AL, parameters = helpers.layers(DATA, LABELS, parameters, .25)

                if (predict == TEST).all():
                    found = i
                    result = predict
                    break

            print("ANN arrived at conclusion: " + str(result) + " after " + str(found) + " iterations ")
            return parameters


        DATA = np.array([[1,0], [1,0], [0,0], [1,1], [0,1]])
        LABELS = np.array([[0, 0, 1, 1, 1]])
        TEST = np.array([[False, False, True, True, True]])
        # 1st layer is same as DATA.T.shape[0]
        LAYERS = np.array([DATA.T.shape[0], DATA.T.shape[1], 1])

        MODEL = train_ml_ann(DATA.T, LABELS, LAYERS, 100, TEST)
        # print(MODEL)
        helpers.saveModel(MODEL, 'implication')

        # --------------------------------------------------------------- #
        # Now, let's save off the training data above (results) and ...
        # pass in a fresh set of data

        DATA = np.array([[1, 1], [0, 0], [1, 0], [0, 1]])
        testResult1 = helpers.predict_ann(DATA.T, MODEL)
        print("Test set 1: " + str(testResult1) + " from " + str(DATA))

        DATA = np.array([[0, 1], [1, 1], [1, 1], [0, 1]])
        testResult2 = helpers.predict_ann(DATA.T, MODEL)
        print("Test set 2: " + str(testResult2) + " from " + str(DATA))

        DATA = np.array([[1, 1], [0, 1], [1, 0], [1, 0]])
        testResult3 = helpers.predict_ann(DATA.T, MODEL)
        print("Test set 3: " + str(testResult3) + " from " + str(DATA))

        DATA = np.array([[0, 1], [1, 0], [1, 1], [0, 0], [1, 1], [0, 0]])
        testResult4 = helpers.predict_ann(DATA.T, MODEL)
        print("Test set 4: " + str(testResult4) + " from " + str(DATA))

        DATA = np.array([[0,0], [1,1], [0,1], [1,0]])
        testResult5 = helpers.predict_ann(DATA.T, MODEL)
        print("Test set 5: " + str(testResult5) + " from " + str(DATA))

        DATA = np.array([[1,0], [1,0], [1,0], [1,0], [1, 1], [0, 0]])
        testResult6 = helpers.predict_ann(DATA.T, MODEL)
        print("Test set 6: " + str(testResult6) + " from " + str(DATA))

    except Exception as ex:

        print('Exception! ' + str(ex))
