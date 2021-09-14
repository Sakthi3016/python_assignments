#1)CHECK THE is OPERATOR ON FLOAT AND STRING
a=256
b=256
a is b  #true

a=257
b=257
a is b #false

#The above code is beacause of caching principle


#is checks whether both operand refer to same object or not if it is pointing to same object the answer will be true
float(20) is float(20) #false

float(0.0) is float(0.0) #true

# == operator compares the values of operand and value
a=257
b=257
a==b #true

 1>3>4  #answer:false
#first we compare 1>3 which is false
# second we compare 3>4 whuch is also false

