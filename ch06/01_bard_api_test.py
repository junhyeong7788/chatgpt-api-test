from bardapi import Bard

token = 'your_token'
bard = Bard(token=token, timeout=30)
result = bard.get_answer('your_question')

print(result)