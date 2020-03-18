import sys

def is_one_to_one(str1: str, str2: str) -> bool:    
        # Unequal lengths -> false
        if len(str1) != len(str2):
            return False
        
        # Check that each instance of a char in str1 matches the same char in str2
        for i in range(len(str1)):
            c1 = str1[i];
            c2 = str2[i];
            
            for j in range(len(str2)):
                if (str1[j] == c1 and str2[j] != c2):
                    return False
                    
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
