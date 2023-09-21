from django.test import TestCase


class TestBasicCalculation(TestCase):

    def test_basic_sum(self):
        # Arrange
        expected_result = 5
        x = 1
        y = 4

        # Act
        summy = x + y

        # Assert
        self.assertEqual(summy, expected_result)
