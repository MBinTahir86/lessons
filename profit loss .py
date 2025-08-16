money=int(input("write the cost on which you buyed the thing"))

sellingprice=int(input("write the cost on which you sold the thing"))
print(sellingprice - money)
if sellingprice > money:
    print("you got profit")
else:
    print("you got loss")
