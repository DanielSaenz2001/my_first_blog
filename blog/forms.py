from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text','create_date','entrega_date')
        



    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] ='form-control'

        self.fields['entrega_date'].widget.input_type='date'
          
        