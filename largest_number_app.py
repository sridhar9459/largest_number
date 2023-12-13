import streamlit as st

def find_largest(num1, num2, num3):
    # Find the largest number among the three
    return max(num1, num2, num3)

# Streamlit app
def main():
    st.title("Find the Largest Number")

    # User input for three numbers
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    # Button to calculate and display the result
    if st.button("Find Largest Number"):
        result = find_largest(num1, num2, num3)
        st.success(f"The largest number is: {result}")

if __name__ == "__main__":
    main()
