import sys

# One node in the BST Cipher Tree


class Node:
    def __init__(self, ch):
        self.ch = ch
        self.left = None
        self.right = None


class Tree:

    # Create the BST Cipher tree based on the key
    def __init__(self, key):
        self.root = None
        for char in self.convert_string(key):
            self.insert(char)

    # Insert one new charater to the BST Cipher tree
    def insert(self, ch):
        new_node = Node(ch)
        if self.root is None:
            self.root = new_node
            return
        else:
            curr = self.root
            parent = self.root
            while curr is not None:
                parent = curr
                if curr.ch == ch:
                    break
                elif ch < curr.ch:
                    curr = curr.left
                else:
                    curr = curr.right   
            if ch < parent.ch:
                parent.left = new_node
            elif ch > parent.ch:
                parent.right = new_node
    
    def ch_present(self, node, ch):
        if node == None:
            return False
        elif node.ch == ch:
            return True
        elif ch < node.ch:
            return self.ch_present(node.left, ch)
        elif ch > node.ch:
            return self.ch_present(node.right, ch)

    # Encrypts a text message using the BST Tree
    def encrypt(self, message):
        message = self.convert_string(message)
        encrypted_msg = ''
        for char in message:
            code = self.encrypt_ch(char)
            if code != '':
                encrypted_msg += code + '!'
        return encrypted_msg[:-1]

    # Encrypts a single character
    def encrypt_ch(self, ch):
        encrypted_ch = ''
        # Return empty string if ch doesn't exist in BST
        if not self.ch_present(self.root, ch):
            return ''
        elif self.root.ch == ch:
            return '*'
        else:
            curr = self.root
            while curr != None and curr.ch != ch:
                if ch < curr.ch:
                    encrypted_ch += '<'
                    curr = curr.left
                elif ch > curr.ch:
                    encrypted_ch += '>'
                    curr = curr.right
            return encrypted_ch
            
    # Decrypts an encrypted message using the same BST Tree
    def decrypt(self, codes_string):
        codes = codes_string.split('!')
        decrypted_msg = ''
        for code in codes:
            decrypted_msg += self.decrypt_code(code)
        return decrypted_msg

    # Decrypts a single code
    def decrypt_code(self, code):
        try:
            curr = self.root
            for char in code:
                if char == '*':
                    return self.root.ch
                elif char == '<':
                    curr = curr.left
                elif char == '>':
                    curr = curr.right
            return curr.ch
        # Return empty string if code doesn't exist in BST
        except:
            return ''
            
    # Get printed version of BST for debugging

    def BST_print(self):
        if self.root is None:
            return
        self.BST_print_helper(self.root)

    # Prints a BST subtree
    def BST_print_helper(self, node, level=0):
        if node is not None:
            if node.right is not None:
                self.BST_print_helper(node.right, level + 1)
            print('     ' * level + '->', node.ch)
            if node.left is not None:
                self.BST_print_helper(node.left, level + 1)

    # Utility method
    def isValidLetter(self, ch):
        if (ch >= "a" and ch <= "z"):
            return True
        return False

    # Utility method
    def isValidCh(self, ch):
        if (ch == " " or self.isValidLetter(ch)):
            return True
        return False
    
    
    # Convert string to lowercase letters with spaces
    def convert_string(self, string):
        result = ''
        for i in range(len(string)):
            # letter
            if string[i].isalpha():
                result += string[i].lower()
            # space
            elif string[i] == ' ':
                result += ' '
        return result

def main():

    # Debug flag - set to False before submitting
    debug = False
    if debug:
        in_data = open('bst_cipher.in')
    else:
        in_data = sys.stdin

    # read encryption key
    key = in_data.readline().strip()

    # create a Tree object
    key_tree = Tree(key)

    # for debug purposes. comment out before turning it in. key_tree.BST_print()

    # read string to be encrypted
    text_message = in_data.readline().strip()
    
    # print the encryption
    print(key_tree.encrypt(text_message))

    # read the string to be decrypted
    coded_message = in_data.readline().strip()

    # print the decryption
    print(key_tree.decrypt(coded_message))


if __name__ == "__main__":
    main()
