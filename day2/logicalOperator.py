# and  Both should be true
age = 20
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")
# or   At least one should be true
age = 12
has_ticket = True

if age >=18 or has_ticket:
    print("Allowed to enter")
else:
    print("Denied")
# not  Negation
light = "Red"

if not light =="Red":
    print("Go")
else:
    print("Stop")
    