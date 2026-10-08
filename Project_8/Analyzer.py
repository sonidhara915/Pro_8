import numpy as np

class numpyanalyzer:

    def __init__(self):
        self.__current_array = None
        print("Tools are Ready to Analyze with your skill")

    def __del__(self):
        print("Analyzer is Ready to Shutdown")

    def get_array(self):
        return self.__current_array

    def set_array(self, arr):
        self.__current_array = arr

    def cre_arr(self, elements_str, rows, cols):
        try:
            arr = np.fromstring(elements_str, sep=' ').reshape(rows, cols)
            self.set_array(arr)
            return self.get_array()

        except Exception as e:
            print("Error creating array:", e)
            return None

    def math_op(self, elements_str, operation):
        curr = self.get_array()

        try:
            if operation == "5":
                r, c = elements_str.split(',')
                r_start, r_end = map(int, r.split(':'))
                c_start, c_end = map(int, c.split(':'))
                return curr[r_start:r_end, c_start:c_end]

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

        except Exception as e:
            print("Error:", e)

    def combine_arr(self, elements_str, mode):
        curr = self.get_array()

        try:
            other = np.fromstring(elements_str, sep=' ').reshape(curr.shape)
            print("\nSecond Array:\n", other)

            if mode == "1":
                return np.vstack((curr, other))

            elif mode == "2":
                return np.hstack((curr, other))

        except Exception as e:
            print("Error:", e)

    def search_val(self, target):
        idx = np.where(self.get_array() == target)
        return list(zip(idx[0], idx[1]))

    def sort_arr(self):
        return np.sort(self.get_array(), axis=-1)

    def filter_greater(self, limit):
        return self.get_array()[self.get_array() > limit]

    def statistics(self, choice):
        arr = self.get_array()

        if choice == "1":
            print("Sum:", np.sum(arr))

        elif choice == "2":
            print("Mean:", np.mean(arr))

        elif choice == "3":
            print("Median:", np.median(arr))

        elif choice == "4":
            print("Standard Deviation:", np.std(arr))

        elif choice == "5":
            print("Variance:", np.var(arr))


def start_menu():
    analyzer = numpyanalyzer()

    while True:

        print("Choose an option:")
        print("1. Create a Numpy Array")
        print("2. Mathematical Operation")
        print("3. Combine Arrays")
        print("4. Search, Sort or Filter")
        print("5. Aggregates and Statistics")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            print("1. 1D Array")
            print("2. 2D Array")
            print("3. 3D Array")

            arr_type = input("Enter array type: ")

            if arr_type == "1":

                elements = input("Enter elements separated by space: ")
                arr = np.fromstring(elements, sep=' ')

                analyzer.set_array(arr)
                print("\nArray created successfully:")
                print(arr)

            elif arr_type == "2":

                rows = int(input("Enter number of rows: "))
                cols = int(input("Enter number of columns: "))

                elements = input(f"Enter {rows * cols} elements separated by space: ")

                print("\nArray created successfully:\n",analyzer.cre_arr(elements, rows, cols))

            elif arr_type == "3":

                x = int(input("Enter number of blocks: "))
                rows = int(input("Enter number of rows: "))
                cols = int(input("Enter number of columns: "))

                elements = input(f"Enter {x * rows * cols} elements separated by space: ")

                try:
                    arr = np.fromstring(elements, sep=' ')
                    arr = arr.reshape(x, rows, cols)
                    analyzer.set_array(arr)
                    print("\n3D Array created successfully:")
                    print(arr)

                except Exception as e:
                    print("Error:", e)

        elif choice == "2":

            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Slicing")

            op = input("Enter your choice: ")

            if op == "5":

                slice_range = input("Enter range (row_start:row_end,col_start:col_end): ")
                print("\nSliced Array:\n",analyzer.math_op(slice_range, "5"))

            else:

                elements = input("Enter same-size array elements separated by space: ")
                print("\nOriginal Array:")
                print(analyzer.get_array())
                print("\nResult:")
                print(analyzer.math_op(elements, op))

        elif choice == "3":

            print("1. Vertical Stack")
            print("2. Horizontal Stack")

            mode = input("Enter your choice: ")

            elements = input("Enter elements of another array: ")

            print("\nOriginal Array:")
            print(analyzer.get_array())

            print("\nCombined Array:")
            print(analyzer.combine_arr(elements, mode))

        elif choice == "4":

            print("1. Search a value")
            print("2. Sort the array")
            print("3. Filter values")

            sub = input("Enter your choice: ")

            print("\nOriginal Array:")
            print(analyzer.get_array())

            if sub == "1":
                target = float(input("Enter target value: "))
                print("Coordinates:",analyzer.search_val(target))

            elif sub == "2":
                print("\nSorted Array:\n",analyzer.sort_arr())

            elif sub == "3":
                limit = float(input("Filter values greater than: "))
                print("Filtered numbers:",analyzer.filter_greater(limit))

        elif choice == "5":

            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print("4. Standard Deviation")
            print("5. Variance")

            op = input("Enter your choice: ")

            print("\nOriginal Array:")
            print(analyzer.get_array())
            analyzer.statistics(op)

        elif choice == "6":
            print("\nThank you for using the NumPy Analyzer! Goodbye!")
            del analyzer
            break

        else:
            print("Invalid choice.")


start_menu()
