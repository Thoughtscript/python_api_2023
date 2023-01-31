from init import init_app

app = init_app()

if __name__ == '__main__':

    try:
        app.run()

    except Exception as ex:
        print('Exception: ' + str(ex))