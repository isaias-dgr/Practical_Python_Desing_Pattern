from pyrfc3339 import generate


def generate_webform(field_dict_list):
    generated_field_list = []

    for field_dict in field_dict_list:
        label = field_dict.get("label")
        if field_dict["type"] == "text_field":
            name = field_dict.get("name")
            generated_field_list.append(
                f"{label}:<br><input type=\"text\" name=\"{name}\"><br>"
            )
        elif field_dict["type"] == "checkbox":
            id = field_dict.get("id")
            value = field_dict.get("value")
            generated_field_list.append(
                f"<label><input type=\"checkbox\" id=\"{id}\" value=\"{value}\">{label}<br>"
            )
    generated_fields = "\n".join(generated_field_list)
    return f"<form>{generated_fields}</form>"


def build_html_form(field_list):
    with open("form_file.html", 'w') as f:
        f.write(
            f"<html><body>{generate_webform(field_list)}</body></html>"
        )


if __name__ == "__main__":
    field_list = [
        {
            "type": "text_field",
            "label": "Best text you have ever written",
            "name": "best_text"
        },
        {
            "type": "checkbox",
            "id": "check_it",
            "label": "Check for one",
            "value": "1"
        },
        {
            "type": "text_field",
            "label": "Another Text field",
            "name": "text_field2"
        }
    ]

    build_html_form(field_list)
