import sys

def is_one_to_one(str1: str, str2: str) -> bool:    
    # By definition of one-to-one function there can be a char in str2 that
    # isn't mapped to a char in str1 so str2 can be longer than str1
    if len(str1) > len(str2):
        return False

    # Dictionary to store mappings
    dictionary = dict()

    for i in range(len(str1)):
        c1 = str1[i];
        c2 = str2[i];
        # If char at index i -> False
        if c1 in dictionary:
            if c2 != dictionary[c1]:
                return False
        # Add new mapping
        else:
            dictionary[c1] = c2
            
            
    return True

def main():
    if len(sys.argv) != 3:
        print("Incorrect number of arguments. Must provide exactly 2 arguments")
    else:
        str1 = sys.argv[1]
        str2 = sys.argv[2]
        print(is_one_to_one(str1, str2))


  
if __name__ == "__main__":
  main()
