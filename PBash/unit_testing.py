import unittest


class MainTest(unittest.TestCase):
    def setUp(self):
        # be executed before each test
        pass

    def help_quit(self):
        print("application terminates properly")
        self.assertTrue(self.help_quit())





if __name__ == '__main__':
    # unittest.main(verbosity=2)  # with more details
    unittest.main()