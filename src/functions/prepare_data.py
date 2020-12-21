def convert_to_html(data):
    prepare_message = "<u>Stats about Pandemic:</u>\n"
    for k, v in data.items():
        if k == "Num":
            continue
        prepare_message += f"<b>{k:45}</b>: {v}\n"
    return prepare_message
