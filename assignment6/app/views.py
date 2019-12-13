from django.shortcuts import render

# Create your views here.
def show(request):
    return render(request, "one.html")


def songs(request):
   n = request.GET.get("x")
   p = request.GET.get("y")
   a = request.GET.get("z")
   if n == "album1":
       res1 = "yes"
   else:
       res1 = None
   if p == "album2":
       res2 = "yes"
   else:
       res2 = None
   if a == "album3":
       res3 = "yes"
   else:
       res3 = None
   data = {'res1': res1, 'res2': res2, 'res3': res3}
   return render(request, "two.html", {'data1': data})

