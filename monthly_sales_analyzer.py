# Example data
sales_data = [
    {"day": 1, "product_a": 202, "product_b": 142, "product_c": 164},
    {"day": 2, "product_a": 206, "product_b": 121, "product_c": 338},
    {"day": 3, "product_a": 120, "product_b": 152, "product_c": 271},
    {"day": 4, "product_a": 174, "product_b": 137, "product_c": 266},
    {"day": 5, "product_a": 199, "product_b": 153, "product_c": 301},
    {"day": 6, "product_a": 230, "product_b": 199, "product_c": 202},
    {"day": 7, "product_a": 101, "product_b": 137, "product_c": 307},
    {"day": 8, "product_a": 137, "product_b": 179, "product_c": 341},
    {"day": 9, "product_a": 287, "product_b": 70, "product_c": 310},
    {"day": 10, "product_a": 157, "product_b": 71, "product_c": 238},
    {"day": 11, "product_a": 148, "product_b": 108, "product_c": 319},
    {"day": 12, "product_a": 287, "product_b": 64, "product_c": 339},
    {"day": 13, "product_a": 289, "product_b": 100, "product_c": 257},
    {"day": 14, "product_a": 154, "product_b": 113, "product_c": 280},
    {"day": 15, "product_a": 150, "product_b": 184, "product_c": 170},
    {"day": 16, "product_a": 172, "product_b": 67, "product_c": 281},
    {"day": 17, "product_a": 188, "product_b": 109, "product_c": 163},
    {"day": 18, "product_a": 108, "product_b": 139, "product_c": 202},
    {"day": 19, "product_a": 229, "product_b": 133, "product_c": 241},
    {"day": 20, "product_a": 210, "product_b": 57, "product_c": 324}
]

def total_sales_by_product(data, product_key):
    """Calculates the total sales of a specific product in 30 days."""
    total_sales=0
    for i in data:
        total_sales=total_sales+i[product_key]
    return total_sales

def average_daily_sales(data, product_key):
    """Calculates the average daily sales of a specific product."""
    average_daily_sales=total_sales_by_product(data, product_key)/len(data)
    return average_daily_sales

def best_selling_day(data):
    """Finds the day with the highest total sales."""
    highest_daily_total_sales=0
    for i in data:
        daily_total_sales=i["product_a"]+i["product_b"]+i["product_c"]
        if daily_total_sales>highest_daily_total_sales:
            highest_daily_total_sales=daily_total_sales
            best_day=i["day"]
    return str(best_day) + " (with " + str(highest_daily_total_sales) + " sales)"

def days_above_threshold(data, product_key, threshold):
    """Counts how many days the sales of a product exceeded a given threshold."""
    number_days_exceeded=0
    for i in data:
        product_daily_sales=i[product_key]
        if product_daily_sales>threshold:
            number_days_exceeded += 1
    return number_days_exceeded

def top_product(data):
    """Determines which product had the highest total sales in 30 days."""
    total_sales_product_a=0
    total_sales_product_b=0
    total_sales_product_c=0
    for i in data:
        total_sales_product_a += i["product_a"]
        total_sales_product_b += i["product_b"]
        total_sales_product_c += i["product_c"]
    total_sales_top_product=max(total_sales_product_a,total_sales_product_b,total_sales_product_c)
    if total_sales_product_a==total_sales_top_product:
        best_product="product_a"
    if total_sales_product_b==total_sales_top_product:
        best_product="product_b"
    if total_sales_product_c==total_sales_top_product:
        best_product="product_c"
    return best_product + " (with a total of " + str(total_sales_top_product) + " sales)"

print("Total sales of product_a:", total_sales_by_product(sales_data, "product_a"))
print("Average daily sales of product_b:", average_daily_sales(sales_data, "product_b"))
print("Day with highest total sales:", best_selling_day(sales_data))
print("Days when product_c exceeded 300 sales:", days_above_threshold(sales_data, "product_c", 300))
print("Product with highest total sales:", top_product(sales_data))

#Extra exercise no.1
def worst_selling_day(data):
    """Finds the day with the lowest total sales."""
    first_day = data[0]
    lowest_daily_total_sales = first_day["product_a"] + first_day["product_b"] + first_day["product_c"]
    worst_day = first_day["day"]

    for i in data:
        daily_total_sales=i["product_a"]+i["product_b"]+i["product_c"]
        if daily_total_sales<lowest_daily_total_sales:
            lowest_daily_total_sales=daily_total_sales
            worst_day=i["day"]
    return str(worst_day) + " (with " + str(lowest_daily_total_sales) + " sales)"

print("Day with lowest total sales:", worst_selling_day(sales_data))

#Extra exercise no.2
def get_total_sales(data):
    return data["total_daily_sales"]

def tier_selling_days(data):
    """Sorts days by total sales and shows top 3."""
    total_daily_sales_list=[]
    for i in data:
        total_daily_sales_list.append({"day":i["day"],"total_daily_sales":i["product_a"] + i["product_b"] + i["product_c"]})
    sorted_total_daily_sales_list = sorted(total_daily_sales_list, key=get_total_sales, reverse=True)
    return \
            "-1st position for day " + str(sorted_total_daily_sales_list[0]["day"]) + " (" + str(sorted_total_daily_sales_list[0]["total_daily_sales"]) + " sales)\n" \
            " -2nd position for day " + str(sorted_total_daily_sales_list[1]["day"]) + " (" + str(sorted_total_daily_sales_list[1]["total_daily_sales"]) + " sales)\n" \
            " -3rd position for day " + str(sorted_total_daily_sales_list[2]["day"]) + " (" + str(sorted_total_daily_sales_list[2]["total_daily_sales"]) + " sales)" 

print("TIER:\n", tier_selling_days(sales_data))

#Extra exercise no.3
def get_sales_range_by_product(data, product_key):
    """Calculates the sales range (max-min) of a specific product."""
    first_day = data[0]
    product_max = first_day[product_key]
    product_min= first_day[product_key]
    for i in data:
        product_daily_sales=i[product_key]
        if product_daily_sales>product_max:
            product_max = product_daily_sales
        if product_daily_sales<product_min:
            product_min = product_daily_sales
    sales_range=product_max-product_min
    return str(sales_range) + " sales"

print("Sales range for product_c:", get_sales_range_by_product(sales_data,"product_c"))