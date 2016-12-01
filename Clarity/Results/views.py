from django.shortcuts import render

# Create your views here.
def results(request):
	if request.method == "POST":
		a = request.POST.get("search")		
		print(a)
		return render(request, 'Results/index.html', {})
	else:
		return render(request, 'Results/index.html', {})
