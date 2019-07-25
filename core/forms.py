from django.shortcuts import render, redirect

class ApiRequest(forms.Form):
    template_name = 'core/send_request.html'
    
    def get(self, request):
        form = ApiRequest()
        return render(request, self.template_name, {'form':form})

    def post(self,request):
        form = ApiRequest(request.POST)
        if form.is_valid():
            text = clean_data['post']
            form = ApiRequest()
            return redirect('home:home')
        args = {'form':form, 'text':text}
        return render(request, 'core/get_request.html', args)