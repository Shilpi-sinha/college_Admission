from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    val1=int(request.POST["num"])
    val2=(request.POST["var"])
    if val1>70:
        text="yes, you are selected"
    
        return HttpResponse(text)
        #render('home.html', text='Yes you are selected')       
    elif(val2=="yes"):
        text="yes, you are selected"
    
        return HttpResponse(text)
    
        #return render('home.html', text='Yes you are selected')
        
    else:
        text="Sorry, you are not selected"
    
        return HttpResponse(text)
        #return render('home.html', text='Sorry,you are not selected')

    
    


