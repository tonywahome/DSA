class UniqueInt:
    def __init__(self, input_filename, output_filename):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.unique_integers = [] 

    def is_int(self, s):
        """valid integer checker"""
        if s.startswith('-'):
            return s[1:].isdigit()
        return s.isdigit()
    
    def insert_sorted(self, number):
        """inserts number into sorted list"""
        if not self.unique_integers:
            self.unique_integers.append(number)
            return
        
    for i in range(len(self.unique_integers)):
        if self.unique_integers[i] > number: # type: ignore
            self.unique_integers.insert(i, number)
            return
    self.unique_integers.append(number) 

def process_unique_ints(lst):
    unique_set = set(lst)
    return list(unique_set)

# Example usage
numbers = [1, 2, 2, 3, 4, 4, 5]
print(process_unique_ints(numbers))  # Output: [1, 2, 3, 4, 5]

def procedure_file(self):
    """reads the input files and extracts unique integers"""
    with open(self.input_filename, 'r') as infile:
        for line in infile:
            line = line.strip() #removes whitespaces
            if not line:
                continue
            parts = line.split()

            if len(parts) != 1 or not self.is_integer(parts[0]):
                continue

            number = int(parts[0])
            self.insert_sorted(number)

    self.write_output()

def output(self):
    with open(self.output_filename, 'w') as outfile:
        for number in self.unique_integers:
            outfile.write(f"{number}\n")
    
input_filename = 'sample_01.txt'
output_filename = 'results_file.txt'
processor = UniqueInt(input_filename, output_filename)
processor.process_file()
    
