
from pyrfc3339 import generate


def generate_text_field(text_field_dict):
    label = text_field_dict.get("label")
    return f"{label}: <br><input type=\"text\" name=\"{label}\"><br>"


def generate_checkbox_field(checkbox_field_dict):
    id = checkbox_field_dict.get("id")
    value = checkbox_field_dict.get("value")
    label = checkbox_field_dict.get('label')
    return f"<label><input type=\"checkbox\" id=\"{id}\" value=\"{value}\"> {label}<br>"


def build_html_form(field_list):
    with open("form_file.html", 'w') as f:
        f.write(
            f"<html><body>{generate_webform(field_list)}</body></html>"
        )


def generate_webform(field_dict_list):
    generate_field_list = []

    for field_dict in field_dict_list:
        if field_dict["type"] == "text_field":
            field_html = generate_text_field(field_dict)
        elif field_dict["type"] == "checkbox":
            field_html = generate_checkbox_field(field_dict)
        generate_field_list.append(field_html)

    generate_fields = "\n".join(generate_field_list)
    return f"<form>{generate_fields}</form>"


if __name__ == "__main__":
    field_list = [
        {
            "type": "text_field",
            "label": "Best text you have ever written",
            "name": "best_text",
        },
        {
            "type": "checkbox",
            "id": "check_it",
            "label": "1",
            "value": "Check for one",
        },
        {
            "type": "text_field",
            "label": "Another texr field",
            "name": "text_field2",
        }
    ]

    build_html_form(field_list)
