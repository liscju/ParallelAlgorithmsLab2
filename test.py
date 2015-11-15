__author__ = 'liscju'

from unittest import TestCase

from calculations import Star, G, calculate_forces, calculate_force


class TestStar(TestCase):
    def test_calculate_force_case1(self):
        s1 = Star(1, 10, (0, 0, 0))
        s2 = Star(2, 10, (0, 0, 1))

        force_result = s1.calculate_force(s2)

        expected_result = (0, 0, 100 * G)
        self.assertEqual(force_result, expected_result)

    def test_calculate_force_case2(self):
        s1 = Star(1, 1, (0, 0, 0))
        s2 = Star(2, 1, (0, 1, 0))

        force_result = s1.calculate_force(s2)

        expected_result = (0, G, 0)
        self.assertEqual(force_result, expected_result)

    def test_calculate_force_case3(self):
        s1 = Star(1, 10, (0, 0, 0))
        s2 = Star(2, 5, (0, 1, 0))

        force_result = s1.calculate_force(s2)

        expected_result = (0, 50*G, 0)
        self.assertEqual(force_result, expected_result)


class TestCalculationMethods(TestCase):
    def test_calculate_forces_case1(self):
        s1 = Star(1, 10, (0, 0, 0))
        s2 = Star(2, 10, (0, 0, 1))
        s3 = Star(3, 1, (0, 1, 0))

        actual_forces = calculate_forces([s1, s2, s3])

        expected_first_result = (0, 10 * G, 100*G)
        self.assertEqual(actual_forces[0], expected_first_result)

    def test_calculate_force_case1(self):
        s1 = Star(1, 10, (0, 0, 0))
        s2 = Star(2, 10, (0, 1, 0))
        s3 = Star(3, 5, (0, 1, 0))

        actual_forces = calculate_force(s1, [s2, s3])

        expected_result = (0, 150*G, 0)
        self.assertEqual(actual_forces, expected_result)