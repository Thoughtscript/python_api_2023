from handlers import initHandlers

if __name__ == '__main__':

    try:
        # Initialize ML models

        # initDB()

        initHandlers()

    except Exception as ex:
        print('Exception: ' + str(ex))