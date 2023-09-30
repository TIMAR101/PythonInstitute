# Prompt the user to enter a word
# and assign it to the user_word variable.

user_word = input().upper()


print(''.join(item for item in user_word if item not in ['A', 'E', 'I', 'O', 'U']))

