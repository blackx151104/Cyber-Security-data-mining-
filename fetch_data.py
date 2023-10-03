import requests
def getdata(url,address):
    r=requests.get(url)
    with open(address,"a") as f:
        f.write(r.text)
url="https://www.amazon.in/iQOO-Stellar-Snapdragon-Segment-Included/dp/B07WHSR1NR/?_encoding=UTF8&pd_rd_w=9G84p&content-id=amzn1.sym.e5c03be3-10ba-4bc8-b9be-6fcea12320ed%3Aamzn1.symc.adba8a53-36db-43df-a081-77d28e1b71e6&pf_rd_p=e5c03be3-10ba-4bc8-b9be-6fcea12320ed&pf_rd_r=EFR4BHZQ56JY19048PK3&pd_rd_wg=XUtzJ&pd_rd_r=7a8725c9-3c50-4c5e-b282-ea0b257a071e&ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1"
getdata(url,"data/times.text")        