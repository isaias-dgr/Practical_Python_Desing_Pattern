class HtmlField:
    def __init__(self, **kwargs):
        self.html = ""

        if kwargs['field_type'] == "text_field":
            self.html = self.construct_text_field(kwargs["label"],
                                                  kwargs["field_name"])
        elif kwargs['field_type'] == "checkbox":
            self.html = self.contruct_checkbox(kwargs["field_id"],
                                               kwargs["value"],
                                               kwargs["label"])

    def construct_text_field(self, label, field_name):
        return f"{label}: <br><input type=\"text\" name \"{field_name}\"><br>"

    def construct_checkbox_field(self, id, value, label):
        return f"<label><input type=\"checkbox\" id=\"{id}\" value=\"{value}\"> {label}<br>"

    def __str__(self):
        return self.html


def generate_webform(field_dict_list):
    generate_field_list = []
    for field in field_dict_list:
        try:
            generate_field_list.append(str(HtmlField(**field)))
        except Exception as e:
            print(f"error: {e}")
    generated_fields = "\n".join(fields=generate_field_list)
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
