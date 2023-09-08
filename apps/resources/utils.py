def generate_cat_count_list(category_count):
    result = ''
    for cat in category_count:
        result += f"<li>{cat['cat_id__cat']}: {cat['cnt']}</li>"

    return result
