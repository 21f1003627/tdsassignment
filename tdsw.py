import streamlit as st

def greatest_of_three(a, b, c):
    # Find the maximum of three numbers
    return max(a, max(b, c))

# Create a Streamlit app
def main():
    st.title("Greatest of Three Numbers")

    # Get user input
    a = st.number_input("Enter the first number:")
    b = st.number_input("Enter the second number:")
    c = st.number_input("Enter the third number:")

    # Calculate the greatest of the three
    greatest = greatest_of_three(a, b, c)

    # Display the result
    st.write(f"The greatest of the three numbers is: {greatest}")

if __name__ == "__main__":
    main()
