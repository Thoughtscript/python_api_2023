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

                predict, AL, parameters = helpers.layers(DATA, LABELS, parameters, 1.155)

                if (predict == TEST).all():
                    found = i
                    result = predict
                    break

            print("ANN arrived at conclusion: " + str(result) + " after " + str(found) + " iterations ")
            return parameters


        DATA = np.array([[1,0], [0,1], [1,1], [0,0], [1,1], [1,0], [0,1], [1,1], [0,1], [0,0], [1,0], [0,0], [0,1]])
        LABELS = np.array([[1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1]])
        TEST = np.array([[True, True, False, False, False, True, True, False, True, False, True, False, True]])
        # 1st layer is same as DATA.T.shape[0]
        LAYERS = np.array([DATA.T.shape[0], DATA.T.shape[1], 1])

        MODEL = train_ml_ann(DATA.T, LABELS, LAYERS, 100, TEST)
        # print(MODEL)
        helpers.saveModel(MODEL, 'xor')

        # --------------------------------------------------------------- #
        # Now, let's save off the training data above (results) and ...
        # pass in a fresh set of data

        DATA = np.array([[1, 1], [0, 0], [1, 0], [0, 1]])
        testResult = helpers.predict_ann(DATA.T, MODEL)
        expected = "[[False False  True  True]]"
        result = str(testResult)
        print("XOR test set 1: " + result + " from " + str(DATA).replace("\n", "") + " passed: " + str(result == expected))

        DATA = np.array([[0, 1], [1, 1], [1, 1], [0, 1]])
        testResult = helpers.predict_ann(DATA.T, MODEL)
        expected = "[[ True False False  True]]"
        result = str(testResult)
        print("XOR test set 2: " + result + " from " + str(DATA).replace("\n", "") + " passed: " + str(result == expected))

        DATA = np.array([[1, 1], [1, 1], [1, 1], [1, 1]])
        testResult = helpers.predict_ann(DATA.T, MODEL)
        expected = "[[False False False False]]"
        result = str(testResult)
        print("XOR test set 3: " + result + " from " + str(DATA).replace("\n", "") + " passed: " + str(result == expected))

        DATA = np.array([[0, 1], [0, 1], [0, 1], [0, 1]])
        testResult = helpers.predict_ann(DATA.T, MODEL)
        expected = "[[ True  True  True  True]]"
        result = str(testResult)
        print("XOR test set 4: " + result + " from " + str(DATA).replace("\n", "") + " passed: " + str(result == expected))

        DATA = np.array([[0, 0], [0, 0], [0, 0], [0, 0]])
        testResult = helpers.predict_ann(DATA.T, MODEL)
        expected = "[[False False False False]]"
        result = str(testResult)
        print("XOR test set 5: " + result + " from " + str(DATA).replace("\n", "") + " passed: " + str(result == expected))

        DATA = np.array([
            [1, 1], [0, 0], [1, 0], [0, 1], [1, 1], [0,0], [1,0], [0,1]
        ])
        testResult = helpers.predict_ann(DATA.T, MODEL)
        expected = "[[False False  True  True False False  True  True]]"
        result = str(testResult)
        print("XOR test set 6: " + result + " from " + str(DATA).replace("\n", "") + " passed: " + str(result == expected))

    except Exception as ex:

        print('Exception! ' + str(ex))
