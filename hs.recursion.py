# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import hashlib

def hash_with_sha256(str):
        hash_object=hashlib.sha256(str.encode('utf-8'))
        hex_dig =hash_object.hexdigest()
        return hex_dig

def main ():

    hex_dig=hash_with_sha256('This is how you hast a string with sha256')
    print(hex_dig)
    
    unused_set = open('password_file.txt','r')
    
    def perm(cur_perm,unused_set):
        
        if len(unused_set) ==0:
            print (cur_perm)
            return
    
        for item in unused_set:
            new_cur_perm=cur_perm.copy()
            new_unused_set=unused_set.copy()
            new_cur_perm.append(item)
            perm(new_cur_perm, new_unused_set)
    
main()