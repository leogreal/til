# Adicionando attrs aos campos de formulário do Django.

Para habilitar novos templatetags basta criar um arquivo para implementar as novas templates tags. No meu caso eu criei um diretório templatetags e dentro dele criei o arquivo form_widgets.py.

Exemplo do meu "form_widgets.py"

```
from django.template import Library

register = Library()

@register.filter
def add_classes(widget, classes):
    widget.field.widget.attrs['class'] = classes
    return widget


@register.filter
def add_placeholder(widget, placeholder):
    widget.field.widget.attrs['placeholder'] = placeholder
    return widget


@register.filter
def add_key_value_attr(widget, key_value):
    attr, value = key_value.split(',')
    widget.field.widget.attrs[attr] = value
    return widget
```

Depois no settings do Django, em TEMPLATES tem que colocar dentro de OPTIONS o diretório da librarie.

```
'libraries': {
    'form_widgets': 'spm_web.templatetags.form_widgets',}
```

Para finalizar, no arquivo de template sempre que precisar usar as tags, basta importar a customização.

```
{% load form_widgets %}
<form class="form" method="post" action="">
    {{ form.name.label_tag }}
    {{ form.name|add_classes:"form-control"|add_placeholder:"Seu Nome" }}

    {{ form.email.label_tag }}
    {{ form.email|add_classes:"form-control"|add_placeholder:"email@example.com" }}

    <button type="submit" class="btn btn-primary">Send</button>
</form>
```
