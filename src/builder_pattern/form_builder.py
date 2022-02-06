from abc import ABCMeta, abstractclassmethod, abstractmethod


class Director(metaclass=ABCMeta):

    def __init__(self):
        self._builder = None

    def set_builder(self, builder):
        self._builder = builder

    @abstractmethod
    def construct(self):
        pass

    def get_constructed_object(self):
        return self._builder.constructed_object


class AbstractFormBuilder(metaclass=ABCMeta):

    def __init__(self):
        self.constructed_object = None

    @abstractmethod
    def add_text_field(self, field_dict):
        pass

    @abstractmethod
    def add_checkbox(self, checkout_dict):
        pass

    @abstractmethod
    def add_button(self):
        pass


class HtmlForm:

    def __init__(self):
        self.field_list = []

    def __repr__(self):
        return f"<form>{self.field_list}</form>"


class HtmlFormBuilder(AbstractFormBuilder):

    def __init__(self):
        self.constructed_object = HtmlForm()

    def add_text_field(self, field_dict):
        self.constructed_object.field_list.append(
            f"{field_dict['label']}: <br><input type=\"text\" name=\"{field_dict['field_name']}\"> "
        )

    def add_checkbox(self, checkbox_dict):
        self.constructed_object.field_list.append(f"""
        <label><input type=\"checkbox\" 
                      id=\"{checkbox_dict['field_id']}\"
                      value=\"{checkbox_dict['value']}\">
        {checkbox_dict['label']}<br>""")

    def add_button(self, button_dict):
        self.constructed_object.field_list.append(f"""\
          <button type=\"button\">{button_dict['text']}</button>"
          """)


class FormDirector(Director):

    def __init__(self):
        Director.__init__(self)

    def construct(self, field_list):
        for field in field_list:
            if field["field_type"] == "text_field":
                self._builder.add_text_field(field)
            elif field["field_type"] == "checkbox":
                self._builder.add_checkbox(field)
            elif field["field_type"] == "button":
                self._builder.add_button(field)


if __name__ == "__main__":
    director = FormDirector()
    html_form_builder = HtmlFormBuilder()
    director.set_builder(html_form_builder)

    field_list = [
        {
            "field_type": "text_field",
            "label": "Best text you have ever written",
            "field_name": "Field One"
        },
        {
            "field_type": "checkbox",
            "field_id": "check_it",
            "label": "Check for on",
            "value": "1"
        },
        {
            "field_type": "text_field",
            "label": "Another Text field",
            "field_name": "text_field2"
        },
        {
            "field_type": "button",
            "text": "DONE"
        }
    ]

    director.construct(field_list)

    with open("form_field.html", 'w') as f:
        f.write(f"""
        <html>
          <body>{director.get_constructed_object()}</body>
        </html>""")
