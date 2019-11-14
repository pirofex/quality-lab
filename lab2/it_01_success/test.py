import unittest

from wordpress_system import bootstrapper

class Test(unittest.TestCase):
    def test_system_available(self):
        """
        Test that the system is available.
        """
        system = bootstrapper.create()
        self.assertTrue(system.is_available)

    def test_valid_password(self):
        """
        Test that the registration component accepts valid passwords.
        """
        system = bootstrapper.create()
        result = system.register_user('name', 'Password1')

        self.assertTrue(result)
    
    def test_invalid_password(self):
        """
        Test that the registration component rejects invalid passwords.
        """
        system = bootstrapper.create()
        result = system.register_user('name', 'pass')

        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()