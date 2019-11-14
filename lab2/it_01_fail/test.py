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

    def test_logging_in(self):
        """
        Test that the registration component rejects invalid passwords.
        """
        system = bootstrapper.create()
        result = system.register_user('name', 'pass')

        self.assertFalse(result)

    def test_invalid_site_type(self):
        """
        Test that site type selection rejects invalid types.
        """
        system = bootstrapper.create()
        result = system.select_type_of_site('School')

        self.assertFalse(result)

    def test_valid_site_type(self):
        """
        Test that site type selection accepts valid types.
        """
        system = bootstrapper.create()
        result = system.select_type_of_site('Business')

        self.assertTrue(result)

    def test_valid_site_name(self):
        """
        Test that site name selection accepts valid names.
        """
        system = bootstrapper.create()
        result = system.select_name_of_site('Test')

        self.assertTrue(result)

    def test_invalid_site_name(self):
        """
        Test that site name selection accepts valid names.
        """
        system = bootstrapper.create()
        result = system.select_name_of_site('Ab')

        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()