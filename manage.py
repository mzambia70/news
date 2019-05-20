from app import create_app
from flask_script import Manager,Server #initialise our extensions and server class that aid in launching of our server
# Creating app instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server) #launch app server

@manager.command 
def test():
    """Run the ubit tests"""
    import unittest
    tests = unittest 
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__': #checks if the script is run directly
    manager.run()