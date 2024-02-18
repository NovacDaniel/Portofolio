while True:
    _1st_nr=(input("First number: "))  
    _2th_nr=(input("Secand number: "))
    operator=input("Select operator: ")

    
    if not (_1st_nr.strip().replace('.', '', 1).isdigit() and _2th_nr.strip().replace('.', '', 1).isdigit()):
        print("Error: Parameters need to be numbers and corect operator! (use only: + - / * ).")
        
    else:
        
        def calculator():
            nr_float1=float(_1st_nr)
            nr_float2=float(_2th_nr)

            if operator== "+":
                return nr_float1 + nr_float2
            elif operator=="-":
                return nr_float1 - nr_float2
            elif operator=="/":
                if nr_float2!=0:
                    return nr_float1 / nr_float2
                else:
                    return f"Infinity"       
             
            elif operator=="*":
                return nr_float1 * nr_float2 
            else:
                print("The operator is not corect! (use only: + - / * )")
        print(calculator())
    print()    
    print("IRY AGAYN!")
    print()    
