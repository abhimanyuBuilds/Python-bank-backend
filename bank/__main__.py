# from bank.models.customer import Customer
# from bank.models.account import Account
# from bank.services.customer_service import CustomerService
# from bank.services.transaction_service import TransactionService
# from bank.exceptions.custom_exceptions import InsufficientBalance
# # from bank.services.transaction_service import TransactionService

# def main():
#     customer_service = CustomerService()
#     transaction_service = TransactionService()

#     
#     customers = [
#         # Customer("Abhimanyu Singh","Meerut",'7983536144',"abhimanyu01","password123","abhi@gmail.com"),
#         # Customer("Rahul Kumar","Jaipur",'987456754',"Rahul887","85874Pass","rAhul877@gmail.com"),
#         # Customer("Ashok Kumar","J&K",'854587225',"AshoKK87","Aaasko4Pss","ASoKKK854@gmail.com"),
#         # Customer("Manoj Singh","Hisar",'978545854',"Manj976","M857AN00J","MaNoJ915@gmail.com"),
#         Customer("Krishan Gupta","Meerut",'85651545454',"KK785Gup","GUPPASS11","KKGUP254@gmail.com"),
#         Customer("Rohit Sharma","Udaipur",'758524582',"Rohit33","0MKI54","Rohit00@gmail.com"),
#         Customer("Avdesh Kumar","Purvanchal",'782365981',"Avdesh57","57Av4Pass","AV57@gmail.com"),
#         Customer("Rahul Sharma","Jaipur","9876543210","rahul12","Pass1234","rahul12@gmail.com"),
#         Customer("Anjali Mehra","Delhi","9876543211","anjali34","Pass5678","anjali34@yahoo.com"),
#         Customer("Rohit Verma","Mumbai","9876543212","rohit56","Pass9101","rohit56@gmail.com"),
#         Customer("Priya Singh","Bangalore","9876543213","priya78","Pass1121","priya78@outlook.com"),
#         Customer("Amit Gupta","Chennai","9876543214","amit90","Pass3141","amit90@gmail.com"),
#         Customer("Sneha Patel","Pune","9876543215","sneha21","Pass5161","sneha21@yahoo.com"),
#         Customer("Vikram Kumar","Kolkata","9876543216","vikram43","Pass7181","vikram43@gmail.com"),
#         Customer("Pooja Sharma","Delhi","9876543217","pooja65","Pass9202","pooja65@outlook.com"),
#         Customer("Arjun Verma","Jaipur","9876543218","arjun87","Pass1222","arjun87@gmail.com"),
#         Customer("Neha Singh","Mumbai","9876543219","neha09","Pass3242","neha09@yahoo.com"),
#         Customer("Karan Mehra","Chennai","9876543220","karan11","Pass5262","karan11@gmail.com"),
#         Customer("Ritu Patel","Pune","9876543221","ritu33","Pass7282","ritu33@outlook.com"),
#         Customer("Aditya Gupta","Kolkata","9876543222","aditya55","Pass9303","aditya55@gmail.com"),
#         Customer("Simran Sharma","Delhi","9876543223","simran77","Pass1323","simran77@yahoo.com"),
#         Customer("Mohit Kumar","Jaipur","9876543224","mohit99","Pass3343","mohit99@gmail.com"),
#         Customer("Sakshi Verma","Mumbai","9876543225","sakshi13","Pass5363","sakshi13@outlook.com"),
#         Customer("Ankit Singh","Chennai","9876543226","ankit35","Pass7383","ankit35@gmail.com"),
#         Customer("Divya Patel","Pune","9876543227","divya57","Pass9404","divya57@yahoo.com"),
#         Customer("Raghav Gupta","Kolkata","9876543228","raghav79","Pass1424","raghav79@gmail.com"),
#         Customer("Sanya Mehra","Delhi","9876543229","sanya01","Pass3444","sanya01@outlook.com"),
#         Customer("Yash Sharma","Jaipur","9876543230","yash23","Pass5464","yash23@gmail.com"),
#         Customer("Isha Verma","Mumbai","9876543231","isha45","Pass7484","isha45@yahoo.com"),
#         Customer("Kabir Singh","Chennai","9876543232","kabir67","Pass9505","kabir67@gmail.com"),
#         Customer("Mona Patel","Pune","9876543233","mona89","Pass1525","mona89@outlook.com"),
#         Customer("Rohan Gupta","Kolkata","9876543234","rohan11","Pass3545","rohan11@gmail.com"),
#         Customer("Anaya Sharma","Delhi","9876543235","anaya33","Pass5565","anaya33@yahoo.com"),
#         Customer("Dhruv Kumar","Jaipur","9876543236","dhruv55","Pass7585","dhruv55@gmail.com"),
#         Customer("Tanya Verma","Mumbai","9876543237","tanya77","Pass9606","tanya77@outlook.com"),
#         Customer("Veer Singh","Chennai","9876543238","veer99","Pass1626","veer99@gmail.com"),
#         Customer("Rhea Patel","Pune","9876543239","rhea21","Pass3646","rhea21@yahoo.com"),
#         Customer("Arnav Gupta","Kolkata","9876543240","arnav43","Pass5666","arnav43@gmail.com"),
#         Customer("Mira Sharma","Delhi","9876543241","mira65","Pass7686","mira65@outlook.com"),
#         Customer("Kabir Mehra","Jaipur","9876543242","kabir87","Pass9707","kabir87@gmail.com"),
#         Customer("Anika Verma","Mumbai","9876543243","anika09","Pass1727","anika09@yahoo.com"),
#         Customer("Vivaan Singh","Chennai","9876543244","vivaan31","Pass3747","vivaan31@gmail.com"),
#         Customer("Ira Patel","Pune","9876543245","ira53","Pass5767","ira53@outlook.com"),
#         Customer("Advik Gupta","Kolkata","9876543246","advik75","Pass7787","advik75@gmail.com"),
#         Customer("Tara Sharma","Delhi","9876543247","tara97","Pass9808","tara97@yahoo.com"),
#         Customer("Reyansh Kumar","Jaipur","9876543248","reyansh19","Pass1828","reyansh19@gmail.com"),
#         Customer("Kiara Verma","Mumbai","9876543249","kiara41","Pass3848","kiara41@outlook.com"),
#         Customer("Aarav Singh","Chennai","9876543250","aarav63","Pass5868","aarav63@gmail.com"),
#         Customer("Saanvi Patel","Pune","9876543251","saanvi85","Pass7888","saanvi85@outlook.com"),
#         Customer("Vivaan Sharma","Kolkata","9876543252","vivaan07","Pass9909","vivaan07@gmail.com"),
#         Customer("Diya Mehra","Delhi","9876543253","diya29","Pass1929","diya29@yahoo.com"),
#         Customer("Shaurya Verma","Jaipur","9876543254","shaurya51","Pass3949","shaurya51@gmail.com"),
#         Customer("Anvi Singh","Mumbai","9876543255","anvi73","Pass5969","anvi73@outlook.com"),
#         Customer("Krishna Patel","Chennai","9876543256","krishna95","Pass7989","krishna95@gmail.com"),
#         Customer("Rudra Gupta","Pune","9876543257","rudra17","Pass9000","rudra17@yahoo.com"),
#         Customer("Myra Sharma","Kolkata","9876543258","myra39","Pass1020","myra39@gmail.com"),
#         Customer("Aria Mehra","Delhi","9876543259","aria61","Pass3040","aria61@outlook.com"),
#         Customer("Aditya Verma","Jaipur","9876543260","aditya83","Pass5060","aditya83@gmail.com"),
#         Customer("Kiara Singh","Mumbai","9876543261","kiara05","Pass7080","kiara05@yahoo.com"),
#         Customer("Aarav Patel","Chennai","9876543262","aarav27","Pass9100","aarav27@gmail.com"),
#         Customer("Isha Gupta","Pune","9876543263","isha49","Pass1121","isha49@outlook.com"),
#         Customer("Raghav Sharma","Kolkata","9876543264","raghav71","Pass3141","raghav71@gmail.com"),
#         Customer("Saanvi Mehra","Delhi","9876543265","saanvi93","Pass5161","saanvi93@yahoo.com"),
#         Customer("Dhruv Verma","Jaipur","9876543266","dhruv15","Pass7181","dhruv15@gmail.com"),
#         Customer("Tara Singh","Mumbai","9876543267","tara37","Pass9202","tara37@gmail.com"),
#         Customer("Veer Patel","Chennai","9876543268","veer59","Pass1222","veer59@gmail.com"),
#         Customer("Anika Gupta","Pune","9876543269","anika81","Pass3242","anika81@gmail.com"),
#         Customer("Arnav Sharma","Kolkata","9876543270","arnav03","Pass5262","arnav03@gmail.com")
#     ]

    

#     customer_ids = []
#     for c in customers:
#         try:
#             cid = customer_service.create_customer(c)
#             customer_ids.append(cid)
#         except Exception as e:
#             print(f"Error adding customer {c.Name}: {e}")

    
    
   
#     accounts = []
#     for cid in customer_ids:
#         acc = Account(cid, "SAVINGS", 5000)  
#         acc_id = transaction_service.create_account(acc)
#         accounts.append(acc_id)

    

   
#     for idx, acc_id in enumerate(accounts):
        
#         transaction_service.deposit(acc_id, 2000 + idx * 500, "UPI")  
    
#         try:
#             transaction_service.withdraw(acc_id, 1000 + idx * 200, "CASH")  
#         except InsufficientBalance as e:
#             print(f"Insufficient Balance for Account {acc_id}: Attempted {e.attempted_withdraw}, Balance {e.balance}")

    
#     for acc_id in accounts:
#         balance = transaction_service.get_balance(acc_id)

#         print(f"Account {acc_id} final balance: {balance}")

# if __name__ == "__main__":
#     main()









