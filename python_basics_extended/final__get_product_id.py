def get_product_id(url: str) -> str:
    return url.rsplit("-p-",1)[1].split("-")[0]

product_url = "exampleshop.com/public-toilet-proximity-radar-p-in-my-url-007-01012020.html"
url_date_html = product_url[-14:]
p_string = product_url.rsplit("-p-",1)[1].split("-")[0]
p_string_2 = product_url.split("-p-")[1].rsplit("-",1)[0]

# print(url_date_html)
print(p_string)
# print(p_string_2)
print("-----")
print(get_product_id("exampleshop.com/public-toilet-proximity-radar-p-in-my-url-007-01012020.html"))