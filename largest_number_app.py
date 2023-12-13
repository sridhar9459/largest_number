import streamlit as st

def find_largest(a,b,c):
    if (a >= b) and (a >= c): 
        largest = a 
    elif (b >= c): 
        largest = b 
    else: 
        largest = c 
    return largest 

def main():
    st.title("Find the Largest Number")

    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")


    if st.button("Find Largest Number"):
        result = find_largest(num1, num2, num3)
        st.success(f"The largest number is: {result}")

if __name__ == "__main__":
    main()
