# from app  import app
# from flask_script import Manager,Server

# # Creating app instance
# app = app('development')

# manager = Manager(app)
# manager.add_command('server',Server)

# if __name__ == '__main__':
#     manager.run()


from app import app

if __name__ == '__main__':
    app.run()