from init import init_app

app = init_app()

if __name__ == '__main__':

    try:
        app.run(host="0.0.0.0", debug=True, port=5000)

    except Exception as ex:
        print('Exception: ' + str(ex))