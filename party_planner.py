import sys

party_items = [
    "Cake",
    "Balloons",
    "Music System",
    "Lights",
    "Catering Service",
    "DJ",
    "Photo Booth",
    "Tables",
    "Chairs",
    "Drinks",
    "Party Hats",
    "Streamers",
    "Invitation Cards",
    "Party Games",
    "Cleaning Service"
]

def display_party_items(items):
    """
    Display the party items with their respective indices.
    """
    print("Party Items:")
    for index, item in enumerate(items):
        print(f"<p>{index}: {item}</p>")


def select_party_items(items):
    """
    Allow the user to select one or more items by their indices.
    """
    if sys.argv[1:]:
        selected_indices = ''.join(sys.argv[1:])
    else:
        selected_indices = input("Enter the indices of the items you want to select (comma-separated): ")
    if not selected_indices:
        print("No items selected.")
        return [], []
    selected_indices = [int(index.strip()) for index in selected_indices.split(",")]

    selected_items = [items[index] for index in selected_indices if index < len(items)]
    
    return selected_items, selected_indices


def calculate_base_party_code(selected_items):
    """
    Calculate the base party code using bitwise AND operation on the selected items.
    """
    values = [20, 21, 10, 5, 8, 3, 15, 7, 12, 6, 9, 18, 4, 2, 11]
    
    base_party_code = values[selected_items[0]]
    base_party_expression = f"Base Party Code: {base_party_code}"
    
    for index in selected_items[1:]:
        base_party_code &= values[index]
        base_party_expression += f" & {values[index]}"
    
    return base_party_code, base_party_expression + f" = {base_party_code}"


def modify_base_party_code(base_party_code):
    """
    Modify the base party code based on the specified conditions.
    """
    if base_party_code == 0:
        adjusted_party_code = f"Adjusted Party Code: {base_party_code} + 5"
        base_party_code += 5
        message = "Epic Party Incoming!"
    elif base_party_code > 5:
        adjusted_party_code = f"Adjusted Party Code: {base_party_code} - 2"
        base_party_code -= 2
        message = "Let's keep it classy!"
    else:
        adjusted_party_code = f"Adjusted Party Code: {base_party_code}"
        message = "Chill vibes only!"
    
    return base_party_code, message, adjusted_party_code


def render_output(selected_items, base_party_code, base_party_expression, message, adjusted_party_code):
    """
    Render the output in HTML format.
    """
    html_output = f"""
    <html>
        <head>
            <title>Party Planner</title>
        </head>
        <body>
            <h2>Your Selected Party Items:</h2>
            <ul>
                {''.join(f'<li>{item}</li>' for item in selected_items)}
            </ul>
            <h3>{base_party_expression}</h3>
            <h3>{adjusted_party_code}</h3>
            <h3>Final Party Code: {base_party_code}</h3>
            <h1>{message}</h1>
        </body>
    </html>
    """
    
    return html_output


def main():
    """
    Main function to run the party planner.
    """
    display_party_items(party_items)
    
    selected_items, selected_indices = select_party_items(party_items)
    
    if not selected_items:
        print("No items selected.")
        return
    
    base_party_code, base_party_code_expression = calculate_base_party_code(selected_indices)
    
    modified_base_party_code, message, adjusted_party_code_expression = modify_base_party_code(base_party_code)
    
    html_output = render_output(selected_items, modified_base_party_code, base_party_code_expression, message, adjusted_party_code_expression)
    
    print(html_output)


if __name__ == "__main__":
    main();