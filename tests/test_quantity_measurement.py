import pytest
from quantity_measurement_problem import QuantityMeasurement
from qunatity_measurement_exception import QuantityMeasurementException


class TestQuantityMeasurementProblem:
        @pytest.mark.parametrize("length1,unit1,length2,unit2",[(0,"feet",0,"feet")])
        def test_zero_value_check(self, length1, unit1, length2, unit2):
            print(length1)
            quantity1 = QuantityMeasurement(length1, unit1)
            quantity2 = QuantityMeasurement(length2, unit2)
            assert quantity1 == quantity2

        @pytest.mark.parametrize('length1, unit1, length2, unit2', [(None, "feet", None, "feet")])
        def test_null_reference_check(self, length1, unit1, length2, unit2):
            quantity1 = QuantityMeasurement(length1, unit1)
            quantity2 = QuantityMeasurement(length2, unit2)
            with pytest.raises(QuantityMeasurementException) as exe:
                quantity1 == quantity2
            assert exe.value.message == 'Null'