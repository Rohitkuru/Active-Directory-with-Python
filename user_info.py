from pyad import adquery,aduser,addomain

## Get all user related information 
q = adquery.ADQuery()

q.execute_query(
    attributes = ["distinguishedName", "sAMAccountName"],
    where_clause = "objectClass = '*'",
    base_dn = "CN=users, DC=centralapp, DC=com"
)
count = 0
for row in q.get_results():
    if row['sAMAccountName'] == "<enter_user_id>":
        count = count + 1
        print("User Found")

        aduser_user = aduser.ADUser(distinguished_name=row['distinguishedName'])
        print("AccountDisable ...{}".format(aduser_user.get_user_account_control_settings()['ACCOUNTDISABLE']))
        print(aduser_user.get_max_pwd_age())
        print("Password Expired .. {}".format(aduser_user.get_password_expired()))
        print("Last Password reset .. {}".format(aduser_user.get_password_last_set()))
        print("Expiry Date .. {}".format(aduser_user.get_expiration()))
        aduser_obj = aduser.ADObject(distinguished_name=row['distinguishedName'])
        print("Members Ofs .. ")
        for each in aduser_obj.get_memberOfs():
            print("\t"+ str(each))
        print(aduser_obj.dump_to_xml())

if count == 0:
    print("User id not found")
