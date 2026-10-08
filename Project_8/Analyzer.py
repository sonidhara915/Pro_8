import numpy as np
            With the name : numpyanalyzer 

class numpyanalyzer:
    pass
class numpyanalyzer(numpyanalyzer):
    def __init__(self):
       
        self.__current_array = None 
        print("Tools are Ready to Analyze with your skill")

    def __del__(self):
        print("Analyzer is Ready to Shutdown")
        
    def get_array(self):
        return self.__current_array
        
    def set_array(self, arr):
        self.__current_array = arr
class numpyanalyzer(numpyanalyzer):
    def cre_arr(self, elements_str, rows, cols):
        
        try:
            flat_arr = np.fromstring(elements_str, sep=' ')
            arr = flat_arr.reshape(rows, cols)
            self.set_array(arr)
            return self.get_array()
        except Exception as e:
            print(f"Error creating array: {e}")
            return None
class numpyanalyzer(numpyanalyzer):
    def math_op(self, elements_str, operation="1"):
        """Performs element-wise arithmetic array operations or matrices slicing."""
        curr = self.get_array()
        if operation in ["1", "2", "3", "4"]:
            other = np.fromstring(elements_str, sep=' ').reshape(curr.shape)
            
            print("\nSecond Array:\n", other)
            
            if operation == "1": 
                return np.add(curr, other)
            
            elif operation == "2": 
                return np.subtract(curr, other)
            
            elif operation == "3": 
                return np.multiply(curr, other)
            
            elif operation == "4": 
                return np.divide(curr, other)
            
        elif operation == "5": 
            
            r_start, r_end = map(int, elements_str.split(',')[0].split(':'))
            c_start, c_end = map(int, elements_str.split(',')[1].split(':'))
            return curr[r_start:r_end, c_start:c_end]
class numpyanalyzer(numpyanalyzer):
    def combine_arr(self, elements_str, mode="1"):
        
        curr = self.get_array()
        other = np.fromstring(elements_str, sep=' ').reshape(curr.shape)
        print("\nSecond Array:\n", other)
        if mode == "1":
            return np.vstack((curr, other))
        elif mode == "2":
            return np.hstack((curr, other))
class numpyanalyzer(numpyanalyzer):
    
    def search_val(self, target):

        idx = np.where(self.get_array() == target)
        return list(zip(idx[0], idx[1]))
class numpyanalyzer(numpyanalyzer):
    
    def sort_arr(self):
       
        return np.sort(self.get_array(), axis=-1)
class numpyanalyzer(numpyanalyzer):
    
    def filter_greater(self, limit):
       
        return self.get_array()[self.get_array() > limit]
class numpyanalyzer(numpyanalyzer):
    def run_aggregations(self, op_choice):
        curr = self.get_array()
        
        if op_choice == "1": 
            print("Sum of Array:", np.sum(curr))

        elif op_choice == "2": 
            print("Mean of Array:", np.mean(curr))

class numpyanalyzer(numpyanalyzer):

    def run_statistics(self, op_choice):
        curr = self.get_array()
        
        if op_choice == "3": 
            print("Median of Array:", np.median(curr))

        elif op_choice == "4": 
            print("Standard Deviation:", np.std(curr))

        elif op_choice == "5": 
            print("Variance of Array:", np.var(curr))

def start_menu():
    analyzer = numpyanalyzer()
    
    while True:
        print("\nChoose an option:")
        print("1. Create a Numpy Array.")
        print("2. Perform Methamatical Operation.")
        print("3. Combine or Split Arrays.")
        print("4. Search,Sort or Filter Arrays.")
        print("5. Compute Aggregates and Statistics.")
        print("6. Exit.")
        
        choice = input("Enter your choice: ").strip()
        
        if choice == "1":
            print("Which type of Array You have to Creat")
            print("\n 1. 1D Array")
            print("\n 2. 2D Array")
            print("\n 3. 3D Array")
            
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            elements = input(f"Enter {rows*cols} elements separated by space: ")
            print("\nArray created successfully:\n", analyzer.cre_arr(elements, rows, cols))
            
        elif choice == "2":
            print("\n1. Addition") 
            print("\n2. Subtraction" )
            print("\n3. Multiplication" )
            print("\n4. Division" )
            print("\n5. Slicing")

            op = input("Enter your choice: ").strip()
            if op == "5":
                slice_range = input("Enter ranges as 'row_start:row_end,col_start:col_end' (e.g., 0:2,1:3): ")
                print("\nSliced Array:\n", analyzer.math_op(slice_range, "5"))
            else:
                elements = input("Enter the same-size array elements separated by space: ")
                print("\nOriginal Array:\n", analyzer.get_array())
                print("\nResult:\n", analyzer.math_op(elements, op))
                
        elif choice == "3":
            print("\n1. Combine Arrays (Vertical Stack)\n2. Combine Arrays (Horizontal Stack)")
            mode = input("Enter your choice: ").strip()
            elements = input("Enter the elements of another array to combine: ")
            print("\nOriginal Array:\n", analyzer.get_array())
            print("\nCombined Array:\n", analyzer.combine_arr(elements, mode))
            
        elif choice == "4":
            print("\n1. Search a value")
            print("\n2. Sort the array")
            print("\n3. Filter values")

            sub = input("Enter your choice: ").strip()
            
            print("\nOriginal Array:\n", analyzer.get_array())

            if sub == "1":
                target = float(input("Enter target value: "))
                print("Coordinates positions:", analyzer.search_val(target))

            elif sub == "2":
                print("\nSorted Array:\n", analyzer.sort_arr())
                print("(Sorting applied row-wise.)")

            elif sub == "3":
                limit = float(input("Filter values greater than: "))
                print("Filtered numbers:", analyzer.filter_greater(limit))
                
        elif choice == "5":
            print("\nChoose an aggregate/statistical operation:")
            print("\n1. Sum")
            print("\n2. Mean")
            print("\n3. Median")
            print("\n4. Standard Deviation")
            print("\n5. Variance")

            op_choice = input("Enter your choice: ").strip()
            
            print("\nOriginal Array:\n", analyzer.get_array())
            
            if op_choice in ["1", "2"]:
                analyzer.run_aggregations(op_choice)
            elif op_choice in ["3", "4", "5"]:
                analyzer.run_statistics(op_choice)
                
        elif choice == "6":
            print("\nThank you for using the NumPy Analyzer! Goodbye!")
            del analyzer
            break
start_menu()
