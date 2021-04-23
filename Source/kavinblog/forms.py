from django import forms
from .models import Post, Category, Profile, Comment
#choices = [('coding', 'coding'), ('technology', 'technology'), ('gaming', 'gaming'),]
choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
	choice_list.append(item)



class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title','header_image', 'author','excerpt', 'category', 'body')

		widgets = {
			'title': forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter your Blog Title', 'text-color' : 'white'}),
			'author': forms.TextInput(attrs = {'class' : 'form-control', 'value' : '', 'id':'user', 'type':'hidden'}),
			'excerpt': forms.Textarea(attrs = {'class' : 'form-control', 'placeholder' : 'Tell about your blog in less than 255 words'}), 

			#'title_tag': forms.TextInput(attrs = {'class' : 'form-control', 'placeholder' : 'Enter your title tag'}), 
			#'author': forms.Select(attrs = {'class' : 'form-control'}),
			'category': forms.Select(choices=choice_list, attrs = {'class' : 'form-control'}), 
 			'body': forms.Textarea(attrs = {'class' : 'form-control', 'placeholder' : 'Enter the blog'}), 
 

		}


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name','body')

		widgets = {
      'name': forms.TextInput(attrs = {'class' : 'form-control', 'value' : '', 'id':'user', 'type':'hidden'}),
			
 			'body': forms.Textarea(attrs = {'class' : 'form-control', 'placeholder' : 'Enter the blog'}), 
 

		}


