def saveModel(model, file_name):
    f = open("../models/" + file_name, "a")
    f.write(str(model))
    f.close()