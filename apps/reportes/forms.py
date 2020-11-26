from django import forms 

class num61(forms.Form):
    telescopio = forms.CharField(label='Telescopio, instrumento, infraestructura',initial="{{modelo17.telescopio_instrumento_infra}}", widget=forms.TextInput(
        attrs={"class":"form-control mb-3","name":"telescopio_instrumento_infra"}
    ))

    url = forms.URLField(label="Url", widget = forms.TextInput(
        attrs={"class":"form-control mb-3"}
    ))

    descripcion = forms.CharField(label="Descripcion", widget=forms.Textarea(
        attrs={"class":"form-control mb-3", "rows":3}
    ))

    anexo = forms.FileField(label="Anexo")