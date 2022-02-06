def generate_webform(text_field_list=[], checkbox_field_list=[]):
    generate_fields = "\n".join(
        map(
            lambda x: f"{x}:<br><input type=\"text\" name=\"{x}\"",
            text_field_list)
    )

    generate_fields += "\n".join(
        map(
            lambda x: "<label><input type=\"checkbox\" id=\"{x}\" value=\"\">{x}<br>",
            checkbox_field_list
        )
    )
    return f"<form>{generate_fields}</form>"


def build_html_form(text_fields, checkbox_fields):
    with open("form_file.html", 'w') as f:
        webform = generate_webform(text_fields, checkbox_fields)
        f.write(f"<html><body>{webform}</body></html>")


if __name__ == "__main__":
    text_fields = ["name", "age", "email", "telephone"]
    checkbox_fields = ["awsome", "bad"]
    build_html_form(text_fields, checkbox_fields)
