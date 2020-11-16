from pyad import aduser,adobject,addomain


user = aduser.ADUser.from_cn("<user_name>",options=dict(ldap_server="<enter_domain_name_here>"))


### This will print all user attributes
for x in user.get_allowed_attributes():
    print(x)

#print(user.get_attribute('distinguishedName'))

user_obj = adobject.ADObject(distinguished_name=user.get_attribute('distinguishedName')[0])

aduser_user = aduser.ADUser(distinguished_name=user.get_attribute('distinguishedName')[0])

#for x in aduser_user.get_allowed_attributes():
#    print(x['ACCOUNTDISABLE'])

#print(aduser_user.get_user_account_control_settings()['ACCOUNTDISABLE'])
#print(aduser_user.get_optional_attributes())
#print(aduser_user.get_mandatory_attributes())

#for x , y in aduser_user.get_user_account_control_settings().items():
#    print(x,y)

print(aduser_user.get_allowed_attributes())
print(aduser_user.get_optional_attributes())
print(aduser_user.get_attribute("email"))


#print(aduser_user.get_memberOfs())
#user.set_password("MyNewPassword123")
#print(user_obj.get_user_account_control_settings())
#print(user.get_user_account_control_settings())
#print(aduser_user.get_max_pwd_age())
#print(aduser_user.get_password_expired())
#print(aduser_user.get_password_last_set())
#print(aduser_user.get_expiration())
#aduser_user.set_password("India@124")
#aduser_user.force_pwd_change_on_login()
