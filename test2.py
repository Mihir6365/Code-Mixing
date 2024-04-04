punc=['.',',','?','!',';',':']
sentence="this is a test, and I hope it words. this is another test."
temp=''
final=''

def run(temp):
    print(temp)
    return (temp).upper();


for char in sentence:
    if char in punc:
        final+=run(temp);
        temp='';
        final+=char;
    else:
        temp=temp+char;

print(final)