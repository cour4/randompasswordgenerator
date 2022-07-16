

# Create your views here.
from django.shortcuts import render
from .form import checkboxes
import string
import random
  
# Create your views here.
def home(request):
	context = {}
	context['form'] = checkboxes()
    
	if request.method == 'POST':
        
		form = checkboxes(request.POST)

		if form.is_valid():
			x   = form.cleaned_data["chbox1"] 
			y   = form.cleaned_data['chbox2']
			b_l = form.cleaned_data['chbox3']
			z = form.cleaned_data['num']
            
			print(x,y,z)
            
			if (x == True and y ==True and b_l==True):
				
					string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=?/"]}<>{['
					context['pass'] = random.choices(string.ascii_letters,k=z)
					x = ''.join(map(str,context['pass']))
					context['pass'] = x 
			if (x == True and y ==True and b_l==False):
				
					string.ascii_letters = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+-=?/"]}<>{['
					context['pass'] = random.choices(string.ascii_letter,k=z)
					x = ''.join(map(str,context['pass']))
					context['pass'] = x 
			if (x == True and y ==False and b_l==False):
					string.ascii_letters = 'abcdefghijklmnopqrstuvwxyz1234567890'
					context['pass'] = random.choices(string.ascii_letters,k=z)
					x = ''.join(map(str,context['pass']))
					context['pass'] = x 
			if (x == False and y ==False and b_l==False):
					string.ascii_letters = 'abcdefghijklmnopqrstuvwxyz'
					context['pass'] = random.choices(string.ascii_letters,k=z)
					x = ''.join(map(str,context['pass']))
					context['pass'] = x 
			if (x == True and y ==False and b_l==True):
					string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
					context['pass'] = random.choices(string.ascii_letters,k=z)
					x = ''.join(map(str,context['pass']))
					context['pass'] = x 
			if (x ==False and y ==True and b_l==False):
					string.ascii_letters = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=?/"]}<>{['
					context['pass'] = random.choices(string.ascii_letters,k=z)
					x = ''.join(map(str,context['pass']))
					context['pass'] = x 
			if (x ==False and y ==False and b_l==True):
					string.ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
					context['pass'] = random.choices(string.ascii_letters,k=z)
					x = ''.join(map(str,context['pass']))
					context['pass'] = x 


		return render( request, "template/home.html", context)
	return render( request, "template/home.html", context)