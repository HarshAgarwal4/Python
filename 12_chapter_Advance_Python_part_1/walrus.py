# Using walrus operator 
if (n := len([1, 2, 3, 4, 5])) > 3: 
    print(f"List is too long ({n} elements, expected <= 3)") 
# Output: List is too long (5 elements, expected <= 3) 

#Type definition
a : int = 4
name : str = "Harsh"
b : int = 4

def sum(a: int , b :int) -> int :
    return a+b

print(sum(2,2))

def http_status(status): 
    match status: 
        case 200: 
            return "OK" 
        case 404: 
            return "Not Found" 
        case 500: 
            return "Internal Server Error" 
        case _: 
            return "Unknown status" 
# Usage 
print(http_status(200))  # Output: OK 
print(http_status(404))  # Output: Not Found 
print(http_status(500))  # Output: Internal Server Error 
print(http_status(403))  # Output: Unknown status