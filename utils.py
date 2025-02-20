def get_products(products):
    answer_text = ""    
    for data in products:
            answer_text += f"{data.get("name")} - {data.get("price")}руб.\n"
    return answer_text