print("==== Simple Interest Calculator====")

principal=float(input("Enter the vaue of principal: rs"))
amount=float(input("Enter the value of amount: rs"))
rate=float(input("Enter the annual interest rate:"))
time=float(input("Enter time in years:"))

interest=(principal*rate*time)/100
total_amount=principal+interest

print("\n==== Result ====")
print("Principal amount:rs",principal)
print("Simple interest: rs",interest)
print("Total Amount: rs",total_amount)