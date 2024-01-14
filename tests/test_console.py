import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.cmd = HBNBCommand()

    def test_do_quit(self):
        self.assertTrue(self.cmd.do_quit(''))

    def test_do_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.cmd.do_EOF(''))
            self.assertEqual(f.getvalue(), '\n')

    def test_do_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.do_create('BaseModel')
            self.assertIn('-', f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.do_create('InvalidClass')
            self.assertEqual(f.getvalue(),
                             '** class doesn\'t exist **\n')

        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.do_create('')
            self.assertEqual(f.getvalue(), '** class name missing **\n')

    def test_do_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.do_show('BaseModel 1234')
            self.assertEqual(f.getvalue(), '** no instance found **\n')

        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.do_show('BaseModel')
            self.assertEqual(f.getvalue(),
                             '** instance id missing **\n')

        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.do_show('')
            self.assertEqual(f.getvalue(), '** class name missing **\n')

    def test_do_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.do_destroy('BaseModel 1234')
            self.assertEqual(f.getvalue(), '** no instance found **\n')

        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.do_destroy('BaseModel')
            self.assertEqual(f.getvalue(),
                             '** instance id missing **\n')

        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.do_destroy('')
            self.assertEqual(f.getvalue(), '** class name missing **\n')

    def test_do_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.do_all('BaseModel')
            self.assertIn('BaseModel', f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.do_all('')
            self.assertIn('BaseModel', f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.do_all('InvalidClass')
            self.assertEqual(f.getvalue(),
                             '** class doesn\'t exist **\n')

    def test_do_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.do_count('BaseModel')
            self.assertGreater(int(f.getvalue()), 0)

        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.do_count('')
            self.assertGreater(int(f.getvalue()), 0)

        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.do_count('InvalidClass')
            self.assertEqual(int(f.getvalue()), 0)

    def test_do_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.do_update('BaseModel 1234')
            self.assertEqual(f.getvalue(), '** no instance found **\n')

        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.do_update('BaseModel')
            self.assertEqual(f.getvalue(),
                             '** instance id missing **\n')

        with patch('sys.stdout', new=StringIO()) as f:
            self.cmd.do_update('')
            self.assertEqual(f.getvalue(), '** class name missing **\n')


if __name__ == '__main__':
    unittest.main()
