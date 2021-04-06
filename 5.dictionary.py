pro={"tell":"say", "Protik":"AIUB", "Niloy": "Deffodil",
     "Amartya": "Kazi Nazrul University"}
print("Enter name to know university")
print(pro["Amartya"])
pro["Don"]="Home"
pro2=pro.copy()
del pro["tell"]
pro.update({"Bondhon":"RCS"})
print(pro)
print(pro2)