users.update({newUsername: users[existEmail]}) # update the username
            del users[existEmail]