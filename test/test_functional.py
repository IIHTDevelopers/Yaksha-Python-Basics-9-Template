import unittest
import sys
import os

# Adjusting the path to import TestUtils and the required modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from test.TestUtils import TestUtils
from CourierTrackingSystem import list_all_shipments, check_shipment_status, count_shipments_by_status
from DonationManagementSystem import save_static_donations, check_frank_white_donated, calculate_total_donations
from PharmacyManagementSystem import count_number_of_unique_medicines, calculate_total_stock_value, find_medicine_with_lowest_stock


class TestManagementSystems(unittest.TestCase):
    def setUp(self):
        # Initialize TestUtils object for yaksha assertions
        self.test_obj = TestUtils()

    # ========== Courier Tracking System Tests ==========
    def test_list_all_shipments(self):
        """
        Test case for list_all_shipments() function.
        """
        try:
            result = list_all_shipments()
            # Check if the result is a list and has 5 shipments
            if isinstance(result, list) and len(result) == 5:
                self.test_obj.yakshaAssert("TestListAllShipments", True, "functional")
                print("TestListAllShipments = Passed")
            else:
                self.test_obj.yakshaAssert("TestListAllShipments", False, "functional")
                print("TestListAllShipments = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestListAllShipments", False, "functional")
            print(f"TestListAllShipments = Failed | Exception: {e}")

    def test_check_shipment_status(self):
        """
        Test case for check_shipment_status() function.
        """
        try:
            # Test with a valid tracking number
            result = check_shipment_status("TRK1003")
            expected_result = "Out for Delivery"
            
            if result == expected_result:
                self.test_obj.yakshaAssert("TestCheckShipmentStatus", True, "functional")
                print("TestCheckShipmentStatus = Passed")
            else:
                self.test_obj.yakshaAssert("TestCheckShipmentStatus", False, "functional")
                print("TestCheckShipmentStatus = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestCheckShipmentStatus", False, "functional")
            print(f"TestCheckShipmentStatus = Failed | Exception: {e}")

    # ========== Donation Management System Tests ==========
    def test_check_frank_white_donated(self):
        """
        Test case for check_frank_white_donated() function.
        """
        try:
            result = check_frank_white_donated()
            expected_result = True
            
            if result == expected_result:
                self.test_obj.yakshaAssert("TestCheckFrankWhiteDonated", True, "functional")
                print("TestCheckFrankWhiteDonated = Passed")
            else:
                self.test_obj.yakshaAssert("TestCheckFrankWhiteDonated", False, "functional")
                print("TestCheckFrankWhiteDonated = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestCheckFrankWhiteDonated", False, "functional")
            print(f"TestCheckFrankWhiteDonated = Failed | Exception: {e}")

    def test_calculate_total_donations(self):
        """
        Test case for calculate_total_donations() function.
        """
        try:
            result = calculate_total_donations()
            expected_result = 620  # Sum of all donation amounts (100+50+200+150+120)
            
            if result == expected_result:
                self.test_obj.yakshaAssert("TestCalculateTotalDonations", True, "functional")
                print("TestCalculateTotalDonations = Passed")
            else:
                self.test_obj.yakshaAssert("TestCalculateTotalDonations", False, "functional")
                print("TestCalculateTotalDonations = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestCalculateTotalDonations", False, "functional")
            print(f"TestCalculateTotalDonations = Failed | Exception: {e}")

    # ========== Pharmacy Management System Tests ==========
    def test_count_number_of_unique_medicines(self):
        """
        Test case for count_number_of_unique_medicines() function.
        """
        try:
            result = count_number_of_unique_medicines()
            expected_result = 4  # There are 4 unique medicines in the dataset
            
            if result == expected_result:
                self.test_obj.yakshaAssert("TestCountNumberOfUniqueMedicines", True, "functional")
                print("TestCountNumberOfUniqueMedicines = Passed")
            else:
                self.test_obj.yakshaAssert("TestCountNumberOfUniqueMedicines", False, "functional")
                print("TestCountNumberOfUniqueMedicines = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestCountNumberOfUniqueMedicines", False, "functional")
            print(f"TestCountNumberOfUniqueMedicines = Failed | Exception: {e}")

    def test_calculate_total_stock_value(self):
        """
        Test case for calculate_total_stock_value() function.
        """
        try:
            result = calculate_total_stock_value()
            # Calculate expected result: (10*100) + (50*25) + (15*60) + (20*80) + (30*40)
            expected_result = 1000 + 1250 + 900 + 1600 + 1200  # = 5950
            
            if result == expected_result:
                self.test_obj.yakshaAssert("TestCalculateTotalStockValue", True, "functional")
                print("TestCalculateTotalStockValue = Passed")
            else:
                self.test_obj.yakshaAssert("TestCalculateTotalStockValue", False, "functional")
                print("TestCalculateTotalStockValue = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestCalculateTotalStockValue", False, "functional")
            print(f"TestCalculateTotalStockValue = Failed | Exception: {e}")

    def test_find_medicine_with_lowest_stock(self):
        """
        Test case for find_medicine_with_lowest_stock() function.
        """
        try:
            result = find_medicine_with_lowest_stock()
            expected_result = ("Amoxicillin", 25)  # Amoxicillin has the lowest stock of 25
            
            if result == expected_result:
                self.test_obj.yakshaAssert("TestFindMedicineWithLowestStock", True, "functional")
                print("TestFindMedicineWithLowestStock = Passed")
            else:
                self.test_obj.yakshaAssert("TestFindMedicineWithLowestStock", False, "functional")
                print("TestFindMedicineWithLowestStock = Failed")
        except Exception as e:
            self.test_obj.yakshaAssert("TestFindMedicineWithLowestStock", False, "functional")
            print(f"TestFindMedicineWithLowestStock = Failed | Exception: {e}")


if __name__ == '__main__':
    unittest.main()
