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
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertTrue(self.cmd.do_EOF(''))
            self.assertEqual(fake_out.getvalue(), '\n')

    def test_do_create(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.do_create('BaseModel')
            self.assertIn('-', fake_out.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.do_create('InvalidClass')
            self.assertEqual(fake_out.getvalue(),
                             '** class doesn\'t exist **\n')

        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.do_create('')
            self.assertEqual(fake_out.getvalue(), '** class name missing **\n')

    def test_do_show(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.do_show('BaseModel 1234')
            self.assertEqual(fake_out.getvalue(), '** no instance found **\n')

        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.do_show('BaseModel')
            self.assertEqual(fake_out.getvalue(),
                             '** instance id missing **\n')

        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.do_show('')
            self.assertEqual(fake_out.getvalue(), '** class name missing **\n')

    def test_do_destroy(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.do_destroy('BaseModel 1234')
            self.assertEqual(fake_out.getvalue(), '** no instance found **\n')

        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.do_destroy('BaseModel')
            self.assertEqual(fake_out.getvalue(),
                             '** instance id missing **\n')

        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.do_destroy('')
            self.assertEqual(fake_out.getvalue(), '** class name missing **\n')

    def test_do_all(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.do_all('BaseModel')
            self.assertIn('BaseModel', fake_out.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.do_all('')
            self.assertIn('BaseModel', fake_out.getvalue())

        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.do_all('InvalidClass')
            self.assertEqual(fake_out.getvalue(),
                             '** class doesn\'t exist **\n')

    def test_do_count(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.do_count('BaseModel')
            self.assertGreater(int(fake_out.getvalue()), 0)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.do_count('')
            self.assertGreater(int(fake_out.getvalue()), 0)

        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.do_count('InvalidClass')
            self.assertEqual(int(fake_out.getvalue()), 0)

    def test_do_update(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.do_update('BaseModel 1234')
            self.assertEqual(fake_out.getvalue(), '** no instance found **\n')

        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.do_update('BaseModel')
            self.assertEqual(fake_out.getvalue(),
                             '** instance id missing **\n')

        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.cmd.do_update('')
            self.assertEqual(fake_out.getvalue(), '** class name missing **\n')


if __name__ == '__main__':
    unittest.main()
