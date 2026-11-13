import unittest
from aerospace_optimizer import parameter

class TestParameter(unittest.TestCase):
    def test_Parameter_init(self):
        param = parameter.Parameter('test', -1, 1)
        self.assertEqual(param.name, 'test')
        self.assertEqual(param.lower_bound, -1)
        self.assertEqual(param.upper_bound, 1)

    def test_Parameter_bounds_property(self):
        param = parameter.Parameter('test', -1, 1)
        self.assertEqual(param.bounds, (-1, 1))

    def test_ParameterSet_add_parameter(self):
        params = parameter.ParameterSet()
        params.add_parameter('test', -1, 1)
        self.assertIn('test', params.parameters)

    def test_ParameterSet_get_parameter(self):
        params = parameter.ParameterSet()
        params.add_parameter('test', -1, 1)
        param = params.get_parameter('test')
        self.assertEqual(param.name, 'test')

if __name__ == '__main__':
    unittest.main()
