import streamlit as st
import requests

def insert_random_number():
    response = requests.get('http://localhost:5000/insert_random_number')  # Replace with your backend URL
    if response.status_code == 200:
        return True
    else:
        st.error(f"Failed to insert random number. Status code: {response.status_code}")
        return False

def get_random_number():
    response = requests.get('http://localhost:5000/get_random_number')  # Replace with your backend URL
    if response.status_code == 200:
        data = response.json()
        if 'random_number' in data:
            return data['random_number']
        else:
            st.error('Failed to fetch random number')
            return None
    else:
        st.error(f"Failed to fetch random number. Status code: {response.status_code}")
        return None

def main():
    st.title('MySQL Random Number App')

    if st.button('Generate and Insert Random Number'):
        if insert_random_number():
            st.success('Random number inserted successfully')

    if st.button('Get Random Number'):
        number = get_random_number()
        if number is not None:
            st.success(f'Random Number: {number}')

if __name__ == '__main__':
    main()
